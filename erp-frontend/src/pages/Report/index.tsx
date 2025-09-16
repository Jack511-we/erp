// 文件名：index.tsx
// 日期：2025-09-15
// 版本：v1.0.0
// 作者：Auto
// 功能说明：报表页

import React, { useState } from 'react';
import { Card, Table, Form, Input, Button, Row, Col } from 'antd';
import ReactECharts from 'echarts-for-react';

const columns = [
	{ title: '订单号', dataIndex: 'orderId', key: 'orderId' },
	{ title: '客户', dataIndex: 'customer', key: 'customer' },
	{ title: '金额', dataIndex: 'amount', key: 'amount' },
	{ title: '状态', dataIndex: 'status', key: 'status' },
];

const data = [
	{ orderId: 'A001', customer: '用户A', amount: 1200, status: '已完成' },
	{ orderId: 'A002', customer: '用户B', amount: 800, status: '待支付' },
	{ orderId: 'A003', customer: '用户C', amount: 1500, status: '已完成' },
];

const chartOption = {
	title: { text: '订单金额分布' },
	tooltip: {},
	xAxis: { data: ['用户A', '用户B', '用户C'] },
	yAxis: {},
	series: [{ name: '金额', type: 'bar', data: [1200, 800, 1500] }],
};

const Report = () => {
	const [form] = Form.useForm();
	const [tableData, setTableData] = useState(data);

		const onSearch = (values: { customer?: string }) => {
		const { customer } = values;
		setTableData(
			customer
				? data.filter(item => item.customer.includes(customer))
				: data
		);
	};

	return (
		<div className="p-6 space-y-6">
			<Card title="筛选条件">
				<Form form={form} layout="inline" onFinish={onSearch}>
					<Form.Item name="customer" label="客户">
						<Input placeholder="输入客户名称" />
					</Form.Item>
					<Form.Item>
						<Button type="primary" htmlType="submit">查询</Button>
					</Form.Item>
				</Form>
			</Card>
			<Card title="订单报表" className="mt-6">
				<Table columns={columns} dataSource={tableData} rowKey="orderId" pagination={false} />
			</Card>
			<Card title="订单金额分布" className="mt-6">
				<ReactECharts option={chartOption} style={{ height: 300 }} />
			</Card>
		</div>
	);
};

export default Report;
