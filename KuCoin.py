import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import math
import random

url = "https://www.kucoin.com/zh-hant/announcement"


while True:
  response = requests.get(url)
  last_announcements_text = []
  if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.select_one('#root > div:first-of-type > div:first-of-type > div:nth-of-type(2) > div:first-of-type > div:nth-of-type(2) > div:nth-of-type(2) > a:first-of-type > div:first-of-type > div:first-of-type > h3:first-of-type span')
    content = soup.select_one('#root > div:first-of-type > div:first-of-type > div:nth-of-type(2) > div:first-of-type > div:nth-of-type(2) > div:nth-of-type(2) > a:first-of-type p > span > span')
    if title:
      current_announcement_text = title.get_text(strip=True)
      content = content.get_text(strip=True)
      if last_announcements_text is None:
        last_announcements_text = current_announcement_text
        print(f"Initial announcement set: {current_announcement_text}")
      elif current_announcement_text != last_announcements_text:
        last_announcements_text = current_announcement_text         
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"Time: {now}, New Announcement Title: {current_announcement_text}, \n Content: {content}")
  else:
    print(f"Failed to retrieve the web page.")
  time.sleep(80 + random.random() * 20)
    