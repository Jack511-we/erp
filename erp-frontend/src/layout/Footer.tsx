// 文件名：Footer.tsx
// 日期：2025-09-15
// 版本：v1.0.0
// 作者：Auto
// 功能说明：底部版权/版本信息
import React from 'react';
import { Layout } from 'antd';
const { Footer } = Layout;
export default function AppFooter() {
  return (
    <Footer className="text-center text-xs text-gray-400 bg-white">
      ERP数据分析系统 ©2025 | v1.0.0
    </Footer>
  );
}
