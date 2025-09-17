# 导入接口：处理文件上传
from flask import Blueprint, request, jsonify
import os

upload_api = Blueprint('upload_api', __name__)

@upload_api.route('/api/upload', methods=['POST'])
def upload_file():
    account = request.form.get('account')
    country = request.form.get('country')
    file = request.files.get('file')
    filename = file.filename if file else ''

    # 校验文件名格式
    if not filename or not valid_filename(filename):
        return jsonify({"code": 1, "msg": "文件名格式错误"})

    year = filename[:4]
    month = filename[4:7].upper()
    save_dir = f"D:/erp/data/亚马逊月销售统计资料/{account}/{country}/{month}/"
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, filename)

    if os.path.exists(save_path):
        return jsonify({"code": 1, "msg": "同名文件已存在"})

    file.save(save_path)
    return jsonify({"code": 0, "msg": "上传成功"})


def valid_filename(filename):
    # 前4位为年份，后3位为英文月份
    if len(filename) < 7:
        return False
    year = filename[:4]
    month = filename[4:7].upper()
    return year.isdigit() and month in ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
