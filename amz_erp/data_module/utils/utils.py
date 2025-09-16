
# =================================================
# 文件名称：utils.py
# 开发时间：2025-09-15 18:00
# 版本号：v1.1
# 作者：Jack
# 功能：日志、缓存、异常处理、API重试工具
# 核心逻辑只读，禁止修改，后续只能调用接口
# =================================================

import pickle
import os
import time
from typing import Any, Callable

# 缓存文件路径
CACHE_PATH = 'd:/erp/cache/'
if not os.path.exists(CACHE_PATH):
    os.makedirs(CACHE_PATH)

def cache_save(key: str, data: Any) -> None:
    """
    缓存数据到本地文件
    :param key: 缓存键
    :param data: 需要缓存的数据
    :return: 无
    """
    try:
        with open(os.path.join(CACHE_PATH, f'{key}.pkl'), 'wb') as f:
            pickle.dump(data, f)
        log_info(f"缓存数据成功: {key}")
    except Exception as e:
        log_error(f"缓存数据异常: {e}")

def cache_load(key: str) -> Any:
    """
    加载本地缓存数据
    :param key: 缓存键
    :return: 缓存数据或None
    """
    try:
        with open(os.path.join(CACHE_PATH, f'{key}.pkl'), 'rb') as f:
            data = pickle.load(f)
        log_info(f"加载缓存成功: {key}")
        return data
    except Exception as e:
        log_error(f"加载缓存异常: {e}")
        return None

def log_info(msg: str) -> None:
    """
    记录普通日志信息到本地文件
    :param msg: 日志内容
    :return: 无
    """
    with open(os.path.join(CACHE_PATH, 'log.txt'), 'a', encoding='utf-8') as f:
        f.write(f"[INFO] {time.strftime('%Y-%m-%d %H:%M:%S')} {msg}\n")

def log_error(msg: str) -> None:
    """
    记录错误日志信息到本地文件
    :param msg: 错误内容
    :return: 无
    """
    with open(os.path.join(CACHE_PATH, 'log.txt'), 'a', encoding='utf-8') as f:
        f.write(f"[ERROR] {time.strftime('%Y-%m-%d %H:%M:%S')} {msg}\n")

def retry(func: Callable, max_attempts: int = 3, *args, **kwargs) -> Any:
    """
    API重试工具，自动重试指定函数
    :param func: 需要重试的函数
    :param max_attempts: 最大重试次数，默认3次
    :param args: 位置参数
    :param kwargs: 关键字参数
    :return: 函数返回值或None
    """
    attempt = 0
    while attempt < max_attempts:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            log_error(f"重试第{attempt+1}次失败: {e}")
            attempt += 1
            time.sleep(1)
    log_error(f"API重试失败，已达最大次数: {max_attempts}")
    return None

# =================================================
# 核心逻辑完成后锁定，不允许修改字段结构
# =================================================
