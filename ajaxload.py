#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
    __author__ = 'ever'
"""

import requests
import json

header = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Cookie': '_abtest_userid=0496289a-15cf-4634-b553-ce6ee9744f62;_bfa=1.1464425436141.42hdc4.1.1489306089568.1489306089568.4.9;Visitor=1;page_time=1489295617636%2C1489296125685%2C1489296592040%2C1489306093382;_RGUID=77520729-c5cf-4692-94ec-38ce5818ad3e;_jzqco=%7C%7C%7C%7C1489295620531%7C1.351094635.1489295618882.1489296593398.1489306094495.1489296593398.1489306094495.0.0.0.4.4;__zpspc=9.2.1489306094.1489306094.1%234%7C%7C%7C%7C%7C%23; MKT_Pagesource=PC; _ga=GA1.2.31208175.1489295620; ASP.NET_SessionSvc=MTAuOC4xODkuNjd8OTA5MHxqaW5xaWFvfGRlZmF1bHR8MTQ3MTUyMDQ4OTM3OA; RecentSearch=[{"Keyword":"%e6%97%a5%e6%9c%ac","Url":"http://vacations.ctrip.com/tours/d-japan-100041"}]; _bfi=p1%3D600000435%26p2%3D600000435%26v1%3D9%26v2%3D8; Session=SmartLinkCode=U722327&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; Union=AllianceID=276710&SID=722327&OUID=000401app-; StartCity_Pkg=PkgStartCity=32; _bfs=1.4',
    'Referer': 'http://vacations.ctrip.com/tours/d-japan-100041/grouptravel/pb1999999s13',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'X-Requested-With': 'XMLHttpRequest',
    'Host': 'vacations.ctrip.com',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'

}

json_str = '[{"Id":11851789,"Bu":"GT","Did":2},{"Id":15330853,"Bu":"GT","Did":32},{"Id":6395297,"Bu":"GT","Did":32},{"Id":11729712,"Bu":"GT","Did":58}]'

payload = {'params': json_str}

pr = requests.post('http://vacations.ctrip.com/tour-mainsite-vacations/api/product', data=payload, headers=header)
print pr.content

