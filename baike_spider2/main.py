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

def out_html(root_url, root_data, datas):
    fout = open('output.html', 'w')
    
    fout.write("<html>")
    fout.write("<head>")
    fout.write("<meta charset='utf-8' />")
    fout.write("</head>")
    fout.write("<body>")
    fout.write("<table>")
    
    fout.write("<tr>")
    fout.write("<td>%s</td>" % root_data['title'].encode('utf-8')) 
    fout.write("<td>%s</td>" % root_url.encode('utf-8'))
    fout.write("<td>%s</td>" % root_data['summary'].encode('utf-8'))
    fout.write("</tr>")
    
    for data in datas:
        fout.write("<tr>")
        fout.write("<td>%s</td>" % data['title'].encode('utf-8')) 
        fout.write("<td>%s</td>" % data['url'].encode('utf-8'))
        fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
        fout.write("</tr>")
        
    fout.write("</table>")
    fout.write("</body>")
    fout.write("</html>")
    
    fout.close()
    
def get_new_urls(html_cont):
    try:
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        new_urls = set()
        new_url_list = []
        count = 0;
        if len(links) >= 10: 
            for link in links:
                
                if count < 10: # 抓取10个url上的数据
                    new_url = link['href']
                    new_full_url = urlparse.urljoin('http://baike.baidu.com', new_url)
                    new_urls.add(new_full_url)
                    new_url_list.append(new_urls.pop())
                    
                count = count + 1 
        else:
            print '数据不足10条'
       
        # print list(set(new_url_list)) # 列表去重
        
        return list(set(new_url_list)) 
    
    except:
        print '爬取失败'
        return None

def get_datas(urls):   
    all_datas = []
    # count = 0;
    print '开始爬取...'
    for link in urls:
        # print link
        html_cont = downloader(link)
        all_datas.append(html_parser(link, html_cont))
        # print all_datas[count]
        # count = count + 1
        
    print '数据获取完毕！'
        
    return all_datas

# 下载网页，入口网址
root_url = "http://baike.baidu.com/view/21087.htm"

# 下载入口url
html_cont = downloader(root_url)
# 解析入口url数据
root_data = html_parser(root_url, html_cont)
# 得到入口url里所有的url
urls = get_new_urls(html_cont)
# 得到符合条件的数据
datas = get_datas(urls)
# 输出数据
out_html(root_url, root_data, datas)


