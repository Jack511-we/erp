# 用户列表接口，供前端导入弹窗动态获取账号和国家
from flask import Blueprint, jsonify
import os, json

users_api = Blueprint('users_api', __name__)

@users_api.route('/api/users', methods=['GET'])
def get_users():
    user_file = 'd:/erp/data/用户管理/user_list.json'
    accounts = []
    countries = []
    if os.path.exists(user_file):
        with open(user_file, 'r', encoding='utf-8') as f:
            user_list = json.load(f)
        accounts = list({u['accountName'] for u in user_list if 'accountName' in u})
        countries = list({u['country'] for u in user_list if 'country' in u})
    return jsonify({'accounts': accounts, 'countries': countries})
