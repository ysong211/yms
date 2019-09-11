# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmItem(scrapy.Item):
    # define the fields for your item here like:
    # 商品名称
    name = scrapy.Field()
    # 商品价格
    price = scrapy.Field()
    # 商品url
    name_url = scrapy.Field()
    # 星级数
    icon = scrapy.Field()
    # 评价数量
    evaluate = scrapy.Field()
    # ASIN码
    asin = scrapy.Field()
    # 排名
    ranking = scrapy.Field()
    # 店家名称
    shop = scrapy.Field()
    # 包装尺寸
    size = scrapy.Field()
    # 重量
    weight = scrapy.Field()


