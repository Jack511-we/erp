# -*- coding: utf-8 -*-
"""
广告创意数据模块：负责广告创意基础数据的获取与处理，支持多维度分析
"""
import pandas as pd

def get_creative_data(start_date=None, end_date=None, sku=None, shop=None, campaign=None):
    """
    获取广告创意数据，支持按时间、SKU、店铺、广告系列筛选
    :param start_date: 开始日期
    :param end_date: 结束日期
    :param sku: SKU筛选
    :param shop: 店铺筛选
    :param campaign: 广告系列筛选
    :return: DataFrame
    """
    # 示例数据，可替换为数据库或接口获取
    data = [
        {'creative': 'CR1', 'campaign': 'CAMP1', 'sku': 'A001', 'shop': '店铺1', 'date': '2025-09-01', 'qty': 400},
        {'creative': 'CR2', 'campaign': 'CAMP2', 'sku': 'A002', 'shop': '店铺2', 'date': '2025-09-02', 'qty': 350},
        {'creative': 'CR3', 'campaign': 'CAMP3', 'sku': 'A003', 'shop': '店铺1', 'date': '2025-09-03', 'qty': 280},
        {'creative': 'CR1', 'campaign': 'CAMP1', 'sku': 'A001', 'shop': '店铺3', 'date': '2025-09-01', 'qty': 190},
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
    if campaign:
        df = df[df['campaign'] == campaign]
    return df
