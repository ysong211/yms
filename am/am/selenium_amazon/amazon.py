import os

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from pyquery import PyQuery as pq
import pymongo
import time


# mongodb配置
MONGO_URL = 'localhost'
MONGO_DB = 'AM'
MONGO_TABLE = 'amazon'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
# browser.set_window_size(1400,1400)




def search(name):
    print("正在搜索")
    try:
        browser.get('https://www.amazon.com/gp/new-releases/home-garden')

        # 输入框
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#twotabsearchtextbox"))
        )
        # 搜索按钮
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#nav-search > form > div.nav-right > div > input")))

        # 清空搜索框
        # input.clear()
        print(name)
        input.send_keys(name)
        # 按钮事件
        submit.click()

        # 隐式等待
        browser.implicitly_wait(3)

        # 判断页面是否加载完成
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".a-disabled")))

        get_products()
        # next_page()
        # return total.text

    except TimeoutException:
        return search(name)


# 翻页
def next_page(page_number):
    print("正在翻页")
    try:
        # 确定按钮
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "。a-last > a")))

        submit.click()

        # time.sleep(3)
        # 判断是否跳到下一页
        # wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"li.a-last > a")))
        # 滚动条滚动到底部
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)","")

        get_products()
    except TimeoutException:
        # 如果失败则重新请求
        next_page(page_number)



# 获取商品列表页面信息
def get_products():
    # 最外层的div包括所有的商品
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.s-result-list.s-search-results.sg-row')))
    # 获取网页源代码
    html = browser.page_source

    # 解析网页代码
    # 声明pq对象
    doc = pq(browser.page_source,parser="html")
    items = doc('div.s-result-list.s-search-results.sg-row > div').items()

    for item in items:
        #商品价格
        price = item.find(".a-offscreen").text()
        #商品总评价数量
        commit = item.find(".a-link-normal > .a-size-base").text()
        #评价url
        commit_url = item.find(".a-link-normal").attr('href')
        if commit_url:
            commit_url = "https://www.amazon.cn" + commit_url + "#customerReviews"
        #商品名称
        name = item.find(".a-size-base-plus.a-color-base.a-text-normal").text()
        #商品url
        name_url = item.find(".a-link-normal.a-text-normal").attr('href')
        if name_url:
            name_url = "https://www.amazon.cn" + name_url


        product = {
            'price': price,
            'commit': commit,
            'name': name,
            'commit_url': commit_url,
            'name_url': name_url,
        }

        get_goods(product)


# # 获取商品详情页信息
def get_goods(product):
    print("进入商品详情页")

    browser.get(product['name_url'])
    # 隐式等待
    browser.implicitly_wait(5)

    doc = pq(browser.page_source, parser="html")

    # 商品的主体信息
    ptable = doc('.a-color-success.ddm-font-size-15').text()


    # 加入大字典中
    product['ptable'] = ptable

    get_shop(product)


# 评价信息
def get_shop(product):
    print("进入评价信息")
    browser.get(product['commit_url'])
    # 隐式等待
    browser.implicitly_wait(5)

    doc = pq(browser.page_source, parser="html")
    # 商品的评价信息
    com = doc('#cm-cr-dp-review-list').text()


    # 加入大字典中
    product['com'] = com

    save_to_mongo(product)


# 存储mongodb
def save_to_mongo(result):
    try:
        if db['name'].update({"name": result['name'], "price": result['price']}, {"$set": dict(result)}, upsert=True,multi=True):
        # if db[MONGO_TABLE].insert_one(result):
            print("存储到MONGODB成功",result)
            pass
    except Exception:
        print("存储失败", result)



def main():
    l = ['手机','电脑']
    for name in l:
        search(name)
    # 关闭浏览器
    browser.quit()
if __name__ =="__main__":
    main()
