# ERP数据分析系统项目说明

## 架构分层与流程图

![架构流程图](frontend/FlowChart.md)

## 主要模块说明
- 公共数据模块
- 分析模块（多维度分析、异常高亮）
- 页面逻辑模板（统一接口、JSON返回）
- 前端仪表盘（ECharts、交互、主题切换、导出）
- 报表导出（PDF/Excel/CSV/PNG，嵌入图表）

## 典型接口示例

### 1. 分析模块 API
```http
POST /api/order_analysis
Content-Type: application/json
{
  "start_date": "2025-09-01",
  "end_date": "2025-09-15",
  "module": "order"
}
```
返回：
```json
{
  "categories": ["SKU1", "SKU2", "SKU3"],
  "series": [
    { "name": "销售额", "data": [1200, 1500, 900] },
    { "name": "订单量", "data": [30, 45, 20] }
  ],
  "details": [ ... ]
}
```

### 2. 批量报表导出 API
```http
POST /api/batch_export
Content-Type: application/json
{
  "modules": ["order", "inventory"],
  "start_date": "2025-09-01",
  "end_date": "2025-09-15"
}
```
返回：
```json
[
  { "name": "order_summary_20250915.pdf", "url": "/output/order_summary_20250915.pdf" },
  { "name": "inventory_summary_20250915.xlsx", "url": "/output/inventory_summary_20250915.xlsx" }
]
```

## 可视化与交互说明
- 仪表盘支持主题切换、批量刷新、下钻明细、导出图表
- 图表联动与筛选，支持多维度分析
- 前后端数据闭环，接口标准化，异常处理完善

## 维护与扩展建议
- 新增模块/维度自动适配，流程图与文档同步更新
- 代码规范与开发状态标识，便于团队协作

## 文件与代码规范说明
- 所有核心代码文件需包含文件头（文件名、日期、版本、作者、功能说明）
- 主要函数、类、接口需中文注释，便于维护和协作
- 所有接口示例、返回结构、参数说明需同步更新
- 架构分层、流程图、模块说明、接口文档需保持最新

## 表头与注释检查优化
- 已自动检查并补充各模块说明、接口文档、表头注释
- 如发现遗漏或不规范，建议开发时及时补充

## 参考：
- Architecture.md、ModuleDescription.md、API_Docs.md、dashboard_wireframe.md、dashboard_design_guideline.md、dashboard_figma_components.md、dashboard_design_schedule.md、dashboard_design_delivery_checklist.md
