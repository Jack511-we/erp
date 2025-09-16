from amz_erp.analysis_module.export_utils import export_to_excel, export_to_csv, export_to_pdf
import pandas as pd

def summarize_ads(filters=None):
	"""
	汇总广告数据，返回分析结果并导出文件
	:param filters: 过滤条件
	:return: dict，包含汇总结果和 DataFrame
	"""
	ads = AdsModule().get_ads(filters)
	df_ads = pd.DataFrame([
		{
			'ad_id': a.ad_id,
			'sku': a.sku,
			'spend': a.spend,
			'clicks': a.clicks
		} for a in ads
	])
	summary = {
		'total_ads': len(ads),
		'total_spend': float(df_ads['spend'].sum()) if not df_ads.empty else 0.0,
		'ads_df': df_ads
	}
	file_list = []
	export_formats = filters.get('export_formats') if filters and isinstance(filters, dict) and 'export_formats' in filters else ['excel', 'csv', 'pdf']
	prefix = 'ads_summary'
	if 'excel' in export_formats:
		fname = export_to_excel({'Ads': df_ads}, prefix + '.xlsx')
		file_list.append(fname if fname else prefix + '.xlsx')
	if 'csv' in export_formats:
		fname = export_to_csv(df_ads, prefix + '.csv')
		file_list.append(fname if fname else prefix + '.csv')
	if 'pdf' in export_formats:
		text_lines = [f"广告总数: {summary['total_ads']}", f"广告总花费: {summary['total_spend']}"]
		fname = export_to_pdf(text_lines, prefix + '.pdf')
		file_list.append(fname if fname else prefix + '.pdf')
	return summary, file_list

# =================================================
# 文件名称：ads_analysis.py
# 日期：2025-09-15 21:30
# 版本号：v1.0
# 作者：Jack
# 功能：广告数据分析
# =================================================

from amz_erp.data_module.ads.ads_module import AdsModule, Ad
from typing import List, Dict

def analyze_ads(filters: Dict = None) -> List[Dict]:
	"""
	广告分析接口，统一输入输出
	:param filters: 过滤条件
	:return: 广告分析结果列表，每项为字典
	"""
	ads = AdsModule().get_ads(filters)
	return [
		{
			'ad_id': a.ad_id,
			'sku': a.sku,
			'spend': a.spend,
			'clicks': a.clicks
		} for a in ads
	]
