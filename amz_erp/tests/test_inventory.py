# =================================================
# 文件名称：test_inventory.py
# 日期：2025-09-15 21:10
# 版本号：v1.0
# 作者：Jack
# 功能：验证 InventoryModule 接口及日志、缓存、异常处理
# =================================================

import unittest
from amz_erp.data_module.inventory.inventory_module import InventoryModule, Inventory

class TestInventoryModule(unittest.TestCase):
    def setUp(self):
        self.module = InventoryModule()

    def test_get_inventory(self):
        """
        测试获取库存数据，返回标准 List[Inventory] 对象
        """
        inventory = self.module.get_inventory({'warehouse': 'WH1'})
        self.assertIsInstance(inventory, list)
        self.assertTrue(all(isinstance(i, Inventory) for i in inventory))
        self.assertGreaterEqual(len(inventory), 1)

    def test_cache(self):
        """
        测试缓存机制是否生效
        """
        inv1 = self.module.get_inventory({'warehouse': 'WH1'})
        inv2 = self.module.get_inventory({'warehouse': 'WH1'})
        def inv_to_dict(i):
            return {'sku': i.sku, 'quantity': i.quantity, 'warehouse': i.warehouse}
        list1 = [inv_to_dict(i) for i in inv1]
        list2 = [inv_to_dict(i) for i in inv2]
        self.assertEqual(list1, list2)

    def test_exception(self):
        """
        测试异常处理，传入非法参数
        """
        inventory = self.module.get_inventory(None)
        self.assertIsInstance(inventory, list)

if __name__ == '__main__':
    unittest.main()

# =================================================
# 核心逻辑锁定，只能调用接口，不允许修改
# =================================================
