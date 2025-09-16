# =================================================
# 文件名称：settlement_module.py
# 日期：2025-09-15 21:00
# 版本号：v1.0
# 作者：Jack
# 功能：获取亚马逊结算/利润数据，解析、标准化、缓存、日志
# 核心逻辑只读，禁止修改，后续只能调用接口
# =================================================

from amz_erp.data_module.utils.utils import cache_save, cache_load, log_info, log_error, retry
from typing import List, Dict, Optional

class Settlement:
    """
    结算对象，包含结算基本信息
    :param settlement_id: 结算编号
    :param total: 结算总额
    :param profit: 利润
    :param date: 结算日期
    """
    def __init__(self, settlement_id: str, total: float, profit: float, date: str):
        self.settlement_id = settlement_id
        self.total = total
        self.profit = profit
        self.date = date

class SettlementModule:
    """
    结算数据公共模块，负责获取、解析、标准化亚马逊结算/利润数据
    """
    def get_settlement(self, filters: Optional[Dict] = None) -> List[Settlement]:
        """
        获取亚马逊结算/利润数据
        :param filters: 过滤条件字典，例如{'date':'2025-09-01'}，可选
        :return: 返回结算对象列表 List[Settlement]
        """
        try:
            log_info(f"获取结算数据，过滤:{filters}")
            cache_key = f"settlement_{str(filters)}"
            cached = cache_load(cache_key)
            if cached:
                log_info("返回缓存结算数据")
                return cached
            raw_data = self._fetch_data(filters)
            settlement_list = self._parse_settlement(raw_data)
            cache_save(cache_key, settlement_list)
            return settlement_list
        except Exception as e:
            log_error(f"结算数据获取异常: {e}")
            return []

    def _fetch_data(self, filters: Optional[Dict]) -> list:
        """
        获取原始结算数据（模拟API或CSV读取）
        :param filters: 过滤条件
        :return: 原始结算数据列表
        """
        # TODO: 实际开发时对接API或读取CSV
        return [
            {'settlement_id': 'S001', 'total': 1000.0, 'profit': 200.0, 'date': '2025-09-01'},
            {'settlement_id': 'S002', 'total': 800.0, 'profit': 150.0, 'date': '2025-09-10'}
        ]

    def _parse_settlement(self, raw_data: list) -> List[Settlement]:
        """
        解析并标准化结算数据
        :param raw_data: 原始结算数据列表
        :return: 标准化结算对象列表
        """
        settlement_list = []
        for item in raw_data:
            s = Settlement(
                settlement_id=item.get('settlement_id', ''),
                total=float(item.get('total', 0)),
                profit=float(item.get('profit', 0)),
                date=item.get('date', '')
            )
            settlement_list.append(s)
        return settlement_list

# =================================================
# 核心逻辑锁定，只能调用接口，不允许修改
# =================================================
