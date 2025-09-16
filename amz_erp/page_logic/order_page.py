# =================================================
# 文件名称：order_page.py
# 开发时间：2025-09-15
# 版本号：v1.0
# 作者：Jack
# 功能：订单页面逻辑，负责订单数据展示、导出、参数校验等
# =================================================
from amz_erp.analysis_module.order_analysis import summarize_orders

# =================================================
# 文件名称：order_page.py
# 日期：2025-09-15
# 版本号：v1.0
# 作者：Jack
# 功能：页面逻辑调用分析模块，展示数据并导出文件
# =================================================


from amz_erp.analysis_module.order_analysis import summarize_orders


def page_order_summary(start_date, end_date, export_formats=None):
    """
    页面逻辑：订单汇总，支持导出格式选择，返回文件名列表
    :param start_date: 开始日期
    :param end_date: 结束日期
    :param export_formats: ['excel', 'csv', 'pdf']，可选导出格式
    :return: dict，包含汇总结果和文件名列表
    """
    if export_formats is None:
        export_formats = ['excel', 'csv', 'pdf']
    summary, file_list = summarize_orders(start_date, end_date, export_formats)
    print(f"总订单数: {summary['total_orders']}")
    print(f"总收入: {summary['total_revenue']}")
    print("订单明细:")
    print(summary['orders_df'])
    print("已生成文件:")
    for fname in file_list:
        print(fname)
    return {'summary': summary, 'files': file_list}

# 示例调用
if __name__ == "__main__":
    start_date = "2025-09-01"
    end_date = "2025-09-15"
    result = page_order_summary(start_date, end_date, export_formats=['excel', 'pdf'])
