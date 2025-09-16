# -*- coding: utf-8 -*-
"""
广告创意分析模块：对广告创意数据进行多维度统计与分析，支持异常值高亮、同比/环比
"""
import pandas as pd
from amz_erp.data_module.creative_data import get_creative_data
from amz_erp.utils import cache_result, catch_exception

@catch_exception
@cache_result
def analyze_creative(params=None):
    """
    广告创意多维度分析接口
    :param params: dict，包含筛选条件
    :return: dict，分析结果
    """
    if params is None:
        params = {}
    df = get_creative_data(
        start_date=params.get('start_date'),
        end_date=params.get('end_date'),
        sku=params.get('sku'),
        shop=params.get('shop'),
        campaign=params.get('campaign')
    )
    # 多维度统计
    result = {}
    for dim in ['creative','campaign','sku','shop','date']:
        if dim in df.columns:
            group = df.groupby(dim).size().sort_values(ascending=False)
            stat = pd.DataFrame({dim: group.index, '数量': group.values})
            # 异常值高亮
            mean = stat['数量'].mean()
            std = stat['数量'].std()
            stat['异常'] = stat['数量'].apply(lambda x: abs(x-mean)>3*std)
            # 同比/环比（以时间为例）
            if dim=='date':
                stat['同比'] = stat['数量'].pct_change(periods=365).round(2)
                stat['环比'] = stat['数量'].pct_change().round(2)
            result[dim] = stat
    return result
