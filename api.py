import sys
import ssl
import json
import time
while True: 
    ssl._create_default_https_context = ssl._create_unverified_context
    if sys.version_info[0]==2:
        import six
        from six.moves.urllib import request
        opener = request.build_opener(
            request.ProxyHandler(
                {'http': 'http://brd-customer-hl_8de5f09f-zone-unblocker:0kj82df3olse@brd.superproxy.io:22225',
                'https': 'http://brd-customer-hl_8de5f09f-zone-unblocker:0kj82df3olse@brd.superproxy.io:22225'}))
        readData = opener.open('https://www.binance.com/bapi/composite/v1/public/cms/article/catalog/list/query?catalogId=48&pageNo=1&pageSize=1').read()
    if sys.version_info[0]==3:
        import urllib.request
        opener = urllib.request.build_opener(
            urllib.request.ProxyHandler(
                {'http': 'http://brd-customer-hl_8de5f09f-zone-unblocker:0kj82df3olse@brd.superproxy.io:22225',
                'https': 'http://brd-customer-hl_8de5f09f-zone-unblocker:0kj82df3olse@brd.superproxy.io:22225'}))
        readData = opener.open('https://www.binance.com/bapi/composite/v1/public/cms/article/catalog/list/query?catalogId=48&pageNo=1&pageSize=1').read()

    jsonData = readData.decode('utf-8')
    data = json.loads(jsonData)
    title = data['data']['articles'][0]['title']
    print(title)
    time.sleep(1)
