#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/15 11:38
# @Author : virus
# @File : practice1.py
# @Desp : 新浪新闻历史栏目

import requests
import numpy
from lxml import etree


url="http://blog.sina.com.cn/lm/history/"
page=requests.get(url)
html=page.content
selector = etree.HTML(html)

buyer=selector.xpath('//div[@class="bd"]//a/text()')

print (buyer)
