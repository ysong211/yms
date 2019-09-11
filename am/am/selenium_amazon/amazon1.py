import os

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
import pymongo
import time

# mongodb配置
MONGO_URL = 'localhost'
MONGO_DB = 'amazon'
# MONGO_TABLE = 'British'
MONGO_TABLE = 'imagen3'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
# browser.set_window_size(1000, 1000)


def search(i):
    print("打开浏览器")
    try:
        url = 'https://www.amazon.es/gp/bestsellers/electronics/'+i
        # url = 'https://www.amazon.co.uk/gp/bestsellers/electronics/' + i + '/ref=pd_zg_hrsr_electronics'
        browser.get(url)
        addr()
        time.sleep(5)

        # 隐式等待
        browser.implicitly_wait(3)
        get_products()

    except TimeoutException:
        return search(i)


# 修改配送地址
def addr():
    print("修改配送地址")
    try:
        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#nav-global-location-slot > span > a"))).click()

        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#GLUXZipUpdateInput"))
        ).send_keys("28001")

        # PO94LJ 英国
        # 28001 西班牙

        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#GLUXZipUpdate"))).click()

        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".a-button-inner"))).click()

        browser.implicitly_wait(1)
        browser.back()

    except TimeoutError:
        return addr()


# 翻页
def next_page(i):
    print("正在翻页")
    try:
        url = 'https://www.amazon.es/gp/bestsellers/electronics/' + i + '/ref=zg_bsnr_pg_2?ie=UTF8&pg=2'
        # url = 'https://www.amazon.co.uk/Best-Sellers-Electronics-Mobile-Phone-Bluetooth-Headsets/zgbs/electronics/' + i + '/ref=zg_bs_pg_2/262-1247477-1654514?_encoding=UTF8&pg=2'
        browser.get(url)
        get_products()
    except TimeoutException:
        # 如果失败则重新请求
        next_page(i)


# 获取商品列表页面信息
def get_products():
    print("获取商品列表页面信息")

    # 最外层的div包括所有的商品
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#zg-ordered-list')))

    # 解析网页代码,声明pq对象
    doc = pq(browser.page_source, parser="html")
    items = doc('#zg-ordered-list .zg-item-immersion').items()

    a = 0
    for item in items:
        a += 1
        # 商品价格
        price = item.find(".p13n-sc-price").text()

        # 评价数量
        commit = item.find(".a-size-small.a-link-normal").text()

        # 评价星级
        icon = item.find(".a-icon-alt").text()
        icon = icon[0:4]

        # 商品名称
        name = item.find(".p13n-sc-truncated").attr('title')
        if name == None:
            name = item.find(".p13n-sc-truncated").text()

        # 商品url
        name_url = item.find(".a-link-normal").attr('href')
        if name_url:
            name_url = "https://www.amazon.es" + name_url
            # name_url = "https://www.amazon.co.uk" + name_url

        product = {
            'price': price,
            'commit': commit,
            'name': name,
            'icon': icon,
            'name_url': name_url,
        }

        print('爬取第', a, '个')
        get_goods(product)


# 获取商品详情页信息
def get_goods(product):
    print("进入商品详情页")
    try:
        browser.get(product['name_url'])
        # 隐式等待
        browser.implicitly_wait(5)
        doc = pq(browser.page_source, parser="html")

        # 类似商品
        upd = doc("#olp_feature_div").text()
        # upd = upd[:-9]


        # ASIN码
        ASIN = doc('#prodDetails > div > div.column.col2 > div:nth-child(1) > div.content.pdClearfix > div > div > table > tbody > tr:nth-child(1) > td.value').text()
        if ASIN == "" or len(ASIN) != 10:
            ASIN = doc('#productDetails_detailBullets_sections1 > tbody > tr:nth-child(5) > td').text()
            if ASIN == "" or len(ASIN) != 10:
                ASIN = doc('#detail-bullets > table > tbody > tr > td > div > ul > li:nth-child(2) > td').text()
                if ASIN == "" or len(ASIN) != 10:
                    ASIN = doc('#detail-bullets > table > tbody > tr > td > div > ul > li:nth-child(3) > td').text()
                    if ASIN == "" or len(ASIN) != 10:
                        ASIN = doc('#productDetails_detailBullets_sections1 > tbody > tr:nth-child(4) > td').text()
                        if ASIN == "" or len(ASIN) != 10:
                            ASIN = doc('#productDetails_detailBullets_sections1 > tbody > tr:nth-child(6) > td').text()
                            if ASIN == "" or len(ASIN) != 10:
                                ASIN = doc('#productDetails_detailBullets_sections1 > tbody > tr:nth-child(1) > td').text()
                                if ASIN == "" or len(ASIN) != 10:
                                    ASIN = doc('#detail-bullets > table > tbody > tr > td > div > ul > li:nth-child(1)').text()
                                    if ASIN == "" or len(ASIN) != 10:
                                        ASIN = doc('#prodDetails > div > div.column.col2 > div:nth-child(1) > div.content.pdClearfix > div > div > table > tbody > tr:nth-child(1) > td.value').text()
                                        if ASIN == "" or len(ASIN) != 16:
                                            ASIN = doc("#detail_bullets_id > table > tbody > tr > td > div > ul > li:nth-child(6)").text()
                                            if ASIN == "" or len(ASIN) != 16:
                                                ASIN = doc('#detail-bullets > table > tbody > tr > td > div.content > ul > li:nth-child(2)').text()
                                                if ASIN == "" or len(ASIN) != 16:
                                                    ASIN = doc('#detail-bullets > table > tbody > tr > td > div.content > ul > li:nth-child(3)').text()
                                                    if ASIN == "" or len(ASIN) != 16:
                                                        ASIN = doc('#detail-bullets > table > tbody > tr > td > div.content > ul > li:nth-child(5)').text()
                                                        if ASIN == "" or len(ASIN) != 16:
                                                            ASIN = doc('#detail-bullets > table > tbody > tr > td > div.content > ul > li:nth-child(6)').text()
        if len(ASIN) > 10:
            ASIN = ASIN[-10:]


        # 排行
        BestSellersRank = doc("#productDetails_detailBullets_sections1 > tbody > tr:nth-child(11) > td").text()
        if BestSellersRank == "":
            BestSellersRank = doc("#productDetails_detailBullets_sections1 > tbody > tr:nth-child(9) > td").text()
            if BestSellersRank == "":
                BestSellersRank = doc("#productDetails_detailBullets_sections1 > tbody > tr:nth-child(8) > td").text()
                if BestSellersRank == "":
                    BestSellersRank = doc("#SalesRank > td.value").text()
                    if BestSellersRank == "":
                        BestSellersRank = doc("#productDetails_detailBullets_sections1 > tbody > tr:nth-child(6) > td").text()
                        if BestSellersRank == "":
                            BestSellersRank = doc("#productDetails_detailBullets_sections1 > tbody > tr:nth-child(7) > td").text()
                            if BestSellersRank == "":
                                BestSellersRank = doc("#SalesRank").text()
                                if BestSellersRank == "":
                                    BestSellersRank = doc("#productDetails_detailBullets_sections1 > tbody > tr:nth-child(3) > td > span").text()

        BestSellersRank = BestSellersRank.split('\n')
        BestSellersRank = BestSellersRank[1:]
        # BestSellersRank = BestSellersRank[2:]

        BestSellersRank1 = BestSellersRank[0:1]
        BestSellersRank2 = BestSellersRank[1:]
        BestSellersRank2 = ''.join(BestSellersRank2)
        BestSellersRank1 = ''.join(BestSellersRank1)

        # 厂家
        Manufacturer = doc("#bylineInfo").text()

        # 包装尺寸
        PackageDimensions = doc("#productDetails_detailBullets_sections1 > tbody > tr:nth-child(1) > td").text()
        if PackageDimensions == "":
            PackageDimensions = doc("#prodDetails > div.wrapper.USlocale > div.column.col1 > div > div.content.pdClearfix > div > div > table > tbody > tr:nth-child(2) > td.value").text()
            if PackageDimensions == "":
                PackageDimensions = doc("#detail-bullets > table > tbody > tr > td > div.content > ul > li:nth-child(1)").text()
                if PackageDimensions == "":
                    PackageDimensions = doc("#prodDetails > div.wrapper.ESlocale > div.column.col1 > div > div.content.pdClearfix > div > div > table > tbody > tr:nth-child(3) > td.value").text()
                    if PackageDimensions == "":
                        PackageDimensions = doc("#detail_bullets_id > table > tbody > tr > td > div > ul > li:nth-child(1)").text()
        if len(PackageDimensions) > 35:
            PackageDimensions = PackageDimensions[20:]

        # 重量
        ItemWeight = doc("#productDetails_techSpec_section_1 > tbody > tr:nth-child(1) > td").text()
        if ItemWeight == "":
            ItemWeight = doc("#prodDetails > div.wrapper.USlocale > div.column.col1 > div > div.content.pdClearfix > div > div > table > tbody > tr:nth-child(1) > td.value").text()
            if ItemWeight == "":
                ItemWeight = doc("#productDetails_detailBullets_sections1 > tbody > tr:nth-child(2) > td").text()
                if ItemWeight == "":
                    ItemWeight = doc("#prodDetails > div.wrapper.ESlocale > div.column.col1 > div > div.content.pdClearfix > div > div > table > tbody > tr:nth-child(2) > td.value").text()
                    if ItemWeight == "":
                        ItemWeight = doc("#detail_bullets_id > table > tbody > tr > td > div > ul > li:nth-child(2)").text()

        # 加入字典中
        product['ASIN'] = ASIN
        product['BestSellersRank1'] = BestSellersRank1
        product['BestSellersRank2'] = BestSellersRank2
        product['PackageDimensions'] = PackageDimensions
        product['ItemWeight'] = ItemWeight
        product['Manufacturer'] = Manufacturer
        product['upd'] = upd

        save_to_mongo(product)

    except TimeoutException:
        get_goods(product)


# 存储mongodb
def save_to_mongo(result):
    print("存储mongodb")
    try:
        if db[MONGO_TABLE].update({"name": result['name'], "price": result['price']}, {"$set": dict(result)}, upsert=True, multi=True):

            print("存储到MONGODB成功", result)
    except Exception:
        print("存储失败", result)


def main():
    # 西班牙
    L = ['934033031']
    # 英国
    # L = ['340401031']
    for i in L:
        search(i)
        # 传入页码
        for page in range(1, 2):
            next_page(i)
    # 关闭浏览器
    browser.quit()


if __name__ == "__main__":
    main()