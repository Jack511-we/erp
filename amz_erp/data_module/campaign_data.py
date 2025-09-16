# -*- coding: utf-8 -*-
"""
广告系列数据模块：负责广告系列基础数据的获取与处理，支持多维度分析
"""
import pandas as pd

def get_campaign_data(start_date=None, end_date=None, sku=None, shop=None):
    """
    获取广告系列数据，支持按时间、SKU、店铺筛选
    :param start_date: 开始日期
    :param end_date: 结束日期
    :param sku: SKU筛选
    :param shop: 店铺筛选
    :return: DataFrame
    """
    # 示例数据，可替换为数据库或接口获取
    data = [
        {'campaign': 'CAMP1', 'sku': 'A001', 'shop': '店铺1', 'date': '2025-09-01', 'qty': 300},
        {'campaign': 'CAMP2', 'sku': 'A002', 'shop': '店铺2', 'date': '2025-09-02', 'qty': 250},
        {'campaign': 'CAMP3', 'sku': 'A003', 'shop': '店铺1', 'date': '2025-09-03', 'qty': 180},
        {'campaign': 'CAMP1', 'sku': 'A001', 'shop': '店铺3', 'date': '2025-09-01', 'qty': 90},
    ]
    df = pd.DataFrame(data)
    if start_date:
        df = df[df['date'] >= start_date]
    if end_date:
        df = df[df['date'] <= end_date]
    if sku:
        df = df[df['sku'] == sku]
    if shop:
        df = df[df['shop'] == shop]
    return df
