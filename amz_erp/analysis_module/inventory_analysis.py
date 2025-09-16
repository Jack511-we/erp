from amz_erp.analysis_module.export_utils import export_to_excel, export_to_csv, export_to_pdf
import pandas as pd

def summarize_inventory(filters=None):
	"""
	汇总库存数据，返回分析结果并导出文件
	:param filters: 过滤条件
	:return: dict，包含汇总结果和 DataFrame
	"""
	inventory = InventoryModule().get_inventory(filters)
	df_inventory = pd.DataFrame([
		{
			'sku': i.sku,
			'quantity': i.quantity,
			'warehouse': i.warehouse
		} for i in inventory
	])
	summary = {
		'total_skus': len(inventory),
		'total_quantity': int(df_inventory['quantity'].sum()) if not df_inventory.empty else 0,
		'inventory_df': df_inventory
	}
	file_list = []
	export_formats = filters.get('export_formats') if filters and isinstance(filters, dict) and 'export_formats' in filters else ['excel', 'csv', 'pdf']
	prefix = 'inventory_summary'
	if 'excel' in export_formats:
		fname = export_to_excel({'Inventory': df_inventory}, prefix + '.xlsx')
		file_list.append(fname if fname else prefix + '.xlsx')
	if 'csv' in export_formats:
		fname = export_to_csv(df_inventory, prefix + '.csv')
		file_list.append(fname if fname else prefix + '.csv')
	if 'pdf' in export_formats:
		text_lines = [f"SKU总数: {summary['total_skus']}", f"库存总量: {summary['total_quantity']}"]
		fname = export_to_pdf(text_lines, prefix + '.pdf')
		file_list.append(fname if fname else prefix + '.pdf')
	return summary, file_list

# =================================================
# 文件名称：inventory_analysis.py
# 日期：2025-09-15 21:30
# 版本号：v1.0
# 作者：Jack
# 功能：库存数据分析
# =================================================

from amz_erp.data_module.inventory.inventory_module import InventoryModule, Inventory
from typing import List, Dict

def analyze_inventory(filters: Dict = None) -> List[Dict]:
	"""
	库存分析接口，统一输入输出
	:param filters: 过滤条件
	:return: 库存分析结果列表，每项为字典
	"""
	inventory = InventoryModule().get_inventory(filters)
	return [
		{
			'sku': i.sku,
			'quantity': i.quantity,
			'warehouse': i.warehouse
		} for i in inventory
	]
