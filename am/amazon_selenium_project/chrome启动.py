import selenium
from selenium import webdriver


class chrome(object):
    def __init__(self):
        chrome_option = webdriver.ChromeOptions()
        # 设置代理
        chrome_option.add_argument("--proxy-server=http://125.123.18.114:4226")
        # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://125.123.18.114:4226

        self.driver = webdriver.Chrome(chrome_options=chrome_option)
        self.driver.set_window_size(1440, 900)

    def open_url(self):

        url = 'http://httpbin.org/ip'
        self.driver.get(url)
        print(self.driver.page_source)

        self.driver.quit()


if __name__ == '__main__':
    c = chrome()
    c.open_url()



