import numpy as np
from torch.utils.data import Dataset, DataLoader, random_split


def get_auto_embedding_dim(num_classes):
    """
    根据离散种类数目自动确定embedding向量维度
    emb_dim = [6 * (num_classes)^(1/4)]
    reference: Deep & Cross Network for Ad Click Predictions.(ADKDD'17)
    """
    return np.floor(6 * np.pow(num_classes, 0.26))


def pad_sequences(sequences, maxlen=None, dtype='int32', padding='pre', truncating='pre', value=0.):
    """
    填充序列
    Args:
        sequences (pd.DataFrame): data that needs to pad or truncate
        maxlen (int): maximum sequence length. Defaults to None.
        dtype (str, optional): Defaults to 'int32'.
        padding (str, optional): if len(sequences) less than maxlen, padding style, {'pre', 'post'}. Defaults to 'pre'.
        truncating (str, optional): if len(sequences) more than maxlen, truncate style, {'pre', 'post'}. Defaults to 'pre'.
        value (_type_, optional): Defaults to 0..
    """

    assert padding in ["pre", "post"], "Invalid padding={}.".format(padding)
    assert truncating in ["pre", "post"], "Invalid truncating={}.".format(truncating)

    if maxlen is None:
        maxlen = max(len(x) for x in sequences)
    arr = np.full((len(sequences), maxlen), value, dtype=dtype)
    for idx, x in enumerate(sequences):
        if len(x) == 0:
            continue  # empty list
        if truncating == 'pre':
            trunc = x[-maxlen:]
        else:
            trunc = x[:maxlen]
        trunc = np.asarray(trunc, dtype=dtype)

        if padding == 'pre':
            arr[idx, -len(trunc):] = trunc
        else:
            arr[idx, :len(trunc)] = trunc
    return arr


def df_to_dict(data):
    """
    Convert the DataFrame to a dict type input that the network can accept
    Args:
        data (pd.DataFrame): datasets of type DataFrame
    Returns:
        The converted dict, which can be used directly into the input network
    """
    data_dict = data.to_dict('list')
    for key in data.keys():
        data_dict[key] = np.array(data_dict[key])
    return data_dict


class TorchDataset(Dataset):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def __getitem__(self, index):
        return {k: v[index] for k, v in self.x.items()}, self.y[index]

    def __len__(self):
        return len(self.y)


class PredictDataset(Dataset):

    def __init__(self, x):
        super().__init__()
        self.x = x

    def __getitem__(self, index):
        return {k: v[index] for k, v in self.x.items()}

    def __len__(self):
        return len(self.x[list(self.x.keys())[0]])


class MatchDataGenerator(object):

    def __init__(self, x, y=[]):
        super().__init__()
        if len(y) != 0:
            self.dataset = TorchDataset(x, y)
        else:  # For pair-wise model, trained without given label
            self.dataset = PredictDataset(x)

    def generate_dataloader(self, x_test_user, x_all_item, batch_size, num_workers=8):
        train_dataloader = DataLoader(self.dataset, batch_size=batch_size, shuffle=True, num_workers=num_workers)

        test_dataset = PredictDataset(x_test_user)
        # shuffle = False to keep same order as ground truth
        test_dataloader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=num_workers)

        item_dataset = PredictDataset(x_all_item)
        item_dataloader = DataLoader(item_dataset, batch_size=batch_size, shuffle=False, num_workers=num_workers)
        return train_dataloader, test_dataloader, item_dataloader
