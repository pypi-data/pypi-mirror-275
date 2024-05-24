import numpy as np
from collections import defaultdict


def topk_metrics(y_true, y_pred, topKs=None):
    """
    choice topk metrics and compute it
    the metrics contains 'ndcg', 'mrr', 'recall', 'precision' and 'hit'

    Args:
        y_true (dict): {userid, item_ids}, the key is user id and the value is the list that contains the items the user interacted
        y_pred (dict): {userid, item_ids}, the key is user id and the value is the list that contains the items recommended
        topKs (list or tuple): if you want to get top5 and top10, topKs=(5, 10)

    Return:
        results (dict): {metric_name: metric_values}, it contains five metrics, 'ndcg', 'recall', 'mrr', 'hit', 'precision'

    """
    if topKs is None:
        topKs = [5]
    assert len(y_true) == len(y_pred)

    if not isinstance(topKs, (tuple, list)):
        raise ValueError('topKs wrong, it should be tuple or list')

    pred_array = []
    true_array = []
    for u in y_true.keys():
        pred_array.append(y_pred[u])
        true_array.append(y_true[u])
    ndcg_result = []
    mrr_result = []
    hit_result = []
    precision_result = []
    recall_result = []
    for idx in range(len(topKs)):
        ndcgs = 0
        mrrs = 0
        hits = 0
        precisions = 0
        recalls = 0
        gts = 0
        for i in range(len(true_array)):
            if len(true_array[i]) != 0:
                mrr_tmp = 0
                mrr_flag = True
                hit_tmp = 0
                dcg_tmp = 0
                idcg_tmp = 0
                for j in range(topKs[idx]):
                    if pred_array[i][j] in true_array[i]:
                        hit_tmp += 1.
                        if mrr_flag:
                            mrr_flag = False
                            mrr_tmp = 1. / (1 + j)
                        dcg_tmp += 1. / (np.log2(j + 2))
                    if j < len(true_array[i]):
                        idcg_tmp += 1. / (np.log2(j + 2))
                gts += len(true_array[i])
                hits += hit_tmp
                mrrs += mrr_tmp
                recalls += hit_tmp / len(true_array[i])
                precisions += hit_tmp / topKs[idx]
                if idcg_tmp != 0:
                    ndcgs += dcg_tmp / idcg_tmp
        hit_result.append(round(hits / gts, 4))
        mrr_result.append(round(mrrs / len(pred_array), 4))
        recall_result.append(round(recalls / len(pred_array), 4))
        precision_result.append(round(precisions / len(pred_array), 4))
        ndcg_result.append(round(ndcgs / len(pred_array), 4))

    results = defaultdict(list)
    for idx in range(len(topKs)):
        output = f'NDCG@{topKs[idx]}: {ndcg_result[idx]}'
        results['NDCG'].append(output)

        output = f'MRR@{topKs[idx]}: {mrr_result[idx]}'
        results['MRR'].append(output)

        output = f'Recall@{topKs[idx]}: {recall_result[idx]}'
        results['Recall'].append(output)

        output = f'Hit@{topKs[idx]}: {hit_result[idx]}'
        results['Hit'].append(output)

        output = f'Precision@{topKs[idx]}: {precision_result[idx]}'
        results['Precision'].append(output)
    return results
