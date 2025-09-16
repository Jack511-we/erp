// 文件名：Sidebar.tsx
// 日期：2025-09-15
// 版本：v1.0.0
// 作者：Auto
// 功能说明：侧边栏导航组件
import React from 'react';
import { Layout, Menu } from 'antd';
import {
  PieChartOutlined,
  BarChartOutlined,
  TableOutlined,
  SettingOutlined,
  AppstoreOutlined,
} from '@ant-design/icons';
const { Sider } = Layout;
const menuItems = [
  { key: 'dashboard', icon: <PieChartOutlined />, label: '首页' },
  { key: 'order', icon: <TableOutlined />, label: '订单分析' },
  { key: 'inventory', icon: <BarChartOutlined />, label: '库存分析' },
  { key: 'ad', icon: <AppstoreOutlined />, label: '广告分析' },
  { key: 'settle', icon: <BarChartOutlined />, label: '结算分析' },
  { key: 'report', icon: <TableOutlined />, label: '综合汇总' },
  { key: 'account-management', icon: <SettingOutlined />, label: '账号管理', link: '/account-management' },
  { key: 'settings', icon: <SettingOutlined />, label: '设置' },
];
import { useNavigate } from 'react-router-dom';

export default function AppSidebar() {
  const navigate = useNavigate();
  const handleClick = (e: any) => {
    const item = menuItems.find(i => i.key === e.key);
    if (item && item.link) {
      navigate(item.link);
    }
  };
  return (
    <Sider width={200} className="bg-gray-50">
      <Menu
        mode="inline"
        defaultSelectedKeys={['dashboard']}
        style={{ height: '100%', borderRight: 0 }}
        items={menuItems}
        onClick={handleClick}
      />
    </Sider>
  );
}
