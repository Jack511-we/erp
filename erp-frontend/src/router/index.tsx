// 文件名：index.tsx
// 日期：2025-09-15
// 版本：v1.0.0
// 作者：Auto
// 功能说明：路由配置
import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import AppLayout from '../layout/AppLayout';
import Dashboard from '../pages/Dashboard';
import Report from '../pages/Report';
import Analysis from '../pages/Analysis';
import Settings from '../pages/Settings';
import AccountManagement from '../pages/AccountManagement';

const Router = () => (
  <BrowserRouter>
    <AppLayout>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/report" element={<Report />} />
        <Route path="/analysis" element={<Analysis />} />
        <Route path="/settings" element={<Settings />} />
  <Route path="/account-management" element={<AccountManagement />} />
      </Routes>
    </AppLayout>
  </BrowserRouter>
);
export default Router;
