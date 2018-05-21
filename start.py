#!/usr/bin/env python3
#	encoding:utf-8

#import urllib.request
#
#def gethtml(url):
#    page = urllib.request.urlopen(url)
#    content = page.read().decode()
#    return content
#
#url = "http://www.baidu.com"
#things = gethtml(url)
#print(things)

import requests
import os
import re
import time

def url_open(url):
    # 字典形式的请求头
    header = {
      'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0"
       }
    # 用get方法发送请求，获取网页源码
    response = requests.get(url, headers=header)
    print(response)
    return response

def find_imgs(url):
    html = url_open(url).text
    # p = r'<img src="([^"]=\.jpg")'
    p = r'<img\ src="(http\:.*jpg)"'

    # 图片地址信息: <img src="http://mm.chinasareview.com/wp-content/uploads/2017a/06/04/limg.jpg" ...
    img_addrs = re.findall(p, html)
    # 返回一个页面里的所有图片url
    return img_addrs

def download_mm(folder='beautys'):
    os.path.exists(folder) or os.mkdir(folder)
    os.chdir(folder)	#进入folder目录

    page_num = 1
    x = 0
    img_addrs = []

    while page_num <= 2:
        page_url = url + 'a/more_' + str(page_num) + '.html'
        #print("page_url: ", page_url)
        addrs = find_imgs(page_url)
        #print("addrs", addrs)
        # 避免重复下载相同的图片(相同的url)
        for i in addrs:
            if i in img_addrs:
                continue
            img_addrs.append(i)
        #print("len(img_addrs): ", len(img_addrs))
        for i in img_addrs:
            print(i)
        page_num += 1
        #time.sleep(3)

    for i in img_addrs:
        filename = str(x) + '.' + i.split('.')[-1]	# 把i用'.'分割开，放入一个list
        x += 1
        # 新建一个可写的二进制文件句柄f，保存为filename文件
        with open(filename, 'wb') as f:
            img = url_open(i).content
            f.write(img)
        print(" TO WAIT FOR A SECOND \n")
        time.sleep(1)

if __name__ == '__main__':
    # url是一个全局变量
    url = 'http://www.meizitu.com/'
    download_mm()
