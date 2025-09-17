from flask import Flask, send_from_directory

app = Flask(__name__)

# 允许直接访问 D:/erp/data/用户管理 下的所有文件
@app.route('/data/<path:filename>')
def serve_user_data(filename):
    return send_from_directory(r'D:/erp/data/用户管理', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
