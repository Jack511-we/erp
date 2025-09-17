# 用户删除接口，按 userId 删除 d:/erp/data/用户管理/user_list.json 中用户
from flask import Blueprint, request, jsonify
import os, json

delete_user_api = Blueprint('delete_user_api', __name__)

@delete_user_api.route('/api/delete_user', methods=['POST'])
def delete_user():
    data = request.json
    userId = data.get('userId')
    if not userId:
        return jsonify({'code': 1, 'msg': '缺少 userId'})
    user_file = 'd:/erp/data/用户管理/user_list.json'
    if not os.path.exists(user_file):
        return jsonify({'code': 2, 'msg': '用户数据文件不存在'})
    with open(user_file, 'r', encoding='utf-8') as f:
        user_list = json.load(f)
    new_list = [u for u in user_list if u.get('userId') != userId]
    if len(new_list) == len(user_list):
        return jsonify({'code': 3, 'msg': '未找到对应用户'})
    with open(user_file, 'w', encoding='utf-8') as f:
        json.dump(new_list, f, ensure_ascii=False, indent=2)
    return jsonify({'code': 0, 'msg': '删除成功'})
