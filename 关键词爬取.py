#!usr/bin/env python
#-*- coding:utf-8 _*-
import requests
import time
import re

#获取淘宝首页源码
def require(url):
    response=requests.get(url)
    response.encoding='utf-8'
    html=response.text
    print(html)
    return html

def data_an(html):
    pass
def main():
    pass
if __name__=="__main__":
    url='https://www.taobao.com/'
    html=require(url)
