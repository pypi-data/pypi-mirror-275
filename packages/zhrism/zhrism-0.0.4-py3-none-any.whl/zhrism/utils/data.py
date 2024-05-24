import numpy as np


def get_auto_embedding_dim(num_classes):
    """
    根据离散种类数目自动确定embedding向量维度
    emb_dim = [6 * (num_classes)^(1/4)]
    reference: Deep & Cross Network for Ad Click Predictions.(ADKDD'17)
    """
    return np.floor(6 * np.pow(num_classes, 0.26))
