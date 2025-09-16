# =================================================
# 文件名称：summary_page.py
# 日期：2025-09-15
# 版本号：v1.0
# 作者：Jack
# 功能：页面逻辑调用综合汇总分析模块，展示数据并导出文件
# =================================================
from amz_erp.analysis_module.summary_analysis import summarize_all
from amz_erp.analysis_module.summary_analysis import summarize_all

if __name__ == "__main__":
    summary = summarize_all()
    print("综合汇总结果:")
    print(summary)
    print("已生成 Excel/CSV/PDF 文件，可在 analysis_module/output/ 查看")
