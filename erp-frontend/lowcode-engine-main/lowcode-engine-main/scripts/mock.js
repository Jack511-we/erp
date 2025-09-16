const express = require('express');
const app = express();
const port = 6001;

// 解决跨域
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  next();
});

// 模拟物料数据（左侧组件库）
app.get('/api/materials', (req, res) => {
  res.json({
    success: true,
    data: [
      { componentName: 'Button', title: '按钮' },
      { componentName: 'Input', title: '输入框' },
      { componentName: 'Table', title: '表格' }
    ]
  });
});

// 模拟页面 schema（中间画布）
app.get('/api/page', (req, res) => {
  res.json({
    success: true,
    data: {
      componentName: 'Page',
      children: [
        { componentName: 'Button', props: { children: '提交' } }
      ]
    }
  });
});

// 启动 mock 服务
app.listen(port, () => {
  console.log(`✅ Mock server running at http://localhost:${port}`);
});
