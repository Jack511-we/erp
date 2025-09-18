
# coding: utf-8
"""
统计图表数据 API
- 严格分层：Controller -> Service -> Repository
- 数据源：D:/erp/data/亚马逊月销售统计资料 下所有 CSV
- 支持按账号、国家、时间类型（日/周/月/季/半年/年）、时间范围筛选
- 返回格式严格遵循规范
"""
import os
import pandas as pd
from flask import Blueprint, request, jsonify

statistics_api = Blueprint('statistics_api', __name__)

DATA_ROOT = r'D:/erp/data/亚马逊月销售统计资料'

# Service 层
class ChartDataService:
    @staticmethod
    def get_chart_data(account, country, year, time_type, time_value):
        # 汇总所有相关 CSV 文件
        dfs = []
        for root, dirs, files in os.walk(DATA_ROOT):
            for file in files:
                if file.endswith('.csv') and str(year) in file:
                    df = pd.read_csv(os.path.join(root, file), encoding='utf-8')
                    dfs.append(df)
        if not dfs:
            return []
        df = pd.concat(dfs, ignore_index=True)
        # 过滤账号、国家
        if account:
            df = df[df['账号'] == account]
        if country:
            df = df[df['国家'] == country]
        # 时间字段假定为 '日期'，格式 yyyy-mm-dd
        if '日期' not in df.columns:
            return []
        df['日期'] = pd.to_datetime(df['日期'], errors='coerce')
        # 按时间类型聚合
        if time_type == 'day':
            # 按天筛选
            if time_value:
                start, end = time_value.split('~') if '~' in time_value else (time_value, time_value)
                start = pd.to_datetime(start.strip())
                end = pd.to_datetime(end.strip())
                df = df[(df['日期'] >= start) & (df['日期'] <= end)]
            group = df.groupby(df['日期'].dt.date)['销售额'].sum().reset_index()
            result = [{'label': str(row['日期']), 'value': float(row['销售额'])} for _, row in group.iterrows()]
        elif time_type == 'week':
            df['week'] = df['日期'].dt.isocalendar().week
            if time_value:
                df = df[df['week'] == int(time_value)]
            group = df.groupby('week')['销售额'].sum().reset_index()
            result = [{'label': f'{row["week"]}周', 'value': float(row['销售额'])} for _, row in group.iterrows()]
        elif time_type == 'month':
            df['month'] = df['日期'].dt.month
            if time_value:
                df = df[df['month'] == int(time_value)]
            group = df.groupby('month')['销售额'].sum().reset_index()
            result = [{'label': f'{row["month"]}月', 'value': float(row['销售额'])} for _, row in group.iterrows()]
        elif time_type == 'quarter':
            df['quarter'] = df['日期'].dt.quarter
            if time_value:
                q_map = {'Q1': 1, 'Q2': 2, 'Q3': 3, 'Q4': 4}
                df = df[df['quarter'] == q_map.get(time_value, 0)]
            group = df.groupby('quarter')['销售额'].sum().reset_index()
            result = [{'label': f'Q{row["quarter"]}', 'value': float(row['销售额'])} for _, row in group.iterrows()]
        elif time_type == 'halfyear':
            df['half'] = df['日期'].dt.month.apply(lambda m: 1 if m <= 6 else 2)
            if time_value:
                h_map = {'H1': 1, 'H2': 2}
                df = df[df['half'] == h_map.get(time_value, 0)]
            group = df.groupby('half')['销售额'].sum().reset_index()
            result = [{'label': '上半年' if row['half'] == 1 else '下半年', 'value': float(row['销售额'])} for _, row in group.iterrows()]
        elif time_type == 'year':
            df['year'] = df['日期'].dt.year
            if time_value:
                df = df[df['year'] == int(time_value)]
            group = df.groupby('year')['销售额'].sum().reset_index()
            result = [{'label': f'{row["year"]}年', 'value': float(row['销售额'])} for _, row in group.iterrows()]
        else:
            result = []
        return result

# Controller 层
@statistics_api.route('/api/chart-data', methods=['GET'])
def chart_data():
    account = request.args.get('account', '')
    country = request.args.get('country', '')
    year = request.args.get('year', '')
    time_type = request.args.get('type', 'month')
    time_value = request.args.get('value', '')
    data = ChartDataService.get_chart_data(account, country, year, time_type, time_value)
    return jsonify({
        'code': 0,
        'message': 'success',
        'data': data
    })
