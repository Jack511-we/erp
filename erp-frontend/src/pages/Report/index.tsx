// 文件名：index.tsx
// 日期：2025-09-15
// 版本：v1.0.0
// 作者：Auto
// 功能说明：报表页

import React, { useState } from 'react';
import { Card, Form, Input, Button } from 'antd';
import AggregatedTable from '../../components/AggregatedTable';

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

// 保留你需要的 Report 组件，删除重复声明
const Report = () => {
	// 修正为实际聚合文件参数
	const account = 'US';
	const year = 'JUL';
	const month = 'day';
	const filename = '2025/daily_summary_2025.pkl';

	return (
		<div className="p-6 space-y-6">
			<Card title="筛选条件">
				<Form layout="inline">
					{/* 可扩展筛选表单 */}
				</Form>
			</Card>
			<Card title="销售日汇总表格" className="mt-6">
				<AggregatedTable account={account} year={year} month={month} filename={filename} />
			</Card>
		</div>
	);
};

export default Report;
