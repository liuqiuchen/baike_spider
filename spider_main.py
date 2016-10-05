# coding:utf8
from baike_spider import url_manager, html_downloader, html_parser,\
    html_outputer

class SpiderMain(object):
    # 构造函数
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    def craw(self, root_url):
        pass
    
    


# 编写main函数
if __name__ == "__main_":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain() # Ctrl + 1 是create class
    obj_spider.craw(root_url) # Ctrl + 1 是create method









