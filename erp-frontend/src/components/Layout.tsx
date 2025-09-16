import React from 'react';
import { Layout, Menu, Avatar, Dropdown } from 'antd';
import {
  MenuUnfoldOutlined,
  MenuFoldOutlined,
  UserOutlined,
  SettingOutlined,
  LogoutOutlined,
  DashboardOutlined,
  TableOutlined,
  BarChartOutlined,
  FundOutlined,
} from '@ant-design/icons';
import './Layout.css';
import { Link, Outlet } from 'react-router-dom';

const { Header, Sider, Content, Footer } = Layout;

const menuItems = [
  { key: 'dashboard', icon: <DashboardOutlined />, label: <Link to="/dashboard">首页</Link> },
  { key: 'report', icon: <TableOutlined />, label: <Link to="/report">报表分析</Link> },
  { key: 'analysis', icon: <BarChartOutlined />, label: <Link to="/analysis">数据分析</Link> },
  { key: 'settlement', icon: <FundOutlined />, label: <Link to="/settlement">结算分析</Link> },
  // 可继续扩展
];

const userMenu = (
  <Menu>
    <Menu.Item key="setting" icon={<SettingOutlined />}>设置</Menu.Item>
    <Menu.Item key="logout" icon={<LogoutOutlined />}>退出登录</Menu.Item>
  </Menu>
);

export default function MainLayout() {
  const [collapsed, setCollapsed] = React.useState(false);

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sider collapsible collapsed={collapsed} onCollapse={setCollapsed}>
        <div className="logo">ERP Dashboard</div>
        <Menu theme="dark" mode="inline" items={menuItems} />
      </Sider>
      <Layout>
        <Header style={{ background: '#fff', padding: 0, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div style={{ marginLeft: 24, fontWeight: 'bold', fontSize: 18 }}>ERP 管理系统</div>
          <div style={{ marginRight: 24 }}>
            <Dropdown overlay={userMenu} placement="bottomRight">
              <Avatar icon={<UserOutlined />} style={{ cursor: 'pointer' }} />
            </Dropdown>
          </div>
        </Header>
        <Content style={{ margin: '24px 16px 0', background: '#fff', minHeight: 360 }}>
          <Outlet /> {/* 路由页面内容 */}
        </Content>
        <Footer style={{ textAlign: 'center', background: '#f0f2f5' }}>
          © 2025 ERP Dashboard v1.0
        </Footer>
      </Layout>
    </Layout>
  );
}
