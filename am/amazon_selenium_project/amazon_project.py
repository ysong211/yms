from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
import redis
import requests
import xlrd
import random
import time

# 商品名称
title = "[Upgraded] BEYYON 197”Cord Cover On-Wall Cable Concealer Raceway Kit, Cable Management Cord Hider to Hide Wall Mounted TV Cables, Speaker Wires, Computer Cords - 0.98 (W) x 0.47 (H)"

# 关键词
keyword = ""

# 商品价格
price = "20.99"

# 点击的类别定位
location = ""

# 读取xls中cookie
def xls_cookie():
    print("正在获取cookice")
    # 打开表格
    myWorkbook = xlrd.open_workbook('usa6.xls')
    # 获取工作表list。
    mySheets = myWorkbook.sheets()
    # 通过索引顺序获取
    mySheet = mySheets[0]
    # 获取行数
    nrows = mySheet.nrows
    # 随机获取行数
    i = random.randint(1, nrows)
    # 直接获取单元格数据，行数 列数，行数和列数都是从0开始计数。
    myCellValue = mySheet.cell_value(i, 3)
    globals = {
        'true': 0,
        'false': 1
    }
    # 将字符串转列表
    myCellValue = (eval(myCellValue, globals))

    return myCellValue
    # driver = webdriver.Chrome()
    # # driver.delete_all_cookies()
    # driver.get("http://www.amazon.com")
    # driver.delete_all_cookies()
    # print(myCellValue)
    # for d in myCellValue:
    #     name = d["name"]
    #     val = d["value"]
    #     co = {"name": name, "value": val, 'path': '/', 'secure':True}
    #     print(co)
    #     driver.add_cookie(co)
    # driver.get("https://www.amazon.com")


# ip代理
def proxy_ip():
    print("正在获取有效ip")
    try:
        # 实现一个连接池
        pool = redis.ConnectionPool(host='192.168.5.16', db=0)
        ip_pool = redis.Redis(connection_pool=pool)
        ip_p = (ip_pool.srandmember('usa4_ip', 1)[0]).decode('utf-8')
        ips = eval(ip_p)
        ip = ips["ip"] + ":" + ips["port"]
    except Exception as e:
        print('连接redis数据库错误', e)
        proxy_ip()

    try:
        url = "https://www.amazon.com"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }
        proxies = {
            "https": "https://" + ip
        }

        response = requests.get(url=url, proxies=proxies, headers=headers, timeout=8)
        code = response.status_code
        print(code)
        if code == 200:
            if ip == None:
                proxy_ip()
            return ip

        proxy_ip()

    except Exception as e:
        print('IP失效', e)
        print("删除失效ip")
        ip_pool.srem('usa4_ip', ip_p)
        proxy_ip()


# 打开浏览器
def open_chrome():
    # 接收返回的ip
    # ip = proxy_ip()
    # print(ip)
    # print(type(ip))
    chromeOptions = webdriver.ChromeOptions()
    # # 设置代理
    # chromeOptions.add_argument("--proxy-server=http://{}".format(ip))
    # 设置UA
    chromeOptions.add_argument('User-Agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
    # 设置默认编码为 utf-8
    chromeOptions.add_argument('lang=zh_CN.UTF-8')
    # 将设置的ip加入到浏览器中
    driver = webdriver.Chrome(options=chromeOptions)
    # 隐私等待
    driver.implicitly_wait(10)
    # 窗口最大化
    driver.maximize_window()

    try:
        print("打开浏览器")
        driver.get("https://www.amazon.com")
        # 删除cookie
        driver.delete_all_cookies()
        myCellValue = xls_cookie()
        for d in myCellValue:

            name = d["name"]
            val = d["value"]
            co = {"name": name, "value": val}
            driver.add_cookie(co)

        print("搜索")
        driver.refresh()
        search(driver)
    except Exception as e:
        print("打开浏览器失败", e)
        open_chrome()


# 点击商品跳过广告
def ad_goods(driver):
    # 获取网页源代码
    print('跳过广告')
    driver.implicitly_wait(5)
    doc = pq(driver.page_source, parser="html")
    items = doc('.s-include-content-margin.s-border-bottom').items()
    l = []
    for item in items:
        print("==========")

        name = item.find('.a-size-medium.a-color-base.a-text-normal').text()
        if name == "":
            name = item.find('.a-size-base-plus.a-color-base.a-text-normal').text()

        ad = item.find("span.a-size-base.a-color-secondary").text()
        if name == title and ad == "Sponsored":
            l.append(title)

        if name == title and ad != "Sponsored":
            i = len(l)
            (driver.find_elements_by_link_text(title)[i]).click()
            # 执行滚动
            time.sleep(2)
            js1 = "document.documentElement.scrollTop=1000"
            driver.execute_script(js1)
            time.sleep(2)
            js1 = "document.documentElement.scrollTop=2000"
            driver.execute_script(js1)
            time.sleep(2)
            js1 = "document.documentElement.scrollTop=3000"
            driver.execute_script(js1)
            time.sleep(3)
            js1 = "document.documentElement.scrollTop=4000"
            driver.execute_script(js1)
            time.sleep(3)
            js1 = "document.documentElement.scrollTop=5000"
            driver.execute_script(js1)
            time.sleep(2)
            js1 = "document.documentElement.scrollTop=6000"
            driver.execute_script(js1)
            time.sleep(2)
            js1 = "document.documentElement.scrollTop=7000"
            driver.execute_script(js1)
            time.sleep(2)
            js1 = "document.documentElement.scrollTop=8000"
            driver.execute_script(js1)
            time.sleep(2)
            js1 = "document.documentElement.scrollTop=9000"
            driver.execute_script(js1)
            time.sleep(2)
            js1 = "document.documentElement.scrollTop=10000"
            driver.execute_script(js1)
            time.sleep(2)
            js1 = "document.documentElement.scrollTop=11000"
            driver.execute_script(js1)
            time.sleep(2)
            js1 = "document.documentElement.scrollTop=12000"
            driver.execute_script(js1)
            time.sleep(2)
            js1 = "document.documentElement.scrollTop=0"
            driver.execute_script(js1)
            time.sleep(2)
            cart(driver)


# 购物车操作
def cart(driver):
    driver.find_element_by_id('nav-cart').click()
    # 向后退
    driver.back()
    # 加入购物车
    driver.find_element_by_id('add-to-cart-button').click()
    # 执行滚动
    time.sleep(2)
    js1 = "document.documentElement.scrollTop=1000"
    driver.execute_script(js1)
    time.sleep(2)
    js1 = "document.documentElement.scrollTop=2000"
    driver.execute_script(js1)
    time.sleep(2)
    js1 = "document.documentElement.scrollTop=3000"
    driver.execute_script(js1)
    time.sleep(3)
    js1 = "document.documentElement.scrollTop=4000"
    driver.execute_script(js1)
    time.sleep(3)
    js1 = "document.documentElement.scrollTop=5000"
    driver.execute_script(js1)
    time.sleep(2)
    js1 = "document.documentElement.scrollTop=6000"
    driver.execute_script(js1)
    time.sleep(2)
    js1 = "document.documentElement.scrollTop=7000"
    driver.execute_script(js1)
    time.sleep(2)
    js1 = "document.documentElement.scrollTop=8000"
    driver.execute_script(js1)
    time.sleep(2)
    js1 = "document.documentElement.scrollTop=9000"
    driver.execute_script(js1)
    time.sleep(2)
    js1 = "document.documentElement.scrollTop=10000"
    driver.execute_script(js1)
    time.sleep(2)
    js1 = "document.documentElement.scrollTop=11000"
    driver.execute_script(js1)
    time.sleep(2)
    js1 = "document.documentElement.scrollTop=12000"
    driver.execute_script(js1)


# 网页搜索
def search(driver):
    print("网页搜索")
    try:
        # 关键字输入
        driver.find_element_by_id('twotabsearchtextbox').send_keys(keyword)
        driver.find_element_by_css_selector("input.nav-input").click()

        import time
        time.sleep(100)

        # 定位类别
        driver.find_element_by_css_selector(location).click()

        js1 = "document.documentElement.scrollTop=2000"
        driver.execute_script(js1)

        # 价格输入
        driver.find_element_by_id('low-price').send_keys(price)
        driver.find_element_by_id('high-price').send_keys(price)
        driver.find_element_by_css_selector('input.a-button-input[type="submit"]').click()

        ad_goods(driver)
    except Exception as e:
        print("点击失败", e)
        search(driver)


def main():
    open_chrome()


if __name__ == "__main__":
    main()
