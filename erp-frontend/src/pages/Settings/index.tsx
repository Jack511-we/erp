// 文件名：index.tsx
// 日期：2025-09-15
// 版本：v1.0.0
// 作者：Auto
// 功能说明：设置页

import React from 'react';
import { Card, Form, Input, Button, Switch } from 'antd';

const Settings = () => {
	const [form] = Form.useForm();

		const onFinish = (values: { email: string; nickname: string; darkMode: boolean }) => {
		// 可在此集成后端 API
		console.log('设置已保存:', values);
	};

	return (
		<div className="p-6">
			<Card title="用户设置">
				<Form
					form={form}
					layout="vertical"
					onFinish={onFinish}
					initialValues={{ email: '', nickname: '', darkMode: false }}
				>
					<Form.Item name="email" label="邮箱" rules={[{ required: true, message: '请输入邮箱' }]}> 
						<Input placeholder="请输入邮箱" />
					</Form.Item>
					<Form.Item name="nickname" label="昵称">
						<Input placeholder="请输入昵称" />
					</Form.Item>
					<Form.Item name="darkMode" label="深色模式" valuePropName="checked">
						<Switch />
					</Form.Item>
					<Form.Item>
						<Button type="primary" htmlType="submit">保存设置</Button>
					</Form.Item>
				</Form>
			</Card>
		</div>
	);
};

export default Settings;
