import pandas as pd
import random, tqdm, copy
import numpy as np
from collections import OrderedDict, Counter
from .data import pad_sequences, df_to_dict


def negative_sample(items_cnt_order, ratio, method_id=0):
    """
    Negative Sample method for matching model
    Args:
        items_cnt_order (dict): the item count dict, the keys(item) sorted by value(count) in reverse order.
        ratio (int): negative sample ratio, >= 1
        method_id (int, optional):
        `{
            0: "random sampling",
            1: "popularity sampling method used in word2vec",
            2: "popularity sampling method by `log(count+1)+1e-6`",
            3: "tencent RALM sampling"
        }`. Defaults to 0.

    Returns:
        list: sampled negative item list
    """
    items_set = [item for item, count in items_cnt_order.items()]
    if method_id == 0:
        neg_items = np.random.choice(items_set, size=ratio, replace=True)
    elif method_id == 1:
        p_sel = {item: count ** 0.75 for item, count in items_cnt_order.items()}
        p_value = np.array(list(p_sel.values())) / sum(p_sel.values())
        neg_items = np.random.choice(items_set, size=ratio, replace=True, p=p_value)
    elif method_id == 2:
        p_sel = {item: np.log(count + 1) + 1e-6 for item, count in items_cnt_order.items()}
        p_value = np.array(list(p_sel.values())) / sum(p_sel.values())
        neg_items = np.random.choice(items_set, size=ratio, replace=True, p=p_value)
    elif method_id == 3:
        p_sel = {item: (np.log(k + 2) - np.log(k + 1)) / np.log(len(items_cnt_order) + 1) for item, k in
                 items_cnt_order.items()}
        p_value = np.array(list(p_sel.values())) / sum(p_sel.values())
        neg_items = np.random.choice(items_set, size=ratio, replace=False, p=p_value)
    else:
        raise ValueError("method id should in (0,1,2,3)")
    return neg_items


def generate_seq_feature_match(data,
                               user_col,
                               item_col,
                               time_col,
                               item_attribute_cols=None,
                               sample_method=0,
                               mode=0,
                               neg_ratio=0,
                               min_item=0):
    """
    生成序列特征
    当使用point-wise训练时，独立处理每个样本，交互过的为1，未交互的为0
    使用pair-wise训练时，每个样本包含一个正item和一个负item
    使用list-wise训练时，每个样本包含一个正item和多个负item
    Args:
        data (pd.DataFrame): the raw data.
        user_col (str): the col name of user_id
        item_col (str): the col name of item_id
        time_col (str): the col name of timestamp
        item_attribute_cols (list[str], optional): the other attribute cols of item which you want to generate sequence
                                                   feature. Defaults to `[]`.
        sample_method (int, optional): the negative sample method(详见negative_sample),Defaults to 0.
        mode (int, optional): the training mode, `{0:point-wise, 1:pair-wise, 2:list-wise}`. Defaults to 0.
        neg_ratio (int, optional): negative sample ratio, >= 1. Defaults to 0.
        min_item (int, optional): the min item each user must have. Defaults to 0.
    """
    if item_attribute_cols is None:
        item_attribute_cols = []
    if mode == 2:  # list wise learning
        assert neg_ratio > 0, 'neg_ratio must be greater than 0 when list-wise learning'
    elif mode == 1:  # pair wise learning
        neg_ratio = 1
    print("preprocess data")
    data.sort_values(time_col, inplace=True)  # sort by time from old to new
    train_set, test_set = [], []
    n_cold_user = 0

    items_cnt = Counter(data[item_col].tolist())
    items_cnt_order = OrderedDict(sorted((items_cnt.items()), key=lambda x: x[1], reverse=True))  # item_id:item count
    neg_list = negative_sample(items_cnt_order, ratio=data.shape[0] * neg_ratio, method_id=sample_method)
    neg_idx = 0
    for uid, hist in tqdm.tqdm(data.groupby(user_col), desc='generate sequence features'):
        pos_list = hist[item_col].tolist()
        if len(pos_list) < min_item:  # drop this user when his pos items < min_item
            n_cold_user += 1
            continue

        for i in range(1, len(pos_list)):
            # 历史交互物品列表
            hist_item = pos_list[:i]
            sample = [uid, pos_list[i], hist_item, len(hist_item)]
            if len(item_attribute_cols) > 0:
                for attr_col in item_attribute_cols:  # the history of item attribute features
                    sample.append(hist[attr_col].tolist()[:i])
            if i != len(pos_list) - 1:
                if mode == 0:  # point-wise, the last col is label_col, include label 0 and 1
                    last_col = "label"
                    train_set.append(sample + [1])
                    for _ in range(neg_ratio):
                        sample[1] = neg_list[neg_idx]
                        neg_idx += 1
                        train_set.append(sample + [0])
                elif mode == 1:  # pair-wise, the last col is neg_col, include one negative item
                    last_col = "neg_items"
                    for _ in range(neg_ratio):
                        sample_copy = copy.deepcopy(sample)
                        sample_copy.append(neg_list[neg_idx])
                        neg_idx += 1
                        train_set.append(sample_copy)
                elif mode == 2:  # list-wise, the last col is neg_col, include neg_ratio negative items
                    last_col = "neg_items"
                    sample.append(neg_list[neg_idx: neg_idx + neg_ratio])
                    neg_idx += neg_ratio
                    train_set.append(sample)
                else:
                    raise ValueError("mode should in (0,1,2)")
            else:
                test_set.append(sample + [1])  # Note: if mode=1 or 2, the label col is useless.

    random.shuffle(train_set)
    random.shuffle(test_set)

    print("n_train: %d, n_test: %d" % (len(train_set), len(test_set)))
    print("%d cold start user droped " % (n_cold_user))

    attr_hist_col = ["hist_" + col for col in item_attribute_cols]
    df_train = pd.DataFrame(train_set,
                            columns=[user_col, item_col, "hist_" + item_col, "histlen_" + item_col] + attr_hist_col + [
                                last_col])
    df_test = pd.DataFrame(test_set,
                           columns=[user_col, item_col, "hist_" + item_col, "histlen_" + item_col] + attr_hist_col + [
                               last_col])

    return df_train, df_test


def gen_model_input(df, user_profile, user_col, item_profile, item_col, seq_max_len, padding='pre', truncating='pre'):
    """
    合并序列特征和其他离散，连续特征，同时对序列特征进行pad_sequence操作，最终转换为dict
    Args:
        df (pd.DataFrame): data with history sequence feature
        user_profile (pd.DataFrame): user data
        user_col (str): user column name
        item_profile (pd.DataFrame): item data
        item_col (str): item column name
        seq_max_len (int): sequence length of every data
        padding (str, optional): padding style, {'pre', 'post'}. Defaults to 'pre'.
        truncating (str, optional): truncate style, {'pre', 'post'}. Defaults to 'pre'.

    Returns:
        dict: The converted dict, which can be used directly into the input network
    """
    df = pd.merge(df, user_profile, on=user_col, how='left')  # how=left to keep samples order same as the input
    df = pd.merge(df, item_profile, on=item_col, how='left')
    for col in df.columns.to_list():
        if col.startswith("hist_"):
            df[col] = pad_sequences(df[col], maxlen=seq_max_len, value=0, padding=padding,
                                    truncating=truncating).tolist()
    input_dict = df_to_dict(df)
    return input_dict
