- 输出目录：analysis_module/output/
- 依赖关系：调用utils日志接口，供分析模块和页面逻辑调用
- 版本号：v1.0
- 更新日期：2025-09-15

## 页面逻辑调用模板（order_page.py）
- 功能：调用分析模块接口，展示数据并导出文件，实现数据闭环
- 输入：分析模块接口参数（如日期、过滤条件）
- 输出：分析结果（Python对象）、Excel/CSV/PDF文件
- 文件路径：analysis_module/output/
- 依赖关系：调用分析模块和导出工具
- 版本号：v1.0
- 更新日期：2025-09-15
## ExportUtils（分析导出工具）
- 功能：支持分析结果导出为Excel、CSV、PDF，自动创建输出目录，文件命名规范，支持DataFrame/字典/列表输入，日志记录
- 接口：
	- export_to_excel(data_dict, filename)
	- export_to_csv(df, filename)
	- export_to_pdf(text_lines, filename)
- 输出目录：analysis_module/output/
- 依赖关系：调用utils日志接口，供分析模块和页面逻辑调用
- 版本号：v1.0
- 更新日期：2025-09-15
# AnalysisModule（数据分析模块）
功能：对订单、库存、广告、结算等数据进行分析和汇总，所有分析接口输入输出统一，便于页面逻辑调用
文件：order_analysis.py、inventory_analysis.py、ads_analysis.py、settlement_analysis.py、summary_analysis.py
接口：
	- analyze_orders(start_date, end_date, filters=None) -> List[Dict]
	- analyze_inventory(filters=None) -> List[Dict]
	- analyze_ads(filters=None) -> List[Dict]
	- analyze_settlement(filters=None) -> List[Dict]
	- analyze_summary(params=None) -> Dict
输入：各数据模块返回的对象列表或参数
输出：分析结果（如统计、报表、趋势等，统一为对象列表或字典）
依赖关系：统一调用 data_module 公共接口
版本号：v1.0
更新日期：2025-09-15
# ModuleDescription.md

## OrdersModule（订单模块）
- 功能：获取亚马逊订单数据，解析、标准化、缓存、日志
- 接口：get_orders(start_date, end_date, filters=None) -> List[Order]
- 输入：start_date（YYYY-MM-DD），end_date（YYYY-MM-DD），filters（可选字典）
- 输出：List[Order]，Order对象包含 order_id, sku, quantity, price, order_date
- 依赖关系：依赖 utils.py 的缓存和日志功能
- 版本号：v1.0
- 更新日期：2025-09-15

## InventoryModule（库存模块）
- 功能：获取库存数据，解析、标准化、缓存、日志
- 接口：get_inventory(filters=None) -> List[Inventory]
- 输入：filters（可选字典）
- 输出：List[Inventory]，Inventory对象包含 sku, quantity, warehouse
- 依赖关系：依赖 utils.py 的缓存和日志功能
- 版本号：v1.0
- 更新日期：2025-09-15

## AdsModule（广告模块）
- 功能：获取广告数据，解析、标准化、缓存、日志
- 接口：get_ads(filters=None) -> List[Ad]
- 输入：filters（可选字典）
- 输出：List[Ad]，Ad对象包含 ad_id, sku, spend, clicks
- 依赖关系：依赖 utils.py 的缓存和日志功能
- 版本号：v1.0
- 更新日期：2025-09-15

## SettlementModule（结算/利润模块）
- 功能：获取结算数据，计算利润，缓存、日志
- 接口：get_settlement(filters=None) -> List[Settlement]
- 输入：filters（可选字典）
- 输出：List[Settlement]，Settlement对象包含 settlement_id, total, profit, date
- 依赖关系：依赖 utils.py 的缓存和日志功能
- 版本号：v1.0
- 更新日期：2025-09-15

# ERP系统模块职责与接口说明（优化版）

## 1. 前端仪表盘
- 页面布局、交互逻辑、ECharts渲染、主题切换、导出功能
- 图表组件化，支持联动与下钻
- 数据缓存与批量刷新，异常提示
- 开发状态：已完成基础，交互美化开发中

## 2. API路由
- 参数校验（模块类型、时间范围、维度选择）
- 返回标准 JSON（categories/series/details/status/message）
- 异常处理与状态码，接口文档同步
- 开发状态：已完成主流程，细化校验与异常处理中

## 3. 分析模块
- 公共数据层：统一数据获取接口
- 分析逻辑层：多维度聚合、异常高亮、数据分层
- JSON封装：标准化输出，便于前端渲染
- 开发状态：已完成主分析，扩展维度开发中

## 4. 报表导出
- 多格式支持（PNG/Excel/PDF/CSV）
- 文件命名统一（模块名+时间戳+格式）
- 图表嵌入报表，前端一键下载
- 开发状态：已完成主功能，批量导出与样式优化中

## 5. 测试与维护
- 联调测试、接口文档、流程图同步
- 开发状态标识（已完成/开发中/待测试）
- 维护扩展便捷，支持自动适配新模块/维度

## 文件头与注释规范
- 所有核心代码文件需包含文件头（文件名、日期、版本、作者、功能说明）
- 主要函数、类、接口需中文注释，便于维护和协作
- 所有接口示例、返回结构、参数说明需同步更新

## 模块说明自动回顾
- 已自动检查并补充各模块职责、接口、输入输出、依赖关系、版本号、更新日期
- 如发现遗漏或不规范，建议开发时及时补充
