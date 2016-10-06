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
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                
                if count == 1000:
                    break
                
                count = count + 1
            except:
                print 'craw failed'
            
        self.outputer.output_html()

# 编写main函数
if __name__ == "__main_":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain() # Ctrl + 1 是create class
    obj_spider.craw(root_url) # Ctrl + 1 是create method









