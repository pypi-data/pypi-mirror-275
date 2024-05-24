import torch
import torch.nn as nn

from .features import DenseFeature, SparseFeature, SequenceFeature
from .activation import activation_layer


class EmbeddingLayer(nn.Module):
    """
    Initial Input: features(list):一般有三种类型，详见./features.py
    Forward Input:
        x(dict):{feature_name:feature_value}，feature_value取决于特征类型，
                Dense/SparseFeature的shape：（batch_size,）SequenceFeature的shape：（batch_size,seq_len）
        features(list): forward过程中涉及的特征
        squeeze_dim(bool):
    Forward Output:取决于特征类型以及是否squeeze，详见代码逻辑
                   DenseFeature:(batch_size,num_features_dense)
                   SparseFeature:(batch_size,num_features,embed_dim)
                   SequenceFeature:()
    """

    def __init__(self, features):
        super().__init__()
        self.features = features
        # 存储对应离散特征的EmbeddingTable
        self.embed_dict = nn.ModuleDict()
        self.n_dense = 0
        for fea in features:
            if fea.name in self.embed_dict:
                continue
            if isinstance(fea, SparseFeature) and fea.shared_with == None:
                self.embed_dict[fea.name] = fea.get_embedding_layer()
            elif isinstance(fea, SequenceFeature) and fea.shared_with == None:
                self.embed_dict[fea.name] = fea.get_embedding_layer()
            elif isinstance(fea, DenseFeature):
                # 连续型特征无需embedding
                self.n_dense += 1

    def forward(self, x, features, squeeze_dim=False):
        sparse_emb, dense_values = [], []
        sparse_exists, dense_exists = False, False
        for fea in features:
            if isinstance(fea, SparseFeature):
                if fea.shared_with == None:
                    # SparseFeature:(batch_size,1,embed_dim)
                    sparse_emb.append(self.embed_dict[fea.name](x[fea.name].long()).unsqueeze(1))
                else:
                    # 存在共享embedding table
                    sparse_emb.append(self.embed_dict[fea.shared_with](x[fea.name].long()).unsqueeze(1))
            elif isinstance(fea, SequenceFeature):
                if fea.pooling == "sum":
                    pooling_layer = SumPooling()
                elif fea.pooling == "mean":
                    pooling_layer = AveragePooling()
                elif fea.pooling == "concat":
                    pooling_layer = ConcatPooling()
                else:
                    raise ValueError("Sequence pooling method supports only pooling in %s, got %s." %
                                     (["sum", "mean"], fea.pooling))
                # 输入序列掩码，告知模型哪些部分是有效输入，哪些是无效（填充）
                fea_mask = InputMask()(x, fea)
                if fea.shared_with == None:
                    # 根据Pooling的不同，返回的形状也不同
                    # TODO：如果Pooling为ConcatPooling，则最终shape为（batch_size,1,seq_len,embed_dim）。貌似存在bug？？
                    # 其他均为(batch_size,embed_dim)
                    sparse_emb.append(
                        pooling_layer(self.embed_dict[fea.name](x[fea.name].long()), fea_mask).unsqueeze(1))
                else:
                    sparse_emb.append(
                        pooling_layer(self.embed_dict[fea.shared_with](x[fea.name].long()), fea_mask).unsqueeze(
                            1))
            else:
                # (batch_size,1,)
                dense_values.append(x[fea.name].float().unsqueeze(1))

        if len(dense_values) > 0:
            dense_exists = True
            dense_values = torch.cat(dense_values, dim=1)
        if len(sparse_emb) > 0:
            sparse_exists = True
            sparse_emb = torch.cat(sparse_emb, dim=1)  # [batch_size, num_features, embed_dim]

        if squeeze_dim:
            # TODO：为什么需要squeeze_dim??
            # Note: if the emb_dim of sparse features is different, we must squeeze_dim
            if dense_exists and not sparse_exists:  # only input dense features
                return dense_values
            elif not dense_exists and sparse_exists:
                return sparse_emb.flatten(start_dim=1)  # squeeze dim to : [batch_size, num_features*embed_dim]
            elif dense_exists and sparse_exists:
                return torch.cat((sparse_emb.flatten(start_dim=1), dense_values),
                                 dim=1)  # concat dense value with sparse embedding
            else:
                raise ValueError("The input features can note be empty")
        else:
            if sparse_exists:
                return sparse_emb  # [batch_size, num_features, embed_dim]
            else:
                raise ValueError(
                    "If keep the original shape:[batch_size, num_features, embed_dim], expected %s in feature list, got %s" %
                    ("SparseFeatures", features))


class SumPooling(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, mask=None):
        if mask == None:
            return torch.sum(x, dim=1)
        else:
            # bmm：两矩阵的批量乘法，也即A（batch_size,m,n）B(batch_size,n,p)=>(batch_size,m,p)
            # （batch_size,embed_dim）
            return torch.bmm(mask, x).squeeze(1)


class AveragePooling(nn.Module):
    """
    Shape:
        - Input
            x: `(batch_size, seq_length, embed_dim)`
            mask: `(batch_size, 1（num_features_seq??）, seq_length)`
        - Output: `(batch_size, embed_dim)`
    """

    def __init__(self):
        super().__init__()

    def forward(self, x, mask=None):
        if mask == None:
            return torch.mean(x, dim=1)
        else:
            sum_pooling_matrix = torch.bmm(mask, x).squeeze(1)
            non_padding_length = mask.sum(dim=-1)
            return sum_pooling_matrix / (non_padding_length.float() + 1e-16)


class ConcatPooling(nn.Module):
    """
    Shape:
    - Input: `(batch_size, seq_length, embed_dim)`
    - Output: `(batch_size, seq_length, embed_dim)`
    """

    def __init__(self):
        super().__init__()

    def forward(self, x, mask=None):
        # 由于EmbeddingLayer包含拼接操作，故此处直接返回即可
        return x


class InputMask(nn.Module):
    """
    # 输入序列掩码，告知模型哪些部分是有效输入，哪些是无效（填充）
    Forward Input:
      x (dict): 同EmbeddingLayer
      features (list/SparseFeature/SequenceFeature):TODO：一般来说应该是序列特征
    Forward Output:
      - if input Sparse: `(batch_size, num_features)`
      - if input Sequence: `(batch_size, num_features_seq, seq_length)`
    """

    def __init__(self):
        super().__init__()

    def forward(self, x, features):
        mask = []
        if not isinstance(features, list):
            features = [features]
        for fea in features:
            if isinstance(fea, SparseFeature) or isinstance(fea, SequenceFeature):
                if fea.padding_idx != None:
                    # （batch_size,seq_len）
                    fea_mask = x[fea.name].long() != fea.padding_idx
                else:
                    # 默认padding的填充元素为-1
                    fea_mask = x[fea.name].long() != -1
                mask.append(fea_mask.unsqueeze(1).float())
            else:
                raise ValueError("Only SparseFeature or SequenceFeature support to get mask.")
        return torch.cat(mask, dim=1)


class MLP(nn.Module):
    """
    多层感知机模型，最简单的全连接层神经网络
    Note we default add `BatchNorm1d`,`Activation` and `Dropout` for each `Linear` Module.

    Args:
        input dim (int): input size of the first Linear Layer.
        output_layer (bool): whether this MLP module is the output layer. If `True`, then append one Linear(*,1) module.
        dims (list): output size of Linear Layer (default=[]).
        dropout (float): probability of an element to be zeroed (default = 0.5).
        activation (str): the activation function, support `[sigmoid, relu, prelu, dice, softmax]` (default='relu').

    Shape:
        - Input: `(batch_size, input_dim)`
        - Output: `(batch_size, 1)` or `(batch_size, dims[-1])`
    """

    def __init__(self, input_dim, output_layer=True, dims=None, dropout=0, activation="relu"):
        super().__init__()
        if dims is None:
            # 隐含层数量
            dims = []
        layers = list()
        for i_dim in dims:
            layers.append(nn.Linear(input_dim, i_dim))
            layers.append(nn.BatchNorm1d(i_dim))
            layers.append(activation_layer(activation))
            layers.append(nn.Dropout(p=dropout))
            input_dim = i_dim
        if output_layer:
            layers.append(nn.Linear(input_dim, 1))
        self.mlp = nn.Sequential(*layers)

    def forward(self, x):
        return self.mlp(x)
