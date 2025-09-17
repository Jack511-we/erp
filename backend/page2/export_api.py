# 导出接口
from flask import Blueprint, request, send_file
import io

export_api = Blueprint('export_api', __name__)

@export_api.route('/api/export', methods=['GET'])
def export_sales_data():
    account = request.args.get('account')
    country = request.args.get('country')
    month = request.args.get('month')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    # TODO: 查询数据并生成导出文件
    # 示例：生成一个简单的 csv 文件流
    csv_content = 'asin,sales,date,country,account\nB001,100,2025-09-01,US,A1\n'
    return send_file(io.BytesIO(csv_content.encode('utf-8')), mimetype='text/csv', as_attachment=True, download_name='sales_data.csv')
