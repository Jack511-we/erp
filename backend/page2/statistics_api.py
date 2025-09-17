# 数据统计图表接口
from flask import Blueprint, request, jsonify

statistics_api = Blueprint('statistics_api', __name__)

@statistics_api.route('/api/statistics', methods=['GET'])
def get_statistics():
    period = request.args.get('period')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    # TODO: 查询数据库或文件，返回统计数据
    data = [
        {"date": "2025-09-01", "value": 123},
        {"date": "2025-09-02", "value": 456}
    ]
    return jsonify({"code": 0, "msg": "success", "data": data})
