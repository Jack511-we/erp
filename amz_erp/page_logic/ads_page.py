# =================================================
# 文件名称：ads_page.py
# 日期：2025-09-15
# 版本号：v1.0
# 作者：Jack
# 功能：页面逻辑调用广告分析模块，展示数据并导出文件
# =================================================

# =================================================
# 文件名称：ads_page.py
# 开发时间：2025-09-15
# 版本号：v1.0
# 作者：Jack
# 功能：广告页面逻辑，负责广告数据展示、导出、参数校验等
# =================================================
# 
from amz_erp.analysis_module.ads_analysis import summarize_ads

if __name__ == "__main__":
    summary = summarize_ads()
    print(f"广告总数: {summary['total_ads']}")
    print(f"广告总花费: {summary['total_spend']}")
    print("广告明细:")
    print(summary['ads_df'])
    print("已生成 Excel/CSV/PDF 文件，可在 analysis_module/output/ 查看")
