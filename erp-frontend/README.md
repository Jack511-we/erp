
# ERP数据分析系统前端项目说明

## 目录结构
```
# erp-frontend

## 项目简介

本项目为企业ERP前端，包含低代码引擎演示、业务数据分析页面、容器隔离规范等。

## 页面结构与容器说明

### 主业务页面（index02.html）
- 公共区：页眉、页脚、主内容区
- 主内容区容器：
	- container-01：数据统计图表
	- container2：销售数据表（支持资料上传，所有分析容器公用数据源）
	- container-03/04：业务分析容器（并排，分别左/右对齐，表格自适应）
	- container5：复制自container2，作为扩展分析区

### 容器隔离规范
- 所有容器为主内容区平级子元素，结构独立，样式/JS隔离
- 尺寸表达统一，宽度80%，间距通过margin/gap控制
- 表格区采用Tabulator插件，支持自适应、合计行、列宽拖拽

### 资料上传与数据流
- 资料上传入口仅在container2，支持Excel/CSV文件
- 上传后数据自动填充表格，并供后续分析容器公用
- 后端需提供文件存储路径与上传接口，前端通过AJAX/Fetch对接

### 目录结构
- public/：静态资源
- src/：主业务代码
- lowcode-engine-demo/：低代码引擎演示与容器模板
- ...existing code...

## 开发与扩展建议
- 所有新容器/模块需遵循容器隔离规范
- 通用样式/JS建议抽离为独立文件，减少重复
- 资料上传、数据接口、交互细节可持续优化

---
如需详细容器规范与开发指引，请查阅《容器隔离规范.md》。
│   ├── App.tsx            # 应用主入口，包含路由和布局
│   ├── main.tsx           # React 渲染入口
│   ├── index.css          # 全局样式，集成 Tailwind CSS
├── package.json           # 项目依赖
├── README.md              # 项目说明
└── ...（其他配置文件）
```

## 主要文件说明
- **public/index.html**：静态资源入口，挂载 React 应用。
- **src/assets/**：存放图片、SVG、logo 等静态资源。
- **src/components/**：通用可复用组件，如表格、筛选器、图表、进度条等。
- **src/pages/**：每个页面一个文件夹，index.tsx 为页面主文件。
- **src/router/**：路由配置，统一管理页面跳转。
- **src/store/**：Redux Toolkit 状态管理，存放全局/模块状态。
- **src/utils/**：工具函数，如接口请求（axios 封装）、数据格式化等。
- **src/App.tsx**：应用主入口，包含路由和整体布局。
- **src/main.tsx**：React 渲染入口。
- **src/index.css**：全局样式，集成 Tailwind CSS。
- **package.json**：项目依赖与脚本配置。
- **README.md**：项目说明文档。

## 技术栈
- React 18
- Ant Design
- ECharts
- Redux Toolkit
- Tailwind CSS
- TypeScript

## 快速开始
1. 安装依赖：`npm install`
2. 启动开发环境：`npm start` 或 `npm run dev`

## 参考文档
- 架构分层与流程图：`frontend/FlowChart.md`
- 设计规范与 Wireframe：`dashboard_design_guideline.md`
- 组件清单与交付进度：`dashboard_figma_components.md`、`dashboard_design_schedule.md`

---
如需详细开发规范、接口文档、组件说明等，请参考项目内相关 md 文件。
