from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from pyquery import PyQuery as pq
import xlwt
import time
import xlrd
import copy
from selenium.webdriver.chrome.options import Options


browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
browser.set_window_size(1000, 800)

L = []

def search():
    print("正在搜索")
    try:
        browser.get('https://www.amazon.com/gp/new-releases/home-garden')

        # 点击
        # wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#zg_browseRoot > ul > ul > li:nth-child(1) > a"))).click()

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#zg_browseRoot > ul > ul > li:nth-child(13) > a"))).click()
        # wait.until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "#nav-global-location-slot > span > a"))).click()
        #
        # wait.until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "#GLUXZipUpdateInput"))
        # ).send_keys("10010")
        #
        # wait.until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "#GLUXZipUpdate"))).click()
        #
        # wait.until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, ".a-button-inner"))).click()
        # time.sleep(1)
        #
        # browser.back()

        # 隐式等待
        browser.implicitly_wait(3)

        get_products()

    except TimeoutException:
        return search()


# 翻页
def next_page():
    print("正在翻页")
    try:
        # 确定按钮
        # submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#zg-center-div > div.a-row.a-spacing-top-mini > div > ul > li.a-last")))

        # submit.click()
        # browser.get('https://www.amazon.com/gp/new-releases/home-garden/3206325011/ref=zg_bsnr_pg_2?ie=UTF8&pg=2')
        # browser.get('https://www.amazon.com/gp/new-releases/home-garden/284507/ref=zg_bsnr_pg_2?ie=UTF8&pg=2')
        # browser.get('https://www.amazon.com/gp/new-releases/home-garden/1063252/ref=zg_bsnr_pg_2?ie=UTF8&pg=2')
        # browser.get('https://www.amazon.com/gp/new-releases/home-garden/1063236/ref=zg_bsnr_pg_2?ie=UTF8&pg=2')
        # browser.get('https://www.amazon.com/gp/new-releases/home-garden/1063306/ref=zg_bsnr_pg_2?ie=UTF8&pg=2')
        # browser.get('https://www.amazon.com/gp/new-releases/home-garden/1063278/ref=zg_bsnr_pg_2?ie=UTF8&pg=2')
        # browser.get('https://www.amazon.com/gp/new-releases/home-garden/3736081/ref=zg_bsnr_pg_2?ie=UTF8&pg=2')
        # browser.get('https://www.amazon.com/gp/new-releases/home-garden/13679381/ref=zg_bsnr_pg_2?ie=UTF8&pg=2')
        # browser.get('https://www.amazon.com/gp/new-releases/home-garden/3206324011/ref=zg_bsnr_pg_2?ie=UTF8&pg=2')
        # browser.get('https://www.amazon.com/gp/new-releases/home-garden/510240/ref=zg_bsnr_pg_2?ie=UTF8&pg=2')
        # browser.get('https://www.amazon.com/gp/new-releases/home-garden/510106/ref=zg_bsnr_pg_2?ie=UTF8&pg=2')
        # browser.get('https://www.amazon.com/gp/new-releases/home-garden/3610841/ref=zg_bsnr_pg_2?ie=UTF8&pg=2')
        browser.get('https://www.amazon.com/gp/new-releases/home-garden/10802561/ref=zg_bsnr_pg_2?ie=UTF8&pg=2')


        # 滚动条滚动到底部
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)", "")

        get_products()
    except TimeoutException:
        # 如果失败则重新请求
        next_page()

# 获取商品列表页面信息
def get_products():
    print("商品列表页面信息")
    # 最外层的div包括所有的商品
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#zg-ordered-list')))
    # 获取网页源代码
    html = browser.page_source

    # 解析网页代码
    # 声明pq对象
    doc = pq(browser.page_source, parser="html")
    items = doc('#zg-ordered-list .zg-item-immersion').items()

    page = doc('#zg-center-div > div.a-row.a-spacing-top-mini > div > ul > li.a-selected').text()
    page = int(page)

    a = (page - 1)*50
    for item in items:
        a += 1
        # 商品价格
        price = item.find(".p13n-sc-price").text()
        # 商品总评价数量
        commit = item.find(".a-size-small.a-link-normal").text()
        if commit == "":
            commit = 0
        # 评价星级
        icon = item.find(".a-icon-alt").text()
        icon = icon[0:4]
        if icon == "":
            icon = "0"

        # 商品名称
        name = item.find(".p13n-sc-truncated").attr('title')
        if name == None:
            name = item.find(".p13n-sc-truncated").text()

        # 商品url
        name_url = item.find(".a-link-normal").attr('href')
        if name_url:
            name_url = "https://www.amazon.com" + name_url

        product = {
            'price': price,
            'commit': commit,
            'name': name,
            'icon': icon,
            'name_url': name_url,
        }

        print('爬取第', a, '个')

        g = get_goods(product)
        L.append(g)
        # print(L, len(L))

        if len(L) == 100:
            save_to_excel(L)

# 获取商品详情页信息
def get_goods(product):
    print("进入商品详情页")
    browser.get(product['name_url'])
    # 隐式等待
    browser.implicitly_wait(5)
    doc = pq(browser.page_source, parser="html")

    # ASIN码
    ASIN = doc('#prodDetails > div > div.column.col2 > div:nth-child(1) > div.content.pdClearfix > div > div > table > tbody > tr:nth-child(1) > td.value').text()
    if ASIN == "" and len(ASIN) != 10:
        ASIN = doc('#productDetails_detailBullets_sections1 > tbody > tr:nth-child(5) > td').text()
        if ASIN == "" and len(ASIN) != 10:
            ASIN = doc('#detail-bullets > table > tbody > tr > td > div > ul > li:nth-child(2) > td').text()
            if ASIN == "" and len(ASIN) != 10:
                ASIN = doc('#productDetails_detailBullets_sections1 > tbody > tr:nth-child(4) > td').text()

    # 排行
    BestSellersRank = doc("#productDetails_detailBullets_sections1 > tbody > tr:nth-child(11) > td").text()
    if BestSellersRank == "":
        BestSellersRank = doc("#productDetails_detailBullets_sections1 > tbody > tr:nth-child(9) > td").text()
        if BestSellersRank == "":
            BestSellersRank = doc("#productDetails_detailBullets_sections1 > tbody > tr:nth-child(8) > td").text()
            if BestSellersRank == "":
                BestSellersRank = doc("#SalesRank > td.value").text()
                if BestSellersRank == "":
                    BestSellersRank = doc("#productDetails_detailBullets_sections1 > tbody > tr:nth-child(7) > td").text()
                    if BestSellersRank == "":
                        BestSellersRank = doc("#SalesRank").text()

    if BestSellersRank[0:4] == '/* *':
        BestSellersRank1 = ""
        BestSellersRank2 = ""

    if BestSellersRank[0:4] != '/* *':

        BestSellersRank = BestSellersRank.split('\n')
        BestSellersRank1 = BestSellersRank[0:1]
        for i in BestSellersRank1:
            BestSellersRank1 = i.split('(')[0:1]

        BestSellersRank2 = BestSellersRank[1:]
        BestSellersRank2 = ''.join(BestSellersRank2)
        BestSellersRank2 = BestSellersRank2.split('#')

        if len(BestSellersRank2) >= 3:
            BestSellersRank2 = BestSellersRank2[-2:]
            # BestSellersRank2 = ''.join(BestSellersRank2)

        if len(BestSellersRank2) < 3:
            BestSellersRank2 = BestSellersRank2[-1:]

    BestSellersRank2 = ''.join(BestSellersRank2)
    BestSellersRank1 = ''.join(BestSellersRank1)

    # 起价
    Manufacturer = doc("#olp-upd-new").text()
    upd = doc("#acrCustomerReviewText").text()

    # 包装尺寸
    PackageDimensions = doc("#productDetails_detailBullets_sections1 > tbody > tr:nth-child(1) > td").text()
    if PackageDimensions == "":
        PackageDimensions = doc("#prodDetails > div.wrapper.USlocale > div.column.col1 > div > div.content.pdClearfix > div > div > table > tbody > tr:nth-child(2) > td.value").text()

    # 重量
    ItemWeight = doc("#productDetails_techSpec_section_1 > tbody > tr:nth-child(1) > td").text()
    if ItemWeight == "":
        ItemWeight = doc("#prodDetails > div.wrapper.USlocale > div.column.col1 > div > div.content.pdClearfix > div > div > table > tbody > tr:nth-child(1) > td.value").text()
        if ItemWeight == "":
            ItemWeight = doc("#productDetails_detailBullets_sections1 > tbody > tr:nth-child(2) > td").text()

    # 加入字典中
    product['ASIN'] = ASIN
    product['BestSellersRank1'] = BestSellersRank1
    product['BestSellersRank2'] = BestSellersRank2
    product['PackageDimensions'] = PackageDimensions
    product['ItemWeight'] = ItemWeight
    product['Manufacturer'] = Manufacturer
    product['upd'] = upd
    print("============")
    print(product)
    return product

# 存储Excel
def save_to_excel(L):
    print("存储Excel")
    try:
        # 创建工作workbook
        workbook = xlwt.Workbook(encoding="utf-8")

        # 创建工作表worksheet,填入表名
        worksheet = workbook.add_sheet('sheet1')

        worksheet.write(0, 0, '商品名称')
        worksheet.write(0, 1, '商品价格')
        worksheet.write(0, 2, '评价数量')
        worksheet.write(0, 3, '评价星级')
        worksheet.write(0, 4, '商品url')
        worksheet.write(0, 5, 'ASIN码')
        worksheet.write(0, 6, '排行1')
        worksheet.write(0, 7, '排行2')
        worksheet.write(0, 8, '店家名称')
        worksheet.write(0, 9, '包装尺寸')
        worksheet.write(0, 10, '重量')
        worksheet.write(0, 11, '起价')

        # 在表中写入相应的数据
        for a in range(len(L)):
            product = L[a]
            c = 0
            a += 1
            # 1,0
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, product['name'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, product['price'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, product['commit'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, product['icon'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, product['name_url'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, product['ASIN'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, product['BestSellersRank1'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, product['BestSellersRank2'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, product['Manufacturer'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, product['PackageDimensions'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, product['ItemWeight'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, product['upd'])

            # 保存表
            # workbook.save('home-garden.xls')
            # workbook.save('KitchenDining.xls')
            # workbook.save('Bedding.xls')
            # workbook.save('Bath.xls')
            # workbook.save('Furniture.xls')
            # workbook.save('HomeDécor.xls')
            # workbook.save('WallDécor.xls')
            # workbook.save('SeasonalDécor.xls')
            # workbook.save('Heating,CoolingQuality.xls')
            # workbook.save('IronsSteamers.xls')
            # workbook.save('VacuumsFloorCare.xls')
            # workbook.save('StorageOrganization.xls')
            workbook.save('Cleaning Supplies.xls')
            print("存储Excel成功", a)

    except Exception:
        print("存储Excel失败")


def main():
    search()
    for i in range(1, 2):
        next_page()
    # 关闭浏览器
    browser.quit()


if __name__ == "__main__":
    main()



