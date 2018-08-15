#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/15 11:38 
# @Author : virus 
# @File : practice1.py
# @Desp : 测试爬虫pip包

import requests
from lxml import etree

url="http://econpy.pythonanywhere.com/ex/001.html"
page=requests.get(url)
html=page.text
selector = etree.HTML(html)

buyer=selector.xpath('//div[@title="buyer-name"]/text()')
prices=selector.xpath('//span[@class="item-price"]/text()')

print (buyer)
print (prices)