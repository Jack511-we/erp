import os
import glob
import pandas as pd

# 自动读取字段映射
def load_field_mapping(mapping_path):
    mapping = {}
    current_key = None
    with open(mapping_path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if line.startswith('[') and line.endswith(']'):
                current_key = line[1:-1]
                mapping[current_key] = []
            elif current_key:
                mapping[current_key].append(line)
    return mapping

RAW_DATA_DIR = r'D:\erp\data\亚马逊月销售统计资料\owosald\US'
OUTPUT_PATH = r'D:\erp\data\聚合管理\owosald\US\日\daily_aggregated.csv'
FIELD_MAPPING_PATH = r'D:\erp\data\聚合管理\owosald\US\field_mapping.txt'

def get_all_csv_files():
    # 获取所有月度文件夹下的CSV文件
    csv_files = []
    for month_dir in os.listdir(RAW_DATA_DIR):
        month_path = os.path.join(RAW_DATA_DIR, month_dir)
        if os.path.isdir(month_path):
            csv_files += glob.glob(os.path.join(month_path, '*.csv'))
    return csv_files

def aggregate_by_day(csv_files):
    field_mapping = load_field_mapping(FIELD_MAPPING_PATH)
    dfs = []
    for file in csv_files:
        try:
            df = pd.read_csv(file, skiprows=7)
            dfs.append(df)
        except Exception as e:
            print(f'文件读取失败: {file}, 错误: {e}')
    if not dfs:
        print('无有效数据文件')
        return
    all_data = pd.concat(dfs, ignore_index=True)
    # 自动查找日期和销售额字段
    date_col = None
    sales_col = None
    for col in all_data.columns:
        for candidate in field_mapping.get('时间', []):
            if col.strip().lower() == candidate.strip().lower():
                date_col = col
        for candidate in field_mapping.get('销售额', []):
            if col.strip().lower() == candidate.strip().lower():
                sales_col = col
    if not date_col or not sales_col:
        print('未找到有效的日期或销售额字段，请检查 field_mapping.txt 和原始数据表头')
        return
    # 原始详细数据输出
    grouped = all_data.groupby(date_col)[sales_col].sum().reset_index()
    grouped = grouped.sort_values(date_col)
    grouped.to_csv(OUTPUT_PATH, index=False, encoding='utf-8-sig')
    print(f'日聚合结果已保存: {OUTPUT_PATH}')

    # 只按年月日聚合，生成 daily_sum.csv
    import numpy as np
    import re
    def extract_date(val):
        # 支持多种日期格式，自动提取年月日
        if isinstance(val, str):
            # 例如 "Apr 1, 2025 12:19:52 AM PDT" -> "2025-04-01"
            match = re.search(r'(\w{3,})\s(\d{1,2}),\s(\d{4})', val)
            if match:
                month_str = match.group(1)
                day = int(match.group(2))
                year = int(match.group(3))
                # 英文月份转数字
                month_map = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12,
                             'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
                month = month_map.get(month_str, 0)
                return f'{year:04d}-{month:02d}-{day:02d}'
        return np.nan
    all_data['聚合日期'] = all_data[date_col].apply(extract_date)
    # 自动筛选数值型字段（排除时间字段）
    exclude_cols = [date_col, '聚合日期']
    numeric_cols = [col for col in all_data.columns if col not in exclude_cols and np.issubdtype(all_data[col].dtype, np.number)]
    # 如果有部分字段是字符串但实际为数字，尝试转换
    for col in all_data.columns:
        if col not in exclude_cols and all_data[col].dtype == object:
            try:
                all_data[col] = pd.to_numeric(all_data[col], errors='ignore')
            except:
                pass
    numeric_cols = [col for col in all_data.columns if col not in exclude_cols and np.issubdtype(all_data[col].dtype, np.number)]
    # 按日聚合所有数值型字段
    sum_grouped = all_data.groupby('聚合日期')[numeric_cols].sum().reset_index()
    sum_grouped = sum_grouped.sort_values('聚合日期')
    sum_path = os.path.join(os.path.dirname(OUTPUT_PATH), "daily_sum.csv")
    sum_grouped.to_csv(sum_path, index=False, encoding='utf-8-sig')
    print(f'日汇总（按年月日）已保存: {sum_path}')

if __name__ == '__main__':
    csv_files = get_all_csv_files()
    aggregate_by_day(csv_files)
