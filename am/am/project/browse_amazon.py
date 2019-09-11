from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import redis
import requests


def redis_ip():
    # 实现一个连接池,无需重新新建数据库连接
    pool = redis.ConnectionPool(host='127.0.0.1')
    ip_pool = redis.Redis(connection_pool=pool)
    # 返回集合中一个或多个随机数
    ip = ip_pool.srandmember('foo', 1)
    # 移除并返回集合中的一个随机元素
    # ip = ip_pool.spop('foo', 1)

    return ip


def request_code():
    redis_ip()

