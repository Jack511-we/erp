# Architecture.md

## 模块结构
- OrdersModule（订单数据公共模块）
- utils（缓存与日志工具）

## 依赖关系
- OrdersModule 依赖 utils.py 的缓存与日志功能

## 数据流向
- OrdersModule 获取订单数据，解析标准化后通过 utils.py 进行缓存和日志记录

## 版本号
- v1.0

## 更新日期
- 2025-09-15
