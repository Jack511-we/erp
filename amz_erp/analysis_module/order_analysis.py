from amz_erp.analysis_module.export_utils import export_to_excel, export_to_csv, export_to_pdf
import pandas as pd

def summarize_orders(start_date, end_date, filters=None):
	"""
	汇总订单数据，返回分析结果并导出文件
	:param start_date: 开始日期
	:param end_date: 结束日期
	:param filters: 过滤条件
	:return: dict，包含汇总结果和 DataFrame
	"""
	orders = OrdersModule().get_orders(start_date, end_date, filters)
	df_orders = pd.DataFrame([
		{
			'order_id': o.order_id,
			'sku': o.sku,
			'quantity': o.quantity,
			'price': o.price,
			'order_date': o.order_date
		} for o in orders
	])
	summary = {
		'total_orders': len(orders),
		'total_revenue': float(df_orders['price'].sum()) if not df_orders.empty else 0.0,
		'orders_df': df_orders
	}
	file_list = []
	# 支持导出格式选择
	export_formats = filters.get('export_formats') if filters and isinstance(filters, dict) and 'export_formats' in filters else ['excel', 'csv', 'pdf']
	prefix = f'order_summary_{start_date}_{end_date}'
	if 'excel' in export_formats:
		fname = export_to_excel({'Orders': df_orders}, prefix + '.xlsx')
		file_list.append(fname if fname else prefix + '.xlsx')
	if 'csv' in export_formats:
		fname = export_to_csv(df_orders, prefix + '.csv')
		file_list.append(fname if fname else prefix + '.csv')
	if 'pdf' in export_formats:
		text_lines = [
			f"总订单数: {summary['total_orders']}",
			f"总收入: {summary['total_revenue']}"
		]
		fname = export_to_pdf(text_lines, prefix + '.pdf')
		file_list.append(fname if fname else prefix + '.pdf')
	return summary, file_list

# =================================================
# 文件名称：order_analysis.py
# 日期：2025-09-15 21:30
# 版本号：v1.0
# 作者：Jack
# 功能：订单数据分析
# =================================================

from amz_erp.data_module.orders.orders_module import OrdersModule, Order
from typing import List, Dict

def analyze_orders(start_date: str, end_date: str, filters: Dict = None) -> List[Dict]:
	"""
	订单分析接口，统一输入输出
	:param start_date: 开始日期
	:param end_date: 结束日期
	:param filters: 过滤条件
	:return: 订单分析结果列表，每项为字典
	"""
	orders = OrdersModule().get_orders(start_date, end_date, filters)
	# 示例：输出订单基础字段
	return [
		{
			'order_id': o.order_id,
			'sku': o.sku,
			'quantity': o.quantity,
			'price': o.price,
			'order_date': o.order_date
		} for o in orders
	]
