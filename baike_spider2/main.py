# coding=utf8

import urllib2
from bs4 import BeautifulSoup
import re
import urlparse

def downloader(url):
    response = urllib2.urlopen(url)
    
    if response.getcode() != 200:
        return None
    
    return response.read()


def html_parser(url, html_cont):
    datas = {}
    
    soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
    datas['url'] = url
    datas['title'] = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1').get_text()
    datas['summary'] = soup.find('div', class_='lemma-summary').get_text()
    
    return datas

def out_html(url, data):
    fout = open('output.html', 'w')
    
    fout.write("<html>")
    fout.write("<head>")
    fout.write("<meta charset='utf-8' />")
    fout.write("</head>")
    fout.write("<body>")
    fout.write("<table>")
    
    fout.write("<td>%s</td>" % data['title'].encode('utf-8')) 
    fout.write("<td>%s</td>" % data['url'].encode('utf-8'))
    fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
        
    fout.write("</table>")
    fout.write("</body>")
    fout.write("</html>")
    
    fout.close()
    
def get_new_urls(html_cont):
    soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
    links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
    new_urls = set()
    new_url_list = []
    count = 0;
    for link in links:
        count = count + 1
        
        if count < 10:
            new_url = link['href']
            new_full_url = urlparse.urljoin('http://baike.baidu.com', new_url)
            new_urls.add(new_full_url)
            new_url_list.append(new_urls.pop()) 
   
    print list(set(new_url_list)) # 列表去重
    
    return list(set(new_url_list))    

# 下载网页，入口网址
root_url = "http://baike.baidu.com/view/21087.htm"

html_cont = downloader(root_url)
datas = html_parser(root_url, html_cont)
out_html(root_url, datas)

get_new_urls(html_cont)


