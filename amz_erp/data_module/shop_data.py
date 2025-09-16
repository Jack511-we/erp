# -*- coding: utf-8 -*-
"""
店铺数据模块：负责店铺基础数据的获取与处理，支持多维度分析
"""
import pandas as pd

def get_shop_data(start_date=None, end_date=None, sku=None, campaign=None):
    """
    获取店铺数据，支持按时间、SKU、广告系列筛选
    :param start_date: 开始日期
    :param end_date: 结束日期
    :param sku: SKU筛选
    :param campaign: 广告系列筛选
    :return: DataFrame
    """
    # 示例数据，可替换为数据库或接口获取
    data = [
        {'shop': '店铺1', 'sku': 'A001', 'campaign': 'CAMP1', 'date': '2025-09-01', 'qty': 200},
        {'shop': '店铺2', 'sku': 'A002', 'campaign': 'CAMP2', 'date': '2025-09-02', 'qty': 150},
        {'shop': '店铺1', 'sku': 'A003', 'campaign': 'CAMP3', 'date': '2025-09-03', 'qty': 180},
        {'shop': '店铺3', 'sku': 'A001', 'campaign': 'CAMP1', 'date': '2025-09-01', 'qty': 90},
    ]
    df = pd.DataFrame(data)
    if start_date:
        df = df[df['date'] >= start_date]
    if end_date:
        df = df[df['date'] <= end_date]
    if sku:
        df = df[df['sku'] == sku]
    if campaign:
        df = df[df['campaign'] == campaign]
    return df
