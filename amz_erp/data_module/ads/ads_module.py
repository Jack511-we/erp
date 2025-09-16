# =================================================
# 文件名称：ads_module.py
# 日期：2025-09-15 21:00
# 版本号：v1.0
# 作者：Jack
# 功能：获取亚马逊广告数据，解析、标准化、缓存、日志
# 核心逻辑只读，禁止修改，后续只能调用接口
# =================================================

from amz_erp.data_module.utils.utils import cache_save, cache_load, log_info, log_error, retry
from typing import List, Dict, Optional

class Ad:
    """
    广告对象，包含广告基本信息
    :param ad_id: 广告编号
    :param sku: 商品SKU
    :param spend: 广告花费
    :param clicks: 点击次数
    """
    def __init__(self, ad_id: str, sku: str, spend: float, clicks: int):
        self.ad_id = ad_id
        self.sku = sku
        self.spend = spend
        self.clicks = clicks

class AdsModule:
    """
    广告数据公共模块，负责获取、解析、标准化亚马逊广告数据
    """
    def get_ads(self, filters: Optional[Dict] = None) -> List[Ad]:
        """
        获取亚马逊广告数据
        :param filters: 过滤条件字典，例如{'sku':'SKU1'}，可选
        :return: 返回广告对象列表 List[Ad]
        """
        try:
            log_info(f"获取广告数据，过滤:{filters}")
            cache_key = f"ads_{str(filters)}"
            cached = cache_load(cache_key)
            if cached:
                log_info("返回缓存广告数据")
                return cached
            raw_data = self._fetch_data(filters)
            ads_list = self._parse_ads(raw_data)
            cache_save(cache_key, ads_list)
            return ads_list
        except Exception as e:
            log_error(f"广告数据获取异常: {e}")
            return []

    def _fetch_data(self, filters: Optional[Dict]) -> list:
        """
        获取原始广告数据（模拟API或CSV读取）
        :param filters: 过滤条件
        :return: 原始广告数据列表
        """
        # TODO: 实际开发时对接API或读取CSV
        return [
            {'ad_id': 'AD001', 'sku': 'SKU1', 'spend': 50.0, 'clicks': 100},
            {'ad_id': 'AD002', 'sku': 'SKU2', 'spend': 30.0, 'clicks': 60}
        ]

    def _parse_ads(self, raw_data: list) -> List[Ad]:
        """
        解析并标准化广告数据
        :param raw_data: 原始广告数据列表
        :return: 标准化广告对象列表
        """
        ads_list = []
        for item in raw_data:
            ad = Ad(
                ad_id=item.get('ad_id', ''),
                sku=item.get('sku', ''),
                spend=float(item.get('spend', 0)),
                clicks=int(item.get('clicks', 0))
            )
            ads_list.append(ad)
        return ads_list

# =================================================
# 核心逻辑锁定，只能调用接口，不允许修改
# =================================================
