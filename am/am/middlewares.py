# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html


from fake_useragent import UserAgent
from scrapy import signals


#随机更换user_agent
class RandomUserAgentMiddlware(object):
    def __init__(self, crawler):
        super(RandomUserAgentMiddlware, self).__init__()
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get("RANDOM_UA_TYPE", "random")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        def get_ua():
            return getattr(self.ua, self.ua_type)
        print(get_ua())
        request.headers.setdefault('User-Agent', get_ua())



# 集成selenium
from scrapy.http import HtmlResponse
from selenium.common.exceptions import TimeoutException
import time


class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        if spider.name == 'amazon_goods':
            try:
                spider.browser.get(request.url)
                spider.browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            except TimeoutException as e:
                print('超时', e)
                spider.browser.execute_script('window.stop()')
            time.sleep(2)
            return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source,
                                encoding="utf-8", request=request)