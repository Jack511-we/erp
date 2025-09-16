# =================================================
# 文件名称：test_orders.py
# 日期：2025-09-15 20:30
# 版本号：v1.0
# 作者：Jack
# 功能：验证 OrdersModule 接口及日志、缓存、异常处理
# =================================================

import unittest
from amz_erp.data_module.orders.orders_module import OrdersModule, Order

class TestOrdersModule(unittest.TestCase):
    def setUp(self):
        self.module = OrdersModule()

    def test_get_orders(self):
        """
        测试获取订单数据，返回标准 List[Order] 对象
        """
        orders = self.module.get_orders('2025-09-01', '2025-09-10', {'status': 'Shipped'})
        self.assertIsInstance(orders, list)
        self.assertTrue(all(isinstance(o, Order) for o in orders))
        self.assertGreaterEqual(len(orders), 1)

    def test_cache(self):
        """
        测试缓存机制是否生效
        """
        orders1 = self.module.get_orders('2025-09-01', '2025-09-10', {'status': 'Shipped'})
        orders2 = self.module.get_orders('2025-09-01', '2025-09-10', {'status': 'Shipped'})
        # 比较对象内容而非对象实例
        def order_to_dict(order):
            return {
                'order_id': order.order_id,
                'sku': order.sku,
                'quantity': order.quantity,
                'price': order.price,
                'order_date': order.order_date
            }
        list1 = [order_to_dict(o) for o in orders1]
        list2 = [order_to_dict(o) for o in orders2]
        self.assertEqual(list1, list2)

    def test_exception(self):
        """
        测试异常处理，传入非法参数
        """
        orders = self.module.get_orders(None, None)
        self.assertEqual(orders, [])

if __name__ == '__main__':
    unittest.main()

# =================================================
# 核心逻辑锁定，只能调用接口，不允许修改
# =================================================
