// 文件名：main.tsx
// 日期：2025-09-15
// 版本：v1.0.0
// 作者：Auto
// 功能说明：渲染入口
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';
const root = ReactDOM.createRoot(document.getElementById('root')!);
root.render(<React.StrictMode><App /></React.StrictMode>);
