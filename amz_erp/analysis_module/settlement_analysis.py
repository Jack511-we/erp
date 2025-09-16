from amz_erp.analysis_module.export_utils import export_to_excel, export_to_csv, export_to_pdf
import pandas as pd

def summarize_settlement(filters=None):
	"""
	汇总结算数据，返回分析结果并导出文件
	:param filters: 过滤条件
	:return: dict，包含汇总结果和 DataFrame
	"""
	settlements = SettlementModule().get_settlement(filters)
	df_settlement = pd.DataFrame([
		{
			'settlement_id': s.settlement_id,
			'total': s.total,
			'profit': s.profit,
			'date': s.date
		} for s in settlements
	])
	summary = {
		'total_settlements': len(settlements),
		'total_profit': float(df_settlement['profit'].sum()) if not df_settlement.empty else 0.0,
		'settlement_df': df_settlement
	}
	file_list = []
	export_formats = filters.get('export_formats') if filters and isinstance(filters, dict) and 'export_formats' in filters else ['excel', 'csv', 'pdf']
	prefix = 'settlement_summary'
	if 'excel' in export_formats:
		fname = export_to_excel({'Settlement': df_settlement}, prefix + '.xlsx')
		file_list.append(fname if fname else prefix + '.xlsx')
	if 'csv' in export_formats:
		fname = export_to_csv(df_settlement, prefix + '.csv')
		file_list.append(fname if fname else prefix + '.csv')
	if 'pdf' in export_formats:
		text_lines = [f"结算总数: {summary['total_settlements']}", f"利润总额: {summary['total_profit']}"]
		fname = export_to_pdf(text_lines, prefix + '.pdf')
		file_list.append(fname if fname else prefix + '.pdf')
	return summary, file_list

# =================================================
# 文件名称：settlement_analysis.py
# 日期：2025-09-15 21:30
# 版本号：v1.0
# 作者：Jack
# 功能：结算/利润数据分析
# =================================================

from amz_erp.data_module.settlement.settlement_module import SettlementModule, Settlement
from typing import List, Dict

def analyze_settlement(filters: Dict = None) -> List[Dict]:
	"""
	结算分析接口，统一输入输出
	:param filters: 过滤条件
	:return: 结算分析结果列表，每项为字典
	"""
	settlements = SettlementModule().get_settlement(filters)
	return [
		{
			'settlement_id': s.settlement_id,
			'total': s.total,
			'profit': s.profit,
			'date': s.date
		} for s in settlements
	]
