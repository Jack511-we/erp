# =================================================
# 文件名称：export_utils.py
# 日期：2025-09-15
# 版本号：v1.1
# 作者：Jack
# 功能：数据分析模块导出工具，支持 Excel/CSV/PDF
# =================================================


import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt
import matplotlib
import os
import time
from amz_erp.data_module.utils.utils import log_info, log_error

# 设置matplotlib中文字体，解决中文乱码
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
matplotlib.rcParams['axes.unicode_minus'] = False

OUTPUT_DIR = "d:/erp/amz_erp/analysis_module/output/"

def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def get_timestamp():
    return time.strftime('%Y%m%d_%H%M%S')

# 导出 Excel，支持多Sheet
def export_to_excel(data_dict, filename_prefix):
    filename = f"{filename_prefix}_{get_timestamp()}.xlsx"
    ensure_output_dir()
    try:
        writer = pd.ExcelWriter(os.path.join(OUTPUT_DIR, filename), engine='xlsxwriter')
        for sheet, df in data_dict.items():
            df.to_excel(writer, sheet_name=sheet, index=False)
            workbook  = writer.book
            worksheet = writer.sheets[sheet]
            # 表头样式
            header_format = workbook.add_format({'bold': True, 'bg_color': '#DDEBF7', 'border': 1})
            for col_num, value in enumerate(df.columns.values):
                worksheet.write(0, col_num, value, header_format)
            # 自动列宽
            for i, col in enumerate(df.columns):
                max_len = max([len(str(s)) for s in df[col].astype(str)] + [len(col)]) + 2
                worksheet.set_column(i, i, max_len)
            # 冻结表头
            worksheet.freeze_panes(1, 0)
            # 条件格式（如高亮最大值）
            if not df.empty:
                for i, col in enumerate(df.columns):
                    if pd.api.types.is_numeric_dtype(df[col]):
                        worksheet.conditional_format(1, i, len(df), i, {'type': '3_color_scale'})
        writer.close()
        log_info(f"导出Excel成功: {filename}")
    except Exception as e:
        log_error(f"导出Excel失败: {e}")
    return filename

# 导出 CSV
def export_to_csv(df, filename_prefix):
    filename = f"{filename_prefix}_{get_timestamp()}.csv"
    ensure_output_dir()
    try:
        df.to_csv(os.path.join(OUTPUT_DIR, filename), index=False)
        log_info(f"导出CSV成功: {filename}")
    except Exception as e:
        log_error(f"导出CSV失败: {e}")
    return filename

# 导出 PDF（文本内容+可选图表）
def export_to_pdf(text_lines, filename_prefix, chart_data=None):
    filename = f"{filename_prefix}_{get_timestamp()}.pdf"
    ensure_output_dir()
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)
        for line in text_lines:
            pdf.multi_cell(0, 8, line)
        # 可选图表
        if chart_data is not None:
            chart_path = os.path.join(OUTPUT_DIR, f"{filename_prefix}_chart_{get_timestamp()}.png")
            plt.figure(figsize=(6,3))
            plt.bar(chart_data['x'], chart_data['y'])
            plt.title(chart_data.get('title', ''))
            plt.xlabel(chart_data.get('xlabel', ''))
            plt.ylabel(chart_data.get('ylabel', ''))
            plt.tight_layout()
            plt.savefig(chart_path)
            plt.close()
            pdf.image(chart_path, x=10, y=pdf.get_y()+10, w=180)
        pdf.output(os.path.join(OUTPUT_DIR, filename))
        log_info(f"导出PDF成功: {filename}")
    except Exception as e:
        log_error(f"导出PDF失败: {e}")
    return filename

# 升级版：导出 PDF（支持封面、目录、多图表布局）
def export_to_pdf(text_lines, filename_prefix, chart_data_list=None, cover_info=None, toc=None):
    filename = f"{filename_prefix}_{get_timestamp()}.pdf"
    ensure_output_dir()
    try:
        pdf = FPDF()
        # 封面页
        if cover_info:
            pdf.add_page()
            pdf.set_font("Arial", 'B', 20)
            pdf.cell(0, 20, cover_info.get('title', 'ERP数据分析报表'), ln=True, align='C')
            pdf.set_font("Arial", size=12)
            pdf.cell(0, 10, f"日期: {cover_info.get('date', get_timestamp())}", ln=True, align='C')
            pdf.cell(0, 10, f"公司: {cover_info.get('company', '演示公司')}", ln=True, align='C')
            pdf.ln(20)
        # 目录页
        if toc:
            pdf.add_page()
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 12, "目录", ln=True, align='L')
            pdf.set_font("Arial", size=12)
            for idx, item in enumerate(toc):
                pdf.cell(0, 8, f"{idx+1}. {item}", ln=True, align='L')
            pdf.ln(10)
        # 正文内容
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)
        for line in text_lines:
            pdf.multi_cell(0, 8, line)
        # 多图表布局
        if chart_data_list:
            for chart_data in chart_data_list:
                chart_path = os.path.join(OUTPUT_DIR, f"{filename_prefix}_chart_{get_timestamp()}.png")
                plt.figure(figsize=chart_data.get('figsize', (6,3)))
                chart_type = chart_data.get('type', 'bar')
                if chart_type == 'bar':
                    plt.bar(chart_data['x'], chart_data['y'])
                elif chart_type == 'pie':
                    plt.pie(chart_data['y'], labels=chart_data['x'], autopct='%1.1f%%')
                elif chart_type == 'line':
                    plt.plot(chart_data['x'], chart_data['y'])
                plt.title(chart_data.get('title', ''))
                plt.xlabel(chart_data.get('xlabel', ''))
                plt.ylabel(chart_data.get('ylabel', ''))
                plt.tight_layout()
                plt.savefig(chart_path)
                plt.close()
                pdf.add_page()
                pdf.image(chart_path, x=10, y=30, w=180)
        pdf.output(os.path.join(OUTPUT_DIR, filename))
        log_info(f"导出PDF成功: {filename}")
    except Exception as e:
        log_error(f"导出PDF失败: {e}")
    return filename

# =================================================
# 核心逻辑只读，禁止修改，后续只能调用接口
# =================================================
