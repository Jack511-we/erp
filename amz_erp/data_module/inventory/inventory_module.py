# =================================================
# 文件名称：inventory_module.py
# 日期：2025-09-15 21:00
# 版本号：v1.0
# 作者：Jack
# 功能：获取亚马逊库存数据，解析、标准化、缓存、日志
# 核心逻辑只读，禁止修改，后续只能调用接口
# =================================================

from amz_erp.data_module.utils.utils import cache_save, cache_load, log_info, log_error, retry
from typing import List, Dict, Optional

class Inventory:
    """
    库存对象，包含库存基本信息
    :param sku: 商品SKU
    :param quantity: 库存数量
    :param warehouse: 仓库名称
    """
    def __init__(self, sku: str, quantity: int, warehouse: str):
        self.sku = sku
        self.quantity = quantity
        self.warehouse = warehouse

class InventoryModule:
    """
    库存数据公共模块，负责获取、解析、标准化亚马逊库存数据
    """
    def get_inventory(self, filters: Optional[Dict] = None) -> List[Inventory]:
        """
        获取亚马逊库存数据
        :param filters: 过滤条件字典，例如{'warehouse':'WH1'}，可选
        :return: 返回库存对象列表 List[Inventory]
        """
        try:
            log_info(f"获取库存数据，过滤:{filters}")
            cache_key = f"inventory_{str(filters)}"
            cached = cache_load(cache_key)
            if cached:
                log_info("返回缓存库存数据")
                return cached
            raw_data = self._fetch_data(filters)
            inventory_list = self._parse_inventory(raw_data)
            cache_save(cache_key, inventory_list)
            return inventory_list
        except Exception as e:
            log_error(f"库存数据获取异常: {e}")
            return []

    def _fetch_data(self, filters: Optional[Dict]) -> list:
        """
        获取原始库存数据（模拟API或CSV读取）
        :param filters: 过滤条件
        :return: 原始库存数据列表
        """
        # TODO: 实际开发时对接API或读取CSV
        return [
            {'sku': 'SKU1', 'quantity': 100, 'warehouse': 'WH1'},
            {'sku': 'SKU2', 'quantity': 50, 'warehouse': 'WH2'}
        ]

    def _parse_inventory(self, raw_data: list) -> List[Inventory]:
        """
        解析并标准化库存数据
        :param raw_data: 原始库存数据列表
        :return: 标准化库存对象列表
        """
        inventory_list = []
        for item in raw_data:
            inv = Inventory(
                sku=item.get('sku', ''),
                quantity=int(item.get('quantity', 0)),
                warehouse=item.get('warehouse', '')
            )
            inventory_list.append(inv)
        return inventory_list

# =================================================
# 核心逻辑锁定，只能调用接口，不允许修改
# =================================================
