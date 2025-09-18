# 主启动文件，注册第2页面所有接口蓝图

# 主启动文件，注册第2页面所有接口蓝图
from flask import Flask, send_from_directory
from flask_cors import CORS
import os
from page2.upload_api import upload_api
from page2.statistics_api import statistics_api
from page2.sales_data_api import sales_data_api
from page2.export_api import export_api
from page2.register_api import register_api
from page2.users_api import users_api
from page2.delete_user_api import delete_user_api
from aggregated_api import aggregated_api

app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

app.register_blueprint(upload_api)
app.register_blueprint(statistics_api)
app.register_blueprint(sales_data_api)
app.register_blueprint(export_api)
app.register_blueprint(register_api)
app.register_blueprint(users_api)
app.register_blueprint(delete_user_api)
app.register_blueprint(aggregated_api)
# 支持前端页面静态文件访问
@app.route('/pages/<path:filename>')
def serve_frontend_page(filename):
    dir_path = r'D:/erp/erp-frontend/lowcode-engine-demo/deploy-space/static/pages'
    return send_from_directory(dir_path, filename)

# 静态文件路由，支持 /data/用户管理/user_list.json 访问
@app.route('/data/用户管理/user_list.json')
def serve_user_list():
    data_dir = os.path.abspath('d:/erp/data/用户管理')
    response = send_from_directory(data_dir, 'user_list.json')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.route('/data/用户管理/<path:filename>')
def serve_user_file(filename):
    data_dir = os.path.abspath('d:/erp/data/用户管理')
    response = send_from_directory(data_dir, filename)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.route('/data/聚合管理/owosald/US/日/<path:filename>')
def serve_daily_sum(filename):
    dir_path = r'D:/erp/data/聚合管理/owosald/US/日'
    return send_from_directory(dir_path, filename)

@app.route('/data/<path:filename>')
def serve_data(filename):
    return send_from_directory('D:/erp/data', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
