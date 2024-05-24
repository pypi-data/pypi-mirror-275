from .initializers import RandomNormal
from ..utils.data import get_auto_embedding_dim


class DenseFeature(object):
    """
    连续型特征
    """

    def __init__(self, name):
        self.name = name
        self.embed_dim = 1

    # 定义对象的字符串表示形式
    def __repr__(self):
        return f'<DenseFeature {self.name}>'


class SparseFeature(object):
    """
    离散型特征
    Args:
        name (str): feature's name.
        vocab_size (int): vocabulary size of embedding table.
        embed_dim (int): embedding vector's length
        shared_with (str): 某特征名称，与其共享embedding table，例如序列特征中的元素可能是某离散特征，它们需共享embedding表示
        padding_idx (int, optional): If specified, the entries at padding_idx will be masked 0 in InputMask Layer.
        initializer(Initializer): Initializer the torch.nn.embedding weight.
    """

    def __init__(self, name, vocab_size, embed_dim=None, shared_with=None, padding_idx=None,
                 initializer=RandomNormal(0, 0.0001)):
        self.name = name
        self.vocab_size = vocab_size
        if embed_dim is None:
            self.embed_dim = get_auto_embedding_dim(vocab_size)
        else:
            self.embed_dim = embed_dim
        self.shared_with = shared_with
        self.padding_idx = padding_idx
        self.initializer = initializer

    def __repr__(self):
        return f'<SparseFeature {self.name} with Embedding shape ({self.vocab_size}, {self.embed_dim})>'

    def get_embedding_layer(self):
        if not hasattr(self, 'embed'):
            self.embed = self.initializer(self.vocab_size, self.embed_dim)
        return self.embed


class SequenceFeature(object):
    """
    序列特征（通常是由一系列离散特征组成）
    Note：训练之前需要先对SequenceFeature进行padding操作，保证维度一致

    Args:
        name (str): feature's name.
        vocab_size (int): vocabulary size of embedding table.
        embed_dim (int): embedding vector's length
        pooling (str): pooling method, support `["mean", "sum", "concat"]` (default=`"mean"`)
        shared_with (str): 参考SparseFeature
        padding_idx (int, optional): If specified, the entries at padding_idx will be masked 0 in InputMask Layer.
        initializer(Initializer): Initializer the embedding layer weight.
    """

    def __init__(self,
                 name,
                 vocab_size,
                 embed_dim=None,
                 pooling="mean",
                 shared_with=None,
                 padding_idx=None,
                 initializer=RandomNormal(0, 0.0001)):
        self.name = name
        self.vocab_size = vocab_size
        if embed_dim is None:
            self.embed_dim = get_auto_embedding_dim(vocab_size)
        else:
            self.embed_dim = embed_dim
        self.pooling = pooling
        self.shared_with = shared_with
        self.padding_idx = padding_idx
        self.initializer = initializer

    def __repr__(self):
        return f'<SequenceFeature {self.name} with Embedding shape ({self.vocab_size}, {self.embed_dim})>'

    def get_embedding_layer(self):
        if not hasattr(self, 'embed'):
            self.embed = self.initializer(self.vocab_size, self.embed_dim)
        return self.embed
