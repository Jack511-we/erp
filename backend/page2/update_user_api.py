# 用户信息编辑接口，按 userId 更新 d:/erp/data/用户管理/user_list.json 中用户信息
from flask import Blueprint, request, jsonify
import os, json

update_user_api = Blueprint('update_user_api', __name__)

@update_user_api.route('/api/update_user', methods=['POST'])
def update_user():
    data = request.json
    userId = data.get('userId')
    company = data.get('company')
    accountName = data.get('accountName')
    country = data.get('country')
    registerTime = data.get('registerTime')
    if not userId:
        return jsonify({'code': 1, 'msg': '缺少 userId'})
    user_file = 'd:/erp/data/用户管理/user_list.json'
    if not os.path.exists(user_file):
        return jsonify({'code': 2, 'msg': '用户数据文件不存在'})
    with open(user_file, 'r', encoding='utf-8') as f:
        user_list = json.load(f)
    found = False
    for u in user_list:
        if u.get('userId') == userId:
            u['company'] = company or u.get('company')
            u['accountName'] = accountName or u.get('accountName')
            u['country'] = country or u.get('country')
            u['registerTime'] = registerTime or u.get('registerTime')
            found = True
            break
    if not found:
        return jsonify({'code': 3, 'msg': '未找到对应用户'})
    with open(user_file, 'w', encoding='utf-8') as f:
        json.dump(user_list, f, ensure_ascii=False, indent=2)
    return jsonify({'code': 0, 'msg': '编辑成功'})
