// 文件名：Content.tsx
// 日期：2025-09-15
// 版本：v1.0.0
// 作者：Auto
// 功能说明：内容区域，承载路由页面
import React from 'react';
import { Layout } from 'antd';
const { Content } = Layout;
export default function AppContent({ children }: { children: React.ReactNode }) {
  return (
    <Content className="p-6 min-h-[80vh] bg-gray-100">
      {children}
    </Content>
  );
}
