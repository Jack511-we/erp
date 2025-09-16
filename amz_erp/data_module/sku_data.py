# -*- coding: utf-8 -*-
"""
SKU数据模块：负责SKU基础数据的获取与处理，支持多维度分析
"""
import pandas as pd

def get_sku_data(start_date=None, end_date=None, shop=None, campaign=None):
    """
    获取SKU数据，支持按时间、店铺、广告系列筛选
    :param start_date: 开始日期
    :param end_date: 结束日期
    :param shop: 店铺筛选
    :param campaign: 广告系列筛选
    :return: DataFrame
    """
    # 示例数据，可替换为数据库或接口获取
    data = [
        {'sku': 'A001', 'shop': '店铺1', 'campaign': 'CAMP1', 'date': '2025-09-01', 'qty': 100},
        {'sku': 'A002', 'shop': '店铺2', 'campaign': 'CAMP2', 'date': '2025-09-02', 'qty': 80},
        {'sku': 'A001', 'shop': '店铺1', 'campaign': 'CAMP1', 'date': '2025-09-03', 'qty': 120},
        {'sku': 'A003', 'shop': '店铺3', 'campaign': 'CAMP3', 'date': '2025-09-01', 'qty': 60},
    ]
    df = pd.DataFrame(data)
    if start_date:
        df = df[df['date'] >= start_date]
    if end_date:
        df = df[df['date'] <= end_date]
    if shop:
        df = df[df['shop'] == shop]
    if campaign:
        df = df[df['campaign'] == campaign]
    return df
