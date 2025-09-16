// 文件名：index.tsx
// 日期：2025-09-15
// 版本：v1.0.0
// 作者：Auto
// 功能说明：分析页

import React from 'react';
import { Card, Row, Col } from 'antd';
import ReactECharts from 'echarts-for-react';

const pieOption = {
	title: { text: '用户分布' },
	tooltip: { trigger: 'item' },
	legend: { top: 'bottom' },
	series: [
		{
			name: '用户类型',
			type: 'pie',
			radius: '50%',
			data: [
				{ value: 1048, name: '普通用户' },
				{ value: 735, name: 'VIP用户' },
				{ value: 580, name: '企业用户' },
			],
		},
	],
};

const lineOption = {
	title: { text: '活跃趋势' },
	tooltip: {},
	xAxis: { data: ['1月', '2月', '3月', '4月', '5月', '6月'] },
	yAxis: {},
	series: [{ name: '活跃用户', type: 'line', data: [500, 800, 600, 900, 1200, 1100] }],
};

const Analysis = () => (
	<div className="p-6 space-y-6">
		<Row gutter={16}>
			<Col span={12}>
				<Card title="用户分布">
					<ReactECharts option={pieOption} style={{ height: 300 }} />
				</Card>
			</Col>
			<Col span={12}>
				<Card title="活跃趋势">
					<ReactECharts option={lineOption} style={{ height: 300 }} />
				</Card>
			</Col>
		</Row>
	</div>
);

export default Analysis;
