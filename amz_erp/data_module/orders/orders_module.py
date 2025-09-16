# =================================================
# 文件名称：orders_module.py
# 日期：2025-09-15 20:30
# 版本号：v1.0
# 作者：Jack
# 功能：获取亚马逊订单数据，解析、标准化、缓存、日志
# 核心逻辑只读，禁止修改，后续只能调用接口
# =================================================

from amz_erp.data_module.utils.utils import cache_save, cache_load, log_info, log_error, retry
from typing import List, Dict, Optional

class Order:
    """
    订单对象，包含订单基本信息
    :param order_id: 订单编号
    :param sku: 商品SKU
    :param quantity: 商品数量
    :param price: 商品价格
    :param order_date: 下单日期
    """
    def __init__(self, order_id: str, sku: str, quantity: int, price: float, order_date: str):
        self.order_id = order_id
        self.sku = sku
        self.quantity = quantity
        self.price = price
        self.order_date = order_date

class OrdersModule:
    """
    订单数据公共模块，负责获取、解析、标准化亚马逊订单数据
    """
    def get_orders(self, start_date: str, end_date: str, filters: Optional[Dict] = None) -> List[Order]:
        """
        获取亚马逊订单数据
        :param start_date: 开始日期，格式YYYY-MM-DD
        :param end_date: 结束日期，格式YYYY-MM-DD
        :param filters: 过滤条件字典，例如{'status':'Shipped'}，可选
        :return: 返回订单对象列表 List[Order]
        """
        # 参数校验，非法参数直接返回空列表
        if not start_date or not end_date:
            log_error("订单数据获取异常: 参数不能为空")
            return []
        try:
            log_info(f"获取订单数据，开始日期:{start_date}，结束日期:{end_date}，过滤:{filters}")
            # 检查缓存
            cache_key = f"orders_{start_date}_{end_date}_{str(filters)}"
            cached = cache_load(cache_key)
            if cached:
                log_info("返回缓存订单数据")
                return cached
            # 模拟获取原始数据（实际可对接API或读取CSV）
            raw_data = self._fetch_data(start_date, end_date, filters)
            orders = self._parse_orders(raw_data)
            cache_save(cache_key, orders)
            return orders
        except Exception as e:
            log_error(f"订单数据获取异常: {e}")
            return []

    def _fetch_data(self, start_date: str, end_date: str, filters: Optional[Dict]) -> list:
        """
        获取原始订单数据（模拟API或CSV读取）
        :param start_date: 开始日期
        :param end_date: 结束日期
        :param filters: 过滤条件
        :return: 原始订单数据列表
        """
        # TODO: 实际开发时对接API或读取CSV
        return [
            {'order_id': 'A001', 'sku': 'SKU1', 'quantity': 2, 'price': 100.0, 'order_date': start_date},
            {'order_id': 'A002', 'sku': 'SKU2', 'quantity': 1, 'price': 200.0, 'order_date': end_date}
        ]

    def _parse_orders(self, raw_data: list) -> List[Order]:
        """
        解析并标准化订单数据
        :param raw_data: 原始订单数据列表
        :return: 标准化订单对象列表
        """
        orders = []
        for item in raw_data:
            order = Order(
                order_id=item.get('order_id', ''),
                sku=item.get('sku', ''),
                quantity=int(item.get('quantity', 0)),
                price=float(item.get('price', 0)),
                order_date=item.get('order_date', '')
            )
            orders.append(order)
        return orders

# =================================================
# 核心逻辑锁定，只能调用接口，不允许修改
# =================================================
