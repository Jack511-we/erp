// 文件名：Header.tsx
// 日期：2025-09-15
// 版本：v1.0.0
// 作者：Auto
// 功能说明：顶栏组件（Logo、项目名、用户菜单、主题切换）
import React from 'react';
import { Layout, Menu, Dropdown, Avatar, Switch } from 'antd';
const { Header } = Layout;
const userMenu = (
  <Menu>
    <Menu.Item key="settings">设置</Menu.Item>
    <Menu.Item key="logout">登出</Menu.Item>
  </Menu>
);
export default function AppHeader() {
  return (
    <Header className="flex items-center justify-between px-4 bg-white shadow">
      <div className="flex items-center gap-2">
        <img src="/logo.svg" alt="Logo" className="h-8" />
        <span className="font-bold text-lg">ERP数据分析系统</span>
      </div>
      <div className="flex items-center gap-4">
        <Switch checkedChildren="🌙" unCheckedChildren="☀️" />
        <Dropdown overlay={userMenu}>
          <Avatar style={{ backgroundColor: '#87d068' }} icon={null} />
        </Dropdown>
      </div>
    </Header>
  );
}
