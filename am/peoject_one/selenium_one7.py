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
MONGO_TABLE = 'tws'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
browser.set_window_size(1000, 1000)


# 获取商品详情页信息
def get_goods():
    print("进入商品详情页")
    try:
        browser.get("https://www.amazon.de/dp/B07H7HHLTD/ref=sspa_dk_detail_6?psc=1&pd_rd_i=B07H7HHLTD&pd_rd_w=IN79E&pf_rd_p=493495a8-6974-49af-bd47-5bd55a278ea6&pd_rd_wg=EKAP6&pf_rd_r=HVBS19M44ETK0S8ET6YZ&pd_rd_r=4e50dfb4-bd62-466a-b179-15cc9c6a8870")
        # 隐式等待
        time.sleep(5)
        browser.implicitly_wait(5)
        doc = pq(browser.page_source, parser="html")

        # 价格
        price = doc("#priceblock_ourprice").text()

        # 评价数量
        commit = doc("#acrCustomerReviewText").text()

        # 评价星级
        icon = doc("#acrPopover > span.a-declarative > a > i.a-icon.a-icon-star.a-star-4-5 > span").text()

        # 商品名称
        name = doc("#productTitle").text()

        # 商品url
        name_url = "https://www.amazon.de/dp/B07H7HHLTD/ref=sspa_dk_detail_6?psc=1&pd_rd_i=B07H7HHLTD&pd_rd_w=IN79E&pf_rd_p=493495a8-6974-49af-bd47-5bd55a278ea6&pd_rd_wg=EKAP6&pf_rd_r=HVBS19M44ETK0S8ET6YZ&pd_rd_r=4e50dfb4-bd62-466a-b179-15cc9c6a8870"

        # 类似商品
        upd = doc(".olp-padding-right").text()

        ASIN = doc("#detail_bullets_id > table > tbody > tr > td > div.content > ul > li:nth-child(5)").text()

        # 排行
        Bk = doc("#SalesRank > ul").text()

        # 厂家
        Mr = doc("#bylineInfo").text()

        # 评论人
        name1 = doc("#customer_review-R2ALMGHSI4EMD8 > div:nth-child(1) > a > div.a-profile-content > span").text()
        name2 = doc("#customer_review-R3CTW7AUSY2IKN > div:nth-child(1) > a > div.a-profile-content > span").text()
        name3 = doc("#customer_review-R3QSLKKNB0WBYE > div:nth-child(1) > a > div.a-profile-content > span").text()
        name4 = doc("#customer_review-R2X92Z357EPX6 > div:nth-child(1) > a > div.a-profile-content > span").text()

        # 评论人链接
        name_like1 = doc("#customer_review-R2ALMGHSI4EMD8 > div.a-row.review-comments.cr-vote-action-bar > a").attr(
            "href")
        print(name_like1)
        if name_like1 != None:
            name_like1 = "https://www.amazon.de" + name_like1
        name_like2 = doc("#customer_review-R4283VSJX7C6D > div.a-row.review-comments.cr-vote-action-bar > a").attr(
            "href")
        if name_like2 != None:
            name_like2 = "https://www.amazon.de" + name_like2
        name_like3 = doc("#customer_review-R2TB8V88V43PJK > div.a-row.review-comments.cr-vote-action-bar > a").attr(
            "href")
        if name_like3 != None:
            name_like3 = "https://www.amazon.de" + name_like3
        name_like4 = doc("#customer_review-R2TB8V88V43PJK > div.a-row.review-comments.cr-vote-action-bar > a").attr(
            "href")
        if name_like4 != None:
            name_like4 = "https://www.amazon.de" + name_like4

        # 评论人星级
        name_icon1 = doc("#customer_review-R2ALMGHSI4EMD8 > div:nth-child(2) > a:nth-child(1) > i > span").text()
        name_icon2 = doc("#customer_review-R3CTW7AUSY2IKN > div:nth-child(2) > a:nth-child(1) > i > span").text()
        name_icon3 = doc("#customer_review-R3QSLKKNB0WBYE > div:nth-child(2) > a:nth-child(1) > i > span").text()
        name_icon4 = doc("#customer_review-R2X92Z357EPX6 > div:nth-child(2) > a:nth-child(1) > i > span").text()

        # 评论时间
        name_time1 = doc("#customer_review-R2ALMGHSI4EMD8 > span").text()
        name_time2 = doc("#customer_review-R3CTW7AUSY2IKN > span").text()
        name_time3 = doc("#customer_review-R3QSLKKNB0WBYE > span").text()
        name_time4 = doc("#customer_review-R2X92Z357EPX6 > span").text()

        # 评论内容
        name_revie1 = doc("#customer_review-R2ALMGHSI4EMD8 > div.a-row.a-spacing-small.review-data > span > div > div.a-expander-content.reviewText.review-text-content.a-expander-partial-collapse-content > span").text()
        name_revie2 = doc("#customer_review-R3CTW7AUSY2IKN > div.a-row.a-spacing-small.review-data > span > div > div.a-expander-content.reviewText.review-text-content.a-expander-partial-collapse-content > span").text()
        name_revie3 = doc("#customer_review-R3QSLKKNB0WBYE > div.a-row.a-spacing-small.review-data > span > div > div.a-expander-content.reviewText.review-text-content.a-expander-partial-collapse-content > span").text()
        name_revie4 = doc("#customer_review-R2X92Z357EPX6 > div.a-row.a-spacing-small.review-data > span > div > div.a-expander-content.reviewText.review-text-content.a-expander-partial-collapse-content > span").text()


        # 认同人数
        name_emen1 = doc("#customer_review-R2ALMGHSI4EMD8 > div.a-row.review-comments.cr-vote-action-bar > span.cr-vote > div.a-row.a-spacing-small > span").text()
        name_emen2 = doc("#customer_review-R3CTW7AUSY2IKN > div.a-row.review-comments.cr-vote-action-bar > span.cr-vote > div.a-row.a-spacing-small > span").text()
        name_emen3 = doc("#customer_review-R3QSLKKNB0WBYE > div.a-row.review-comments.cr-vote-action-bar > span.cr-vote > div.a-row.a-spacing-small > span").text()
        name_emen4 = doc("#customer_review-R2X92Z357EPX6 > div.a-row.review-comments.cr-vote-action-bar > span.cr-vote > div.a-row.a-spacing-small > span").text()

        product = {
            'price': price,
            'commit': commit,
            'name': name,
            'icon': icon,
            'name_url': name_url,
            'upd': upd,
            'ASIN': ASIN,
            'Bk': Bk,
            'Mr': Mr,
            'name1': name1,
            'name2': name2,
            'name3': name3,
            'name4': name4,
            'name_icon1': name_icon1,
            'name_icon2': name_icon2,
            'name_icon3': name_icon3,
            'name_icon4': name_icon4,
            'name_time1': name_time1,
            'name_time2': name_time2,
            'name_time3': name_time3,
            'name_time4': name_time4,
            'name_revie1': name_revie1,
            'name_revie2': name_revie2,
            'name_revie3': name_revie3,
            'name_revie4': name_revie4,
            'name_emen1': name_emen1,
            'name_emen2': name_emen2,
            'name_emen3': name_emen3,
            'name_emen4': name_emen4,
            'name_like1': name_like1,
            'name_like2': name_like2,
            'name_like3': name_like3,
            'name_like4': name_like4,
        }

        save_to_mongo(product)

    except TimeoutException:
        get_goods()


# 存储mongodb
def save_to_mongo(result):
    print("存储mongodb")
    try:
        if db[MONGO_TABLE].update({"name": result['name'], "price": result['price']}, {"$set": dict(result)}, upsert=True, multi=True):

            print("存储到MONGODB成功", result)
    except Exception:
        print("存储失败", result)


def main():
    get_goods()
    # 关闭浏览器
    browser.quit()


if __name__ == "__main__":
    main()

