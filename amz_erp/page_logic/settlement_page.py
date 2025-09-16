
# =================================================
# 文件名称：settlement_page.py
# 开发时间：2025-09-15
# 版本号：v1.0
# 作者：Jack
# 功能：结算页面逻辑，负责结算数据展示、导出、参数校验等
# =================================================
from amz_erp.analysis_module.settlement_analysis import summarize_settlement

if __name__ == "__main__":
    summary = summarize_settlement()
    print(f"结算总数: {summary['total_settlements']}")
    print(f"利润总额: {summary['total_profit']}")
    print("结算明细:")
    print(summary['settlement_df'])
    print("已生成 Excel/CSV/PDF 文件，可在 analysis_module/output/ 查看")
