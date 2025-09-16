import numpy as np
import threading
from amz_erp.utils import cache_result, logger, catch_exception

# 多维度分析增强，支持SKU/店铺/广告系列/时间区间
@cache_result
def multidim_summary(df, dims=['sku','shop','campaign','date'], highlight_outlier=True, calc_ratio=True):
	"""
	多维度汇总分析，支持异常值高亮、同比/环比自动计算
	:param df: DataFrame，包含相关字段
	:param dims: 维度列表
	:param highlight_outlier: 是否高亮异常值
	:param calc_ratio: 是否自动计算同比/环比
	:return: dict，包含多维度统计结果
	"""
	result = {}
	for dim in dims:
		if dim in df.columns:
			group = df.groupby(dim).size().sort_values(ascending=False)
			stat = pd.DataFrame({dim: group.index, '数量': group.values})
			# 异常值高亮（如3倍标准差外）
			if highlight_outlier:
				mean = stat['数量'].mean()
				std = stat['数量'].std()
				stat['异常'] = stat['数量'].apply(lambda x: abs(x-mean)>3*std)
			# 同比/环比（以时间为例）
			if calc_ratio and dim=='date':
				stat['同比'] = stat['数量'].pct_change(periods=365).round(2)
				stat['环比'] = stat['数量'].pct_change().round(2)
			result[dim] = stat
	return result

# 性能优化：异步处理与分页加载（示例）
def async_summary(df, dims, callback):
	def worker():
		res = multidim_summary(df, dims)
		callback(res)
	t = threading.Thread(target=worker)
	t.start()
	return t
from amz_erp.analysis_module.export_utils import export_to_excel, export_to_csv, export_to_pdf
import pandas as pd

@catch_exception
def summarize_all(export_formats=None):
	"""
	综合汇总分析，导出所有模块汇总结果，并自动生成多维度图表
	:return: dict，包含各模块汇总结果
	"""
	from amz_erp.analysis_module.order_analysis import summarize_orders
	from amz_erp.analysis_module.inventory_analysis import summarize_inventory
	from amz_erp.analysis_module.ads_analysis import summarize_ads
	from amz_erp.analysis_module.settlement_analysis import summarize_settlement

	if export_formats is None:
		export_formats = ['excel', 'csv', 'pdf']
	order, order_files = summarize_orders('2025-09-01', '2025-09-15', {'export_formats': export_formats})
	inventory, inventory_files = summarize_inventory({'export_formats': export_formats})
	ads, ads_files = summarize_ads({'export_formats': export_formats})
	settlement, settlement_files = summarize_settlement({'export_formats': export_formats})

	summary = {
		'orders': order,
		'inventory': inventory,
		'ads': ads,
		'settlement': settlement
	}
	file_list = []

	# 多维度图表数据准备
	chart_data_list = []
	# SKU分布（柱状图）
	sku_counts = order['orders_df'].groupby('sku').size()
	chart_data_list.append({
		'x': sku_counts.index.tolist(),
		'y': sku_counts.values.tolist(),
		'title': 'SKU订单分布',
		'xlabel': 'SKU',
		'ylabel': '订单数',
		'type': 'bar',
		'figsize': (6,3)
	})
	# 店铺分布（饼图，假设有店铺字段）
	if 'shop' in order['orders_df'].columns:
		shop_counts = order['orders_df'].groupby('shop').size()
		chart_data_list.append({
			'x': shop_counts.index.tolist(),
			'y': shop_counts.values.tolist(),
			'title': '店铺订单分布',
			'type': 'pie',
			'figsize': (5,5)
		})
	# 广告系列分布（柱状图，假设有campaign字段）
	if 'campaign' in ads['ads_df'].columns:
		campaign_counts = ads['ads_df'].groupby('campaign').size()
		chart_data_list.append({
			'x': campaign_counts.index.tolist(),
			'y': campaign_counts.values.tolist(),
			'title': '广告系列分布',
			'xlabel': '广告系列',
			'ylabel': '广告数',
			'type': 'bar',
			'figsize': (6,3)
		})

	# 汇总导出 Excel（多Sheet，含维度统计）
	excel_data = {
		'Orders': order['orders_df'],
		'Inventory': inventory['inventory_df'],
		'Ads': ads['ads_df'],
		'Settlement': settlement['settlement_df'],
		'SKU分布': pd.DataFrame({'SKU': sku_counts.index, '订单数': sku_counts.values})
	}
	if 'shop' in order['orders_df'].columns:
		shop_df = pd.DataFrame({'店铺': shop_counts.index, '订单数': shop_counts.values})
		excel_data['店铺分布'] = shop_df
	if 'campaign' in ads['ads_df'].columns:
		campaign_df = pd.DataFrame({'广告系列': campaign_counts.index, '广告数': campaign_counts.values})
		excel_data['广告系列分布'] = campaign_df
	fname_excel = export_to_excel(excel_data, 'all_summary.xlsx')
	file_list.append(fname_excel if fname_excel else 'all_summary.xlsx')

	# 汇总导出 CSV（只导出订单）
	fname_csv = export_to_csv(order['orders_df'], 'all_orders_summary.csv')
	file_list.append(fname_csv if fname_csv else 'all_orders_summary.csv')

	# 汇总导出 PDF（含多图表、封面、目录）
	text_lines = [
		f"总订单数: {order['total_orders']}",
		f"SKU总数: {inventory['total_skus']}",
		f"广告总数: {ads['total_ads']}",
		f"结算总数: {settlement['total_settlements']}"
	]
	cover_info = {'title': 'ERP综合汇总报表', 'date': '2025-09-15', 'company': '演示公司'}
	toc = ['汇总统计', 'SKU订单分布']
	if 'shop' in order['orders_df'].columns:
		toc.append('店铺订单分布')
	if 'campaign' in ads['ads_df'].columns:
		toc.append('广告系列分布')
	fname_pdf = export_to_pdf(text_lines, 'all_summary.pdf', chart_data_list=chart_data_list, cover_info=cover_info, toc=toc)
	file_list.append(fname_pdf if fname_pdf else 'all_summary.pdf')

	# 合并各模块文件
	file_list.extend(order_files)
	file_list.extend(inventory_files)
	file_list.extend(ads_files)
	file_list.extend(settlement_files)
	logger.info(f"综合汇总分析执行，导出格式: {export_formats}")
	return summary, file_list

# =================================================
# 文件名称：summary_analysis.py
# 日期：2025-09-15 21:30
# 版本号：v1.0
# 作者：Jack
# 功能：综合汇总分析
# =================================================

from amz_erp.analysis_module.order_analysis import analyze_orders
from amz_erp.analysis_module.inventory_analysis import analyze_inventory
from amz_erp.analysis_module.ads_analysis import analyze_ads
from amz_erp.analysis_module.settlement_analysis import analyze_settlement
from typing import Dict

@catch_exception
def analyze_summary(params: Dict = None) -> Dict:
	"""
	综合汇总分析接口，统一输入输出
	:param params: 汇总参数
	:return: 汇总分析结果字典
	"""
	# 示例：汇总各模块数据条数
	result = {
		'orders_count': len(analyze_orders('2025-09-01', '2025-09-10')),
		'inventory_count': len(analyze_inventory()),
		'ads_count': len(analyze_ads()),
		'settlement_count': len(analyze_settlement())
	}
	return result
