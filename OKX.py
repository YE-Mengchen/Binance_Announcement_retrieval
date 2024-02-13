import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

url = "https://www.okx.com/cn/help/section/announcements-latest-announcements"


while True:
  response = requests.get(url)
  last_announcements_text = []
  if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    selected_a = soup.select_one('#root > div:first-of-type > div:nth-of-type(2) > div:first-of-type > div:nth-of-type(2) > div:first-of-type > ul:first-of-type > li:first-of-type >  a:first-of-type div')
    if selected_a:
      current_announcement_text = selected_a.get_text(strip=True)
      if last_announcements_text is None:
        last_announcements_text = current_announcement_text
        print(f"Initial announcement set: {current_announcement_text}")
      elif current_announcement_text != last_announcements_text:
        last_announcements_text = current_announcement_text         
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"Time: {now}, New Announcement Text: {current_announcement_text}")
  else:
    print(f"Failed to retrieve the web page.")
  time.sleep(60)
    