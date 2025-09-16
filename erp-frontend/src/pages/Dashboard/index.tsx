// 文件名：index.tsx
// 日期：2025-09-15
// 版本：v1.0.0
// 作者：Auto
// 功能说明：首页仪表盘

import React from 'react';
import { Card, Row, Col, Statistic, List } from 'antd';
import ReactECharts from 'echarts-for-react';

const chartOption = {
	title: { text: '访问趋势' },
	tooltip: {},
	xAxis: { data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日'] },
	yAxis: {},
	series: [{ name: '访问量', type: 'line', data: [120, 200, 150, 80, 70, 110, 130] }],
};

const recentData = [
	{ title: '用户A', description: '注册成功', time: '09:00' },
	{ title: '用户B', description: '下单成功', time: '09:15' },
	{ title: '用户C', description: '支付完成', time: '09:30' },
];

const Dashboard = () => (
	<div className="p-6 space-y-6">
		<Row gutter={16}>
			<Col span={6}>
				<Card>
					<Statistic title="今日访问量" value={1128} suffix="人次" />
				</Card>
			</Col>
			<Col span={6}>
				<Card>
					<Statistic title="新增用户" value={32} suffix="人" />
				</Card>
			</Col>
			<Col span={6}>
				<Card>
					<Statistic title="订单数" value={87} suffix="单" />
				</Card>
			</Col>
			<Col span={6}>
				<Card>
					<Statistic title="成交额" value={12800} prefix="￥" />
				</Card>
			</Col>
		</Row>
		<Card title="访问趋势" className="mt-6">
			<ReactECharts option={chartOption} style={{ height: 300 }} />
		</Card>
		<Card title="最新动态" className="mt-6">
			<List
				itemLayout="horizontal"
				dataSource={recentData}
			renderItem={(item: { title: string; description: string; time: string }) => (
					<List.Item>
						<List.Item.Meta
							title={item.title}
							description={item.description}
						/>
						<div>{item.time}</div>
					</List.Item>
				)}
			/>
		</Card>
	</div>
);

export default Dashboard;
