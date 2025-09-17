# 用户注册接口，保存用户信息到 d:/erp/data/用户管理/user_list.json
from flask import Blueprint, request, jsonify
import os, json, uuid, datetime

register_api = Blueprint('register_api', __name__)

@register_api.route('/api/register', methods=['POST'])
def register_user():
    data = request.json
    company = data.get('company')
    accountName = data.get('accountName')
    country = data.get('country')
    if not company or not accountName or not country:
        return jsonify({'code': 1, 'msg': '信息不完整'})
    userId = str(uuid.uuid4())[:8]
    registerTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user_info = {
        'userId': userId,
        'company': company,
        'accountName': accountName,
        'country': country,
        'registerTime': registerTime
    }
    user_file = 'd:/erp/data/用户管理/user_list.json'
    os.makedirs(os.path.dirname(user_file), exist_ok=True)
    if os.path.exists(user_file):
        with open(user_file, 'r', encoding='utf-8') as f:
            user_list = json.load(f)
    else:
        user_list = []
    # 检查是否已存在相同账号和国家
    for u in user_list:
        if u['accountName'] == accountName and u['country'] == country:
            return jsonify({'code': 2, 'msg': '该账号在该国家已注册，禁止重复！'})
    user_list.append(user_info)
    with open(user_file, 'w', encoding='utf-8') as f:
        json.dump(user_list, f, ensure_ascii=False, indent=2)
    return jsonify({'code': 0, 'msg': '注册成功', 'data': user_info})
