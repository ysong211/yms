# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
from am.items import AmItem
from copy import deepcopy
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait


class AmazonGoodsSpider(scrapy.Spider):
    name = 'amazon_goods'
    allowed_domains = ['https://www.amazon.com/']

    def __init__(self):
        self.browser = webdriver.Chrome()
        # WebDriverWait(self.browser, 10)
        self.browser.set_page_load_timeout(30)

    def closed(self, spider):
        print("spider closed")
        self.browser.close()

    def start_requests(self):
        start_urls = []
        keyword = ['3206325011', '284507', '1063252', '1063236', '1063306', '1063278', '3736081', '13679381', '3206324011',
                   '510240', '510106', '3610841', '10802561']

        for kw in keyword:
            for pg in range(1, 2):
                # 转换格式
                pg = str(pg)
                next_page_url = 'https://www.amazon.com/gp/new-releases/home-garden/' + kw + '/ref=zg_bsnr_pg_' + pg + '?ie=UTF8&pg=' + pg
                start_urls.append(next_page_url)
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        goods = response.css('.zg-item-immersion')
        for good in goods:
            item = AmItem()

            # 商品价格
            price = good.css('.p13n-sc-price::text').extract()
            price = ''.join(price)

            # 商品url
            name_url = good.css('.a-link-normal::attr(href)').extract_first()
            if name_url != "":
                name_url = "https://www.amazon.com" + name_url

            # 星级数
            icon = good.css('.a-icon-alt::text').extract()
            if icon == "":
                icon = "0"
            else:
                icon = ''.join(icon)[0:3]

            # 评价数量
            evaluate = good.css('.a-size-small.a-link-normal::text').extract()

            if evaluate == "":
                evaluate = 0
            else:
                evaluate = ''.join(evaluate)

            item['price'] = price
            item['name_url'] = name_url
            item['icon'] = icon
            item['evaluate'] = evaluate

            yield scrapy.Request(
                url=item['name_url'],
                callback=self.good_temp,
                meta={'item': deepcopy(item)},
                dont_filter=True,
            )

    # 商品详情页
    def good_temp(self, response):
        # time.sleep(1)
        item = response.meta['item']

        # 产品名称
        name = response.css('#productTitle::text').extract()
        name = ''.join(name)
        name = ' '.join(name.split())

        # 店名
        shop = response.css('#bylineInfo::text').extract()
        shop = ''.join(shop)

        # 类似比较
        upd = response.css('#olp-upd-new-used-freeshipping-threshold::text').extract()

        print(upd)

        text = response.css('#productDetails_detailBullets_sections1::text').extract()

        print(text)

        # print(item)
        print("================")

        # yield item

