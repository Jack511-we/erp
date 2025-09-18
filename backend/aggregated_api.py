import os
import pickle
from flask import Blueprint, jsonify, request

# 自动聚合结果接口
aggregated_api = Blueprint('aggregated_api', __name__)

# 示例路径，可根据实际目录结构调整
data_root = r'd:/erp/data/亚马逊月销售统计资料/aggregated_pkl/owosald'

@aggregated_api.route('/api/aggregated/<account>/<year>/<month>/<path:filename>', methods=['GET'])
def get_aggregated_data(account, year, month, filename):
    # 构建pkl文件路径
    file_path = os.path.join(data_root, account, year, month, filename)
    if not os.path.exists(file_path):
        return jsonify({'error': '文件不存在'}), 404
    try:
        with open(file_path, 'rb') as f:
            df = pickle.load(f)
        # DataFrame转JSON
        data = df.to_dict(orient='records')
        return jsonify({'data': data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
