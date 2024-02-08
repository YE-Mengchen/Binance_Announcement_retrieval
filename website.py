import sys
import ssl
import json
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
while True:
    ssl._create_default_https_context = ssl._create_unverified_context
    last_announcements_text = []
    if sys.version_info[0]==2:
        import six
        from six.moves.urllib import request
        opener = request.build_opener(
            request.ProxyHandler(
                {'http': 'http://brd-customer-hl_8de5f09f-zone-unblocker:0kj82df3olse@brd.superproxy.io:22225',
                'https': 'http://brd-customer-hl_8de5f09f-zone-unblocker:0kj82df3olse@brd.superproxy.io:22225'}))
        readData = opener.open('https://www.binance.com/zh-CN/support/announcement').read()
    if sys.version_info[0]==3:
        import urllib.request
        opener = urllib.request.build_opener(
            urllib.request.ProxyHandler(
                {'http': 'http://brd-customer-hl_8de5f09f-zone-unblocker:0kj82df3olse@brd.superproxy.io:22225',
                'https': 'http://brd-customer-hl_8de5f09f-zone-unblocker:0kj82df3olse@brd.superproxy.io:22225'}))
        readData = opener.open('https://www.binance.com/zh-CN/support/announcement').read()

    htmlData = readData.decode('utf-8')
    soup = BeautifulSoup(htmlData, 'html.parser')
                
    selected_a = soup.select_one('#app-wrap > div:first-of-type > div:first-of-type > div:nth-of-type(4) > div:first-of-type > div:first-of-type > div:first-of-type > div:nth-of-type(3) > div:first-of-type a')
                
    if selected_a:
        current_announcement_text = selected_a.get_text(strip=True)
        print(f"Initial {'cn'} announcement set: {current_announcement_text}")
    time.sleep(1)