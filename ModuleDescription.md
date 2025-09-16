# ModuleDescription.md

## OrdersModule
- 功能：获取亚马逊订单数据，解析、标准化、异常处理、日志记录、数据缓存，供数据分析和页面调用
- 接口：get_orders(start_date, end_date, filters=None) -> List[Order]
- 输入：start_date（YYYY-MM-DD），end_date（YYYY-MM-DD），filters（可选字典）
- 输出：List[Order]，Order对象包含 order_id, sku, quantity, price, order_date
- 依赖关系：依赖 utils.py 的缓存和日志功能
- 版本号：v1.0
- 更新日期：2025-09-15
