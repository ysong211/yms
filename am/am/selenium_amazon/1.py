# d = ['婴儿用品商品里排第41名', '(查看婴儿用品商品销售排行榜)\n.zg_hrsr', '{', 'margin:', '0;', 'padding:', '0;', 'list-style-type:', 'none;',
#      '}', '.zg_hrsr_item', '{', 'margin:', '0', '0', '0', '10px;', '}', '.zg_hrsr_rank', '{', 'display:',
#      'inline-block;', 'width:', '80px;', 'text-align:', 'right;', '}\n第1位', '-\xa0婴儿包被']


#
# d1 = ['婴儿用品商品里排第43名', '(查看婴儿用品商品销售排行榜)\n.zg_hrsr']
# d2 = (str(i) for i in d1)
# print("".join(d2))
#



# ls1 = ['a', 1, 'b', 2]
# ls2 = [str(i) for i in ls1]
# ['a', '1', 'b', '2']
# ls3 = ''.join(ls2)


#
# import xlwt
#
# # 创建工作workbook
# workbook = xlwt.Workbook()
#
# # 创建工作表worksheet,填入表名
# worksheet = workbook.add_sheet('表名')
#
# worksheet.write(0, 0, '商品名称')
# worksheet.write(0, 1, '商品价格')
# worksheet.write(0, 2, '评价数量')
# worksheet.write(0, 3, '评价星级')
# worksheet.write(0, 4, '商品url')
# worksheet.write(0, 5, 'ASIN码')
# worksheet.write(0, 6, '排行')
# worksheet.write(0, 7, '店家名称')
# worksheet.write(0, 8, '包装尺寸')
# worksheet.write(0, 9, '重量')
#
# j = [{'price': '$11129.95', 'commit': '2,421', 'name': 'Love To Dream Swaddle UP, Dramatically Better Sleep, Allow Baby to Sleep in Their Preferred arms up Position for self-Soothing', 'icon': '4.3 out of 5 stars', 'name_url': 'https://www.amazon.com/Love-Dream-Swaddle-Original-13-18-5/dp/B005MATQNK/ref=zg_bsnr_3206325011_1?_encoding=UTF8&psc=1&refRID=G21Z82JHF5R0Y20YYMCN', 'ASIN': 'B005MATQNK', 'BestSellersRank': '#38in', 'PackageDimensions': '4.8 ounces', 'ItemWeight': '[<td.value>]','Manufacturer': 'Love to Dream', 'reviews': '2,421 customer reviews'}
# ,{'price': '$29222.95', 'commit': '2,421', 'name': 'Love To Dream Swaddle UP, Dramatically Better Sleep, Allow Baby to Sleep in Their Preferred arms up Position for self-Soothing', 'icon': '4.3 out of 5 stars', 'name_url': 'https://www.amazon.com/Love-Dream-Swaddle-Original-13-18-5/dp/B005MATQNK/ref=zg_bsnr_3206325011_1?_encoding=UTF8&psc=1&refRID=G21Z82JHF5R0Y20YYMCN', 'ASIN': 'B005MATQNK', 'BestSellersRank': '#38in', 'PackageDimensions': '4.8 ounces', 'ItemWeight': '[<td.value>]','Manufacturer': 'Love to Dream', 'reviews': '2,421 customer reviews'}
# ,{'price': '$29.95', 'commit': '2,421', 'name': 'Love To Dream Swaddle UP, Dramatically Better Sleep, Allow Baby to Sleep in Their Preferred arms up Position for self-Soothing', 'icon': '4.3 out of 5 stars', 'name_url': 'https://www.amazon.com/Love-Dream-Swaddle-Original-13-18-5/dp/B005MATQNK/ref=zg_bsnr_3206325011_1?_encoding=UTF8&psc=1&refRID=G21Z82JHF5R0Y20YYMCN', 'ASIN': 'B005MATQNK', 'BestSellersRank': '#38in', 'PackageDimensions': '4.8 ounces', 'ItemWeight': '[<td.value>]','Manufacturer': 'Love to Dream', 'reviews': '2,421 customer reviews'}
# ]
#
# for a in range(len(j)):
#     # print(a)
#     c = 0
#     d = j[a]
#     print(d)
#
#     # 在表中写入相应的数据
#     worksheet.col(c).width = 256 * 30
#     # 1,0
#     a += 1
#     print(a)
#     worksheet.write(a,c,d['name'])
#     worksheet.col(c).width = 256 * 30
#     c += 1
#     # print(a)
#     worksheet.write(a,c,d['price'])
#     worksheet.col(c).width = 256 * 30
#     c += 1
#     worksheet.write(a,c,d['commit'])
#     worksheet.col(c).width = 256 * 30
#     c += 1
#     worksheet.write(a,c,d['icon'])
#     worksheet.col(c).width = 256 * 30
#     c += 1
#     worksheet.write(a,c,d['name_url'])
#     worksheet.col(c).width = 256 * 30
#     c += 1
#     worksheet.write(a,c,d['ASIN'])
#     worksheet.col(c).width = 256 * 30
#     c += 1
#     worksheet.write(a,c,d['BestSellersRank'])
#     worksheet.col(c).width = 256 * 30
#     c += 1
#     worksheet.write(a,c,d['Manufacturer'])
#     worksheet.col(c).width = 256 * 30
#     c += 1
#     worksheet.write(a,c,d['PackageDimensions'])
#     worksheet.col(c).width = 256 * 30
#     c += 1
#     worksheet.write(a,c,d['ItemWeight'])
#     worksheet.col(c).width = 256 * 30
#
#
# #
# # 保存表
#
#     workbook.save('2q11111q21.xls')
#

# d = {'price': '$29.95', 'commit': '2,421', 'name': 'Love To Dream Swaddle UP, Dramatically Better Sleep, Allow Baby to Sleep in Their Preferred arms up Position for self-Soothing', 'icon': '4.3 out of 5 stars', 'name_url': 'https://www.amazon.com/Love-Dream-Swaddle-Original-13-18-5/dp/B005MATQNK/ref=zg_bsnr_3206325011_1?_encoding=UTF8&psc=1&refRID=G21Z82JHF5R0Y20YYMCN', 'ASIN': 'B005MATQNK', 'BestSellersRank': '#38in', 'PackageDimensions': '4.8 ounces', 'ItemWeight': '[<td.value>]','Manufacturer': 'Love to Dream', 'reviews': '2,421 customer reviews'}


#
# j = [{'price': '$11129.95', 'commit': '2,421', 'name': 'Love To Dream Swaddle UP, Dramatically Better Sleep, Allow Baby to Sleep in Their Preferred arms up Position for self-Soothing', 'icon': '4.3 out of 5 stars', 'name_url': 'https://www.amazon.com/Love-Dream-Swaddle-Original-13-18-5/dp/B005MATQNK/ref=zg_bsnr_3206325011_1?_encoding=UTF8&psc=1&refRID=G21Z82JHF5R0Y20YYMCN', 'ASIN': 'B005MATQNK', 'BestSellersRank': '#38in', 'PackageDimensions': '4.8 ounces', 'ItemWeight': '[<td.value>]','Manufacturer': 'Love to Dream', 'reviews': '2,421 customer reviews'}
# ,{'price': '$29222.95', 'commit': '2,421', 'name': 'Love To Dream Swaddle UP, Dramatically Better Sleep, Allow Baby to Sleep in Their Preferred arms up Position for self-Soothing', 'icon': '4.3 out of 5 stars', 'name_url': 'https://www.amazon.com/Love-Dream-Swaddle-Original-13-18-5/dp/B005MATQNK/ref=zg_bsnr_3206325011_1?_encoding=UTF8&psc=1&refRID=G21Z82JHF5R0Y20YYMCN', 'ASIN': 'B005MATQNK', 'BestSellersRank': '#38in', 'PackageDimensions': '4.8 ounces', 'ItemWeight': '[<td.value>]','Manufacturer': 'Love to Dream', 'reviews': '2,421 customer reviews'}
# ,{'price': '$29.95', 'commit': '2,421', 'name': 'Love To Dream Swaddle UP, Dramatically Better Sleep, Allow Baby to Sleep in Their Preferred arms up Position for self-Soothing', 'icon': '4.3 out of 5 stars', 'name_url': 'https://www.amazon.com/Love-Dream-Swaddle-Original-13-18-5/dp/B005MATQNK/ref=zg_bsnr_3206325011_1?_encoding=UTF8&psc=1&refRID=G21Z82JHF5R0Y20YYMCN', 'ASIN': 'B005MATQNK', 'BestSellersRank': '#38in', 'PackageDimensions': '4.8 ounces', 'ItemWeight': '[<td.value>]','Manufacturer': 'Love to Dream', 'reviews': '2,421 customer reviews'}
# ]
#
#
# l = len(j)
# print(l)
# for i in range(l):
#     print(i)
#     print(j[i])
#
# {'price': '$8.49', 'commit': '511', 'name': 'Flamingo P Memory Foam Luxury Bath Rugs Anti-Slip Striped Pattern One Pack', 'icon': '4.3 out of 5 stars', 'name_url': 'https://www.amazon.com/Non-Slip-Bathroom-Absorbent-Comfortable-Stylish/dp/B07R4X9RGZ/ref=zg_bsnr_3206325011_15?_encoding=UTF8&psc=1&refRID=YW06SJ6A6XMJ3BGPKDWS', 'ASIN': 'B07R4X9RGZ', 'BestSellersRank': "#4,772 in Home & Kitchen (See Top 100 in Home & Kitchen)\n#2 in Kids' Bath Rugs\n#25 in Bath Rugs", 'PackageDimensions': '16.8 x 11.8 x 1.4 inches', 'ItemWeight': [], 'Manufacturer': 'Flamingo P'}
#
#
#
# {'price': '$28.99', 'commit': '3,225', 'name': 'BreathableBaby Classic Breathable Mesh Crib Liner - White', 'icon': '4.3 out of 5 stars', 'name_url': 'https://www.amazon.com/Breathable-Endorsed-Prevents-Getting-Slatted/dp/B0013FGWD0/ref=zg_bsnr_3206325011_16?_encoding=UTF8&psc=1&refRID=YW06SJ6A6XMJ3BGPKDWS', 'ASIN': 'B0013FGWD0', 'BestSellersRank': '#769 in Baby (See Top 100 in Baby)\n.zg_hrsr { margin: 0; padding: 0; list-style-type: none; } .zg_hrsr_item { margin: 0 0 0 10px; } .zg_hrsr_rank { display: inline-block; width: 80px; text-align: right; }\n#2 in\xa0Crib Bedding Bumpers', 'PackageDimensions': '111 x 11 inches', 'ItemWeight':'[<td.value>]' , 'Manufacturer': 'BreathableBaby'}
#
#
# s = 'B01MTA00AX'
# print(len(s))
# https://www.amazon.com/gp/new-releases/home-garden/3206325011/ref=zg_bsnr_pg_2?ie=UTF8&pg=2

from urllib.parse import urlencode

# start_urls = []
# keyword = ['3206325011', '284507', '1063252', '1063236', '1063306', '1063278', '3736081', '13679381', '3206324011',
#            '510240', '510106', '3610841', '10802561']
# for kw in keyword:
#     for pg in range(1, 2):
#         # 转换格式
#         pg = str(pg)
#         next_page_url = 'https://www.amazon.com/gp/new-releases/home-garden/' + kw  + '/ref=zg_bsnr_pg_' + pg + '?ie=UTF8&pg=' + pg
#         start_urls.append(next_page_url)
#
#
# print(start_urls)
# print(len(start_urls))


from selenium import webdriver



#!/usr/bin/env python
# -*- coding:utf8 -*-

import redis
import requests
from selenium.webdriver.support.ui import WebDriverWait
#
# '''
# 这种连接是连接一次就断了，耗资源.端口默认6379，就不用写
# r = redis.Redis(host='127.0.0.1')
# # r.set('name', 'hhqwqwh1')
# r.sadd('na2me', 'hhh1')
# r.sadd('nam2e', '22h2hh')


# print(r.get('name').decode('utf8'))
# # '''
# '''
# 连接池：
# 当程序创建数据源实例时，系统会一次性创建多个数据库连接，并把这些数据库连接保存在连接池中，当程序需要进行数据库访问时，
# 无需重新新建数据库连接，而是从连接池中取出一个空闲的数据库连接
# '''
# # pool = redis.ConnectionPool(host='127.0.0.1')   #实现一个连接池
# pool = redis.ConnectionPool(host='192.168.5.5')   #实现一个连接池
# ip_pool = redis.Redis(connection_pool=pool)
# a =0
# while True:
#     a += 1
#     l = ip_pool.srandmember('china_ip', 1)
#     # l = ip_pool.spop('ip1', 1)
#     print(ip_pool.scard('ip1'))
#
#     for i in l:
#         j = eval(i.decode())
#         ip = j['ip']+":"+j['port']
#         print(ip)
#
#         import re
#         import requests
#
#         url = "www.baidu.com"
#
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
#         }
#         proxies = {
#             "https": "https://" + 'ip'
#         }
#         response = requests.get(url, headers=headers, proxies=proxies).content.decode()
#
#         print(requests.status_codes)
#

import random
chromeOptions = webdriver.ChromeOptions()

username = 'lum-customer-wanjie-zone-residential'
password = 'uhnw28g6qtk7'
port = 22225
session_id = random.random()
super_proxy_url = ('http://%s-dns-local-session-%s:%s@servercountry-US.zproxy.lum-superproxy.io:%d' %(username, session_id, password, port))

# 设置代理
# chromeOptions.add_argument("--proxy-server=http://202.20.16.82:10152")
# chromeOptions.add_argument("--proxy-server=http://" + super_proxy_url)

# 设置UA
chromeOptions.add_argument('User-Agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')

# 设置无头浏览器
# chromeOptions.add_argument("--headless")

# 设置默认编码为 utf-8
chromeOptions.add_argument('lang=zh_CN.UTF-8')

# print(a)
browser = webdriver.Chrome(options=chromeOptions)
# browser = webdriver.Chrome()
# 打开指定网页
try:
    browser.get("https:www.amazon.com")
except Exception as e:
    print(e)

# 显示等待
wait = WebDriverWait(browser, 10)

# 退出，清除浏览器缓存
browser.quit()

#
# username = 'lum-customer-wanjie-zone-residential'
# password = 'uhnw28g6qtk7'
# port = 22225
# session_id = random.random()
# super_proxy_url = ('http://%s-dns-local-session-%s:%s@servercountry-US.zproxy.lum-superproxy.io:%d' %
# (username, session_id, password, port))
# proxy_handler = urllib.request.ProxyHandler({
# 'http': super_proxy_url,
# 'https': super_proxy_url,
# })
# print(proxy_handler)
# opener = urllib.request.build_opener(proxy_handler)
# print(opener)
# opener.addheaders = \
# [('User-Agent', 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0')]
# print('Performing request')
# print(opener.open('http://lumtest.com/myip.json').read())





#
# def checkip(ip_port):
#     ip_port = eval(ip_port)
#     ip = ip_port['ip']
#     port = ip_port['port']
#     proxies = {"http": "http://"+ ip + ':' + port, "https": "https://"+ ip + ':' + port} # 代理ip
#     print(proxies)
#     try:
#     response=requests.get(url=url,proxies=proxies,headers=headers,timeout=20)
#     print(response.status_code)
#     response = response.status_code
#     print(type(response))
#     if response == 200 :
#     return ip_port
#     else:
#     return False
#     except:
#     return False


#
# s = ['\n                \n                    \n                    \n                \n\n                \n                    \n                    \nleadtimes 双人床 / 双人床 / 大号双人床花卉轻质印花图案超细纤维羽绒被罩，柔软床上用品套装2个枕头套和1个羽绒被套, 微纤维, 两个\n                    \n\n\n                \n                    \n                    \n                \n            ']
#
# s = ''.join(s)
# s = s.split()
# print(s)
# s = ' '.join(s)
# # s = s[1:]
# print(s)

import json

#
#BestSellersRank = '#101 in Home & Kitchen (See Top 100 in Home & Kitchen)\n#1 in Commercial Wet Mops\n#4 in Household Mops, Buckets & Accessories'

#BestSellersRank = "Amazon Best Sellers Rank: #126 in Health & Household (See Top 100 in Health & Household)\n.zg_hrsr { margin: 0; padding: 0; list-style-type: none; } .zg_hrsr_item { margin: 0 0 0 10px; } .zg_hrsr_rank { display: inline-block; width: 80px; text-align: right; }\n#53 in\xa0Sales & Deals\n#2 in\xa0Commercial Bathroom Cleaners\n#3 in\xa0Household Toilet Cleaners', 'PackageDimensions'"

#BestSellersRank = '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }\n4.4 out of 5 stars 5,299 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });\n\n4.4 out of 5 stars'


# if BestSellersRank[0:4] == '/* *':
#     BestSellersRank1 = ""
#     BestSellersRank2 = ""
#
# if BestSellersRank[0:4] != '/* *':
#
#     BestSellersRank = BestSellersRank.split('\n')
#     BestSellersRank1 = BestSellersRank[0:1]
#     for i in BestSellersRank1:
#         BestSellersRank1 = i.split('(')[0:1]
#         BestSellersRank1 = ''.join(BestSellersRank1)
#
#     BestSellersRank2 = BestSellersRank[1:]
#     BestSellersRank2 = ''.join(BestSellersRank2)
#     BestSellersRank2 = BestSellersRank2.split('#')
#
#     if len(BestSellersRank2) >= 3:
#         BestSellersRank2 = BestSellersRank2[-2:]
#         BestSellersRank2 = ''.join(BestSellersRank2)
#
#     if len(BestSellersRank2) < 3:
#         BestSellersRank2 = BestSellersRank2[-1:]
#         BestSellersRank2 = ''.join(BestSellersRank2)
#
# print("--------------")
# print(BestSellersRank1)
# print(BestSellersRank2)



# s1 = s.split("\n")
# print(s1)
# print(s1)
# print("==========")
# print(s1[0:1])
# s2 = s1[1:]
# print(s2)
#
# print(''.join(s2))
# s2 = s1[0:1]
# for i in s2:
#     i1 = i.split('(')[0:1]
#     for j in i1:
#         pass



# s = '.zg_hrsr { margin: 0; padding: 0; list-style-type: none; } .zg_hrsr_item { margin: 0 0 0 10px; } .zg_hrsr_rank { display: inline-block; width: 80px; text-align: right; }#555 in Sales & Deals#7 in Household Cleaning Sponges'
#
# s1 = s.split('#')
# print(s1[-2:])

# s = " "
# for i in s:
#     print(i, 'dd')

# s = 'New (1) from $19.90 & FREE shipping on orders over $25.00. Details'
# print(s[:-9])



# title = doc("#detail-bullets > table > tbody > tr > td > div.content > ul").text()
# if title == "":
#     title = doc("#productDetails_techSpec_section_1 > tbody").text()
#     if title == "":
#         title = doc("#productDetails_detailBullets_sections1 > tbody").text()
#         if title == "":
#             title = doc("#prodDetails > div").text()
#             if title == "":
#                 title = doc("#prodDetails > div.wrapper.USlocale").text()
#                 if title == "":
#                     title = doc("#detailBulletsWrapper_feature_div").text()
#
# print(title.split('\n'))

#
# for i in a33:
#     print(len(i))


# s = 'Product Dimensions: 2.4 x 4.2 x 10.4 inches ; 1.4 pounds'
# print(len(s))
# print(s[20:])

#
# s = {'name': 'O-Cedar EasyWring Microfiber Spin Mop, Bucket Floor Cleaning System', 'price': '$29.98', 'ASIN': 'B00WSWGVZQ', 'BestSellersRank1': '#102 in Home & Kitchen ', 'BestSellersRank2': '1 in Household Floor Cleaners', 'ItemWeight': '5.2 pounds', 'Manufacturer': 'O-Cedar', 'PackageDimensions': '19.5 x 11.7 x 11.5 inches', 'commit': '7,022', 'icon': '4.3 ', 'name_url': 'https://www.amazon.com/Cedar-EasyWring-Microfiber-Bucket-Cleaning/dp/B00WSWGVZQ/ref=zg_bsnr_10802561_1?_encoding=UTF8&psc=1&refRID=S7RYJQE4EAXQFPF0ZDE7', 'upd': 'New (3) from $29.98 & FREE shipping'}
# print(s['name'])


# l = ['Amazon Bestsellers Rank:', '.zg_hrsr { margin: 0; padding: 0; list-style-type: none; } .zg_hrsr_item { margin: 0 0 0 10px; } .zg_hrsr_rank { display: inline-block; width: 80px; text-align: right; }', '#6 in\xa0Wireless Headphones', '#5 in\xa0Mobile Phone Bluetooth Headsets']
#
# print(l[2:])

# l = "'PackageDimensions': '2 x 1 x 1 cm ; 118 g'"
# # print(l[20:])
#
# for i in range(1, 5):
#     print(i)
























