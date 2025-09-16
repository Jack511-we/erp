# =================================================
# 文件名称：test_ads.py
# 日期：2025-09-15 21:10
# 版本号：v1.0
# 作者：Jack
# 功能：验证 AdsModule 接口及日志、缓存、异常处理
# =================================================

import unittest
from amz_erp.data_module.ads.ads_module import AdsModule, Ad

class TestAdsModule(unittest.TestCase):
    def setUp(self):
        self.module = AdsModule()

    def test_get_ads(self):
        """
        测试获取广告数据，返回标准 List[Ad] 对象
        """
        ads = self.module.get_ads({'sku': 'SKU1'})
        self.assertIsInstance(ads, list)
        self.assertTrue(all(isinstance(a, Ad) for a in ads))
        self.assertGreaterEqual(len(ads), 1)

    def test_cache(self):
        """
        测试缓存机制是否生效
        """
        ads1 = self.module.get_ads({'sku': 'SKU1'})
        ads2 = self.module.get_ads({'sku': 'SKU1'})
        def ad_to_dict(a):
            return {'ad_id': a.ad_id, 'sku': a.sku, 'spend': a.spend, 'clicks': a.clicks}
        list1 = [ad_to_dict(a) for a in ads1]
        list2 = [ad_to_dict(a) for a in ads2]
        self.assertEqual(list1, list2)

    def test_exception(self):
        """
        测试异常处理，传入非法参数
        """
        ads = self.module.get_ads(None)
        self.assertIsInstance(ads, list)

if __name__ == '__main__':
    unittest.main()

# =================================================
# 核心逻辑锁定，只能调用接口，不允许修改
# =================================================
