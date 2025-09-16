// 文件名：AppLayout.tsx
// 日期：2025-09-15
// 版本：v1.0.0
// 作者：Auto
// 功能说明：整体布局框架
import React from 'react';
import { Layout } from 'antd';
import AppHeader from './Header';
import AppSidebar from './Sidebar';
import AppContent from './Content';
import AppFooter from './Footer';

export default function AppLayout({ children }: { children: React.ReactNode }) {
  return (
    <Layout style={{ minHeight: '100vh' }}>
      <AppHeader />
      <Layout>
        <AppSidebar />
        <Layout>
          <AppContent>{children}</AppContent>
          <AppFooter />
        </Layout>
      </Layout>
    </Layout>
  );
}
