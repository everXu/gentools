#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
    __author__ = 'ever'
"""

from lxml import etree
from selenium import webdriver
import time

base_url = 'http://vacations.ctrip.com/tours/d-japan-100041/grouptravel/p{0}b1999999s13#_flta'


def crawling(url,info_list):
    # print r.content
    browser = webdriver.Chrome(executable_path="H:\web\chromedriver.exe")

    browser.get(url)
    time.sleep(20)
    ht = browser.page_source
    print ht
    # browser.close()
    html = etree.HTML(ht)
    result = html.xpath("//div[contains(concat(' ',@class,' '),'main_mod')]")
    for item in result:
        tag = item.xpath("div[@class='product_pic']/em")
        info = tag[0].text

        title = item.xpath(".//h2[@class='product_title']/a")
        info += ',' + title[0].text

        price = item.xpath(".//strong/text()")
        info += ',' + price[0]
        info_list.append(info)
        print info


if __name__ == '__main__':
    result_list = []
    for i in range(5):
        target_url = base_url.format(str(i + 2))
        if i == 0:
            target_url = base_url.format('')
        crawling(target_url, result_list)
