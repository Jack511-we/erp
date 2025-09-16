# =================================================
# 文件名称：test_analysis.py
# 日期：2025-09-15 21:40
# 版本号：v1.0
# 作者：Jack
# 功能：验证分析模块接口及字段输出
# =================================================

import unittest
from amz_erp.analysis_module.order_analysis import analyze_orders
from amz_erp.analysis_module.inventory_analysis import analyze_inventory
from amz_erp.analysis_module.ads_analysis import analyze_ads
from amz_erp.analysis_module.settlement_analysis import analyze_settlement
from amz_erp.analysis_module.summary_analysis import analyze_summary

class TestAnalysisModule(unittest.TestCase):
    def test_order_analysis(self):
        result = analyze_orders('2025-09-01', '2025-09-10')
        self.assertIsInstance(result, list)
        if result:
            self.assertIn('order_id', result[0])
            self.assertIn('sku', result[0])
            self.assertIn('quantity', result[0])
            self.assertIn('price', result[0])
            self.assertIn('order_date', result[0])

    def test_inventory_analysis(self):
        result = analyze_inventory()
        self.assertIsInstance(result, list)
        if result:
            self.assertIn('sku', result[0])
            self.assertIn('quantity', result[0])
            self.assertIn('warehouse', result[0])

    def test_ads_analysis(self):
        result = analyze_ads()
        self.assertIsInstance(result, list)
        if result:
            self.assertIn('ad_id', result[0])
            self.assertIn('sku', result[0])
            self.assertIn('spend', result[0])
            self.assertIn('clicks', result[0])

    def test_settlement_analysis(self):
        result = analyze_settlement()
        self.assertIsInstance(result, list)
        if result:
            self.assertIn('settlement_id', result[0])
            self.assertIn('total', result[0])
            self.assertIn('profit', result[0])
            self.assertIn('date', result[0])

    def test_summary_analysis(self):
        result = analyze_summary()
        self.assertIsInstance(result, dict)
        self.assertIn('orders_count', result)
        self.assertIn('inventory_count', result)
        self.assertIn('ads_count', result)
        self.assertIn('settlement_count', result)

if __name__ == '__main__':
    unittest.main()

# =================================================
# 核心逻辑锁定，只能调用接口，不允许修改
# =================================================
