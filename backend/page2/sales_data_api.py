# 销售数据表格与筛选接口
from flask import Blueprint, request, jsonify

sales_data_api = Blueprint('sales_data_api', __name__)

@sales_data_api.route('/api/sales-data', methods=['GET'])
def get_sales_data():
    account = request.args.get('account')
    country = request.args.get('country')
    month = request.args.get('month')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    # TODO: 查询数据库或文件，返回销售数据
    data = [
        {"asin": "B001", "sales": 100, "date": "2025-09-01", "country": "US", "account": "A1"}
    ]
    return jsonify({"code": 0, "msg": "success", "data": data})
