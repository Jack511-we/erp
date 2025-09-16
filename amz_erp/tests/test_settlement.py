# =================================================
# 文件名称：test_settlement.py
# 日期：2025-09-15 21:10
# 版本号：v1.0
# 作者：Jack
# 功能：验证 SettlementModule 接口及日志、缓存、异常处理
# =================================================

import unittest
from amz_erp.data_module.settlement.settlement_module import SettlementModule, Settlement

class TestSettlementModule(unittest.TestCase):
    def setUp(self):
        self.module = SettlementModule()

    def test_get_settlement(self):
        """
        测试获取结算数据，返回标准 List[Settlement] 对象
        """
        settlements = self.module.get_settlement({'date': '2025-09-01'})
        self.assertIsInstance(settlements, list)
        self.assertTrue(all(isinstance(s, Settlement) for s in settlements))
        self.assertGreaterEqual(len(settlements), 1)

    def test_cache(self):
        """
        测试缓存机制是否生效
        """
        s1 = self.module.get_settlement({'date': '2025-09-01'})
        s2 = self.module.get_settlement({'date': '2025-09-01'})
        def s_to_dict(s):
            return {'settlement_id': s.settlement_id, 'total': s.total, 'profit': s.profit, 'date': s.date}
        list1 = [s_to_dict(x) for x in s1]
        list2 = [s_to_dict(x) for x in s2]
        self.assertEqual(list1, list2)

    def test_exception(self):
        """
        测试异常处理，传入非法参数
        """
        settlements = self.module.get_settlement(None)
        self.assertIsInstance(settlements, list)

if __name__ == '__main__':
    unittest.main()

# =================================================
# 核心逻辑锁定，只能调用接口，不允许修改
# =================================================
