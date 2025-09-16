# =================================================
# 文件名称：test_utils.py
# 日期：2025-09-15 20:00
# 版本号：v1.0
# 作者：Jack
# 功能：验证 utils 工具模块接口
# =================================================


import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import unittest
from amz_erp.data_module.utils.utils import cache_save, cache_load, log_info, log_error, retry

def sample_func(x):
    """示例函数，返回 x+1"""
    return x + 1

def error_func(x):
    """示例异常函数，始终抛出异常"""
    raise ValueError('Test error')

class TestUtils(unittest.TestCase):
    def test_cache(self):
        """测试缓存保存与加载"""
        cache_save('test_key', {'a': 1})
        data = cache_load('test_key')
        self.assertEqual(data, {'a': 1})

    def test_log(self):
        """测试日志记录"""
        log_info('测试 info 日志')
        log_error('测试 error 日志')
        # 检查日志文件内容
        with open('d:/erp/cache/log.txt', 'r', encoding='utf-8') as f:
            logs = f.read()
        self.assertIn('测试 info 日志', logs)
        self.assertIn('测试 error 日志', logs)

    def test_retry_success(self):
        """测试重试成功"""
        result = retry(sample_func, 2, 1)
        self.assertEqual(result, 2)

    def test_retry_fail(self):
        """测试重试失败"""
        result = retry(error_func, 2, 1)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()

# =================================================
# 核心逻辑锁定，只能调用接口，不允许修改
# =================================================
