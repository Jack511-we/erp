# =================================================
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
# 文件名称：unified_page_export.py
# 日期：2025-09-15
# 版本号：v1.0
# 作者：Jack
# 功能：统一页面逻辑批量导出，支持模块选择、时间范围、导出格式，返回文件名列表
# =================================================

from amz_erp.page_logic.order_page import page_order_summary
from amz_erp.page_logic.inventory_page import summarize_inventory
from amz_erp.page_logic.ads_page import summarize_ads
from amz_erp.page_logic.settlement_page import summarize_settlement
from amz_erp.page_logic.summary_page import summarize_all
from amz_erp.export_utils import apply_report_style, embed_charts_to_pdf, embed_charts_to_excel

# 扩展：统一风格美化与图表嵌入

def unified_export(modules, start_date, end_date, export_formats=None, chart_images=None):
    """
    批量调用各分析模块，返回所有文件名列表，并统一报表风格，嵌入图表图片
    :param modules: ['order', 'inventory', ...]
    :param start_date: 开始日期
    :param end_date: 结束日期
    :param export_formats: ['excel', 'pdf', 'csv']
    :param chart_images: dict，key为模块名，value为图表图片路径列表
    :return: dict，key为模块名，value为文件名列表
    """
    result = {}
    if export_formats is None:
        export_formats = ['excel', 'pdf', 'csv']
    if chart_images is None:
        chart_images = {}
    if 'order' in modules:
        summary, file_list = page_order_summary(start_date, end_date, export_formats)
        # 统一风格美化
        file_list = [apply_report_style(f) for f in file_list]
        # 图表嵌入
        if 'pdf' in export_formats and chart_images.get('order'):
            embed_charts_to_pdf(file_list, chart_images['order'])
        if 'excel' in export_formats and chart_images.get('order'):
            embed_charts_to_excel(file_list, chart_images['order'])
        result['order'] = file_list
    if 'inventory' in modules:
        summary, file_list = summarize_inventory(export_formats)
        file_list = [apply_report_style(f) for f in file_list]
        if 'pdf' in export_formats and chart_images.get('inventory'):
            embed_charts_to_pdf(file_list, chart_images['inventory'])
        if 'excel' in export_formats and chart_images.get('inventory'):
            embed_charts_to_excel(file_list, chart_images['inventory'])
        result['inventory'] = file_list
    if 'ads' in modules:
        summary, file_list = summarize_ads(export_formats)
        file_list = [apply_report_style(f) for f in file_list]
        if 'pdf' in export_formats and chart_images.get('ads'):
            embed_charts_to_pdf(file_list, chart_images['ads'])
        if 'excel' in export_formats and chart_images.get('ads'):
            embed_charts_to_excel(file_list, chart_images['ads'])
        result['ads'] = file_list
    if 'settlement' in modules:
        summary, file_list = summarize_settlement(export_formats)
        file_list = [apply_report_style(f) for f in file_list]
        if 'pdf' in export_formats and chart_images.get('settlement'):
            embed_charts_to_pdf(file_list, chart_images['settlement'])
        if 'excel' in export_formats and chart_images.get('settlement'):
            embed_charts_to_excel(file_list, chart_images['settlement'])
        result['settlement'] = file_list
    if 'summary' in modules:
        summary, file_list = summarize_all(export_formats)
        file_list = [apply_report_style(f) for f in file_list]
        if 'pdf' in export_formats and chart_images.get('summary'):
            embed_charts_to_pdf(file_list, chart_images['summary'])
        if 'excel' in export_formats and chart_images.get('summary'):
            embed_charts_to_excel(file_list, chart_images['summary'])
        result['summary'] = file_list
    return result

# 接口安全与参数校验（示例）
def validate_export_params(modules, start_date, end_date, export_formats):
    # 校验模块合法性
    valid_modules = {'order','inventory','ads','settlement','summary'}
    if not set(modules).issubset(valid_modules):
        raise ValueError('模块参数不合法')
    # 校验日期格式
    import re
    date_pattern = r'^\d{4}-\d{2}-\d{2}$'
    if not re.match(date_pattern, start_date) or not re.match(date_pattern, end_date):
        raise ValueError('日期格式不正确')
    # 校验导出格式
    valid_formats = {'excel','pdf','csv'}
    if not set(export_formats).issubset(valid_formats):
        raise ValueError('导出格式参数不合法')
    return True

# 在 unified_export 调用前加参数校验
# 示例调用
if __name__ == "__main__":
    modules = ['order', 'inventory', 'ads', 'settlement', 'summary']
    start_date = "2025-09-01"
    end_date = "2025-09-15"
    export_formats = ['excel', 'pdf', 'csv']
    # 参数校验
    try:
        validate_export_params(modules, start_date, end_date, export_formats)
        files_dict = unified_export(modules, start_date, end_date, export_formats)
        print("批量导出结果：")
        for mod, files in files_dict.items():
            print(f"模块：{mod}")
            for fname in files:
                print(f"  {fname}")
    except Exception as e:
        print(f"参数校验或导出过程中发生错误：{e}")
