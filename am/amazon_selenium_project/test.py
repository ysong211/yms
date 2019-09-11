import requests
from selenium import webdriver
chromeOptions = webdriver.ChromeOptions()
import time


# for i in range(1, 5):
#     response = requests.post("http://91.189.187.94:22999/api/refresh_sessions/24000")
#
#     proxies = {
#         "http": "http://91.189.187.94:24000",
#         "https": "http://91.189.187.94:24000",
#     }
#
#     respons = requests.get("http://www.baidu.com", proxies=proxies)
#     print(response.status_code)
#     e = requests.get("http://lumtest.com/myip.json",  proxies=proxies)
#     print(e.status_code)
from selenium.webdriver.common.keys import Keys


# def f1():
#     try:
#         chromeOptions.add_argument("--proxy-server=http://91.189.187.94:24013")
#
#         browser = webdriver.Chrome(options=chromeOptions)
#
#         # browser.get("http://www.amazon.com")
#
#         # browser.get("http://httpbin.org/ip")
#         # print(browser.page_source)
#
#         # 输入空格键
#         time.sleep(2)
#         browser.close()
#         f1()
#     except Exception as e:
#         print(e)
#         f1()
#
#
# f1()

# from selenium.webdriver.common.proxy import *
# import redis
#
# def proxy_ip():
#     print("正在获取有效ip")
#     try:
#         # 实现一个连接池
#         pool = redis.ConnectionPool(host='192.168.5.11', db=0)
#         ip_pool = redis.Redis(connection_pool=pool)
#         ip_p = (ip_pool.srandmember('usa4_ip', 1)[0]).decode('utf-8')
#         ips = eval(ip_p)
#         ip = ips["ip"] + ":" + ips["port"]
#
#         print(type(ip))
#         print(ip)
#     except Exception as e:
#         print('连接redis数据库错误', e)
#         proxy_ip()
#
#     try:
#         url = "https://www.amazon.com"
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
#         }
#         proxies = {
#             "https": "https://" + ip
#         }
#
#         response = requests.get(url=url, proxies=proxies, headers=headers, )
#         code = response.status_code
#         print(code)
#         if code == 200:
#             # 设置代理
#             chromeOptions.add_argument("--proxy-server=http://{}".format(ip))
#
#             # myProxy = "http://{}".format(ip)
#             # proxy = Proxy({
#             #     'proxyType': ProxyType.MANUAL,
#             #     'httpProxy': myProxy,
#             #     'ftpProxy': myProxy,
#             #     'sslProxy': myProxy,
#             #     'noProxy': ''})
#
#             browser = webdriver.Chrome(options=chromeOptions)
#
#
#             try:
#
#                 browser.get("https://www.amazon.com")
#                 # browser.get("http://httpbin.org/ip")
#                 print(browser.page_source)
#                 time.sleep(5)
#                 browser.close()
#                 proxy_ip()
#             except Exception as e:
#                 print(e)
#                 proxy_ip()
#
#         proxy_ip()
#
#     except Exception as e:
#         print('IP失效', e)
#         print("删除失效ip")
#         ip_pool.srem('usa4_ip', ip_p)
#         proxy_ip()
#
#
# proxy_ip()


import xlwt
from selenium import webdriver
import xlrd
import random

# cookie = 'cookies/usa1_1000.xls'
cookie = 'cookies/usa1.xls'


# 读取xls中cookie
def xls_cookie():
    # 创建工作workbook
    workbook = xlwt.Workbook(encoding="utf-8")

    # 创建工作表worksheet,填入表名
    worksheet = workbook.add_sheet('sheet1')
    worksheet1 = workbook.add_sheet('sheet2')

    # 打开表格
    myWorkbook = xlrd.open_workbook(cookie)
    # 获取工作表list。
    mySheets = myWorkbook.sheets()
    # 通过索引顺序获取
    mySheet = mySheets[1]
    # 获取行数
    nrows = mySheet.nrows
    # 随机获取行数
    # i = random.randint(1, nrows-1)
    a = 0
    a1 = 0
    for i in range(10, nrows):
        driver = webdriver.Chrome()
        driver.get("https://www.amazon.com")

        # 直接获取单元格数据，行数 列数，行数和列数都是从0开始计数。
        Value = mySheet.cell_value(i, 3)
        globals = {
            'true': 0,
            'false': 1
        }
        # 将字符串转列表
        myCellValue = (eval(Value, globals))
        print(len(myCellValue))
        driver.delete_all_cookies()
        print("导入cookie")
        for d in myCellValue:
            name = d["name"]
            val = d["value"]
            co = {"name": name, "value": val}
            driver.add_cookie(co)

        driver.refresh()
        name = driver.find_element_by_css_selector("#nav-link-accountList > span.nav-line-1").text
        print(name)
        # print(type(name))
        # 关键字输入
        driver.find_element_by_id('twotabsearchtextbox').send_keys("lightning cable")
        driver.find_element_by_css_selector("input.nav-input").click()
        name1 = driver.find_element_by_css_selector("#nav-link-accountList > span.nav-line-1").text
        print(name1)
        # print(type(name1))
        # time.sleep(1000)

        # if name != "Hello, Sign in" and name1 != "Hello, Sign in":
        #     worksheet.write(a, 3, Value)
        #     a += 1
        #
        # if name == "Hello, Sign in" or name1 == "Hello, Sign in":
        #     worksheet1.write(a1, 3, Value)
        #     a1 += 1
        #
        # workbook.save('usa1.xls')
        driver.quit()


def main():

   while True:
        xls_cookie()


if __name__ == "__main__":
    main()
