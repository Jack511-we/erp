# -*- coding: utf-8 -*-
# =================================================
# 文件名称：creative_page.py
# 开发时间：2025-09-15
# 版本号：v1.0
# 作者：Jack
# 功能：创意页面逻辑，负责创意数据展示、导出、参数校验等
# =================================================
"""
广告创意页面逻辑：联动前端筛选与后端分析接口，返回标准化结果
"""
from amz_erp.analysis_module.creative_analysis import analyze_creative

def page_creative_summary(params):
    """
    前端页面调用广告创意分析接口，返回标准化结果
    :param params: dict，包含筛选条件
    :return: dict，分析结果
    """
    result = analyze_creative(params)
    return result
