# =================================================
# 文件名称：sku_page.py
# 开发时间：2025-09-15
# 版本号：v1.0
# 作者：Jack
# 功能：SKU页面逻辑，负责SKU数据展示、导出、参数校验等
# =================================================
# -*- coding: utf-8 -*-
"""
SKU页面逻辑：联动前端筛选与后端分析接口，返回标准化结果
"""
from amz_erp.analysis_module.sku_analysis import analyze_sku

def page_sku_summary(params):
    """
    前端页面调用SKU分析接口，返回标准化结果
    :param params: dict，包含筛选条件
    :return: dict，分析结果
    """
    result = analyze_sku(params)
    return result
