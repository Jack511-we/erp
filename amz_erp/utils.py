# -*- coding: utf-8 -*-
"""
通用工具模块：缓存装饰器、日志、异常处理等
"""
import functools
import hashlib
import pickle
import logging

_cache = {}

# 日志配置
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s',
    filename='amz_erp.log',
    filemode='a'
)
logger = logging.getLogger('amz_erp')

def cache_result(func):
    """
    简单内存缓存装饰器，参数序列化为key，重复查询直接返回缓存结果
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key_bytes = pickle.dumps((func.__name__, args, kwargs))
        key = hashlib.md5(key_bytes).hexdigest()
        if key in _cache:
            return _cache[key]
        result = func(*args, **kwargs)
        _cache[key] = result
        return result
    return wrapper

# 统一异常处理装饰器
def catch_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"异常: {func.__name__}: {e}", exc_info=True)
            return {'error': str(e)}
    return wrapper

# 可扩展：持久化缓存、超时、清理等
