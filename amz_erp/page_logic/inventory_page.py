
# =================================================
# 文件名称：inventory_page.py
# 开发时间：2025-09-15
# 版本号：v1.0
# 作者：Jack
# 功能：库存页面逻辑，负责库存数据展示、导出、参数校验等
# =================================================
from amz_erp.analysis_module.inventory_analysis import summarize_inventory

if __name__ == "__main__":
    summary = summarize_inventory()
    print(f"SKU总数: {summary['total_skus']}")
    print(f"库存总量: {summary['total_quantity']}")
    print("库存明细:")
    print(summary['inventory_df'])
    print("已生成 Excel/CSV/PDF 文件，可在 analysis_module/output/ 查看")

if __name__ == "__main__":
    summary = summarize_inventory()
    print(f"SKU总数: {summary['total_skus']}")
    print(f"库存总量: {summary['total_quantity']}")
    print("库存明细:")
    print(summary['inventory_df'])
    print("已生成 Excel/CSV/PDF 文件，可在 analysis_module/output/ 查看")
