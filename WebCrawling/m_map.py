from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs  ##from (folder name) import (function name)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import string 

#replit 작동용 코드
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)
place = "광화문"
enter = "맛집"
browser.get(f"https://m.map.naver.com/search2/search.naver?query={place}{enter}")

# infinite_loop(browser)

items = browser.find_elements(By.CSS_SELECTOR, '._item')

datas =[]
data_id=[]

for item in items:
  title = item.get_attribute('data-title')
  address = item.find_element(By.CSS_SELECTOR, '.item_address ').text.replace('주소보기\n', '')
  for character in string.punctuation:
    title = title.replace(character, '')
    id = int(item.get_attribute('data-id'))
  datas.append({
    "title" : title,
    "addr" : address
  })
  data_id.append(id)
  
print(datas)

# search_term = "python"
# base_url = "https://kr.indeed.com/jobs?q="
# url = browser.get(f"{base_url}{search_term}")
  
# soup = BeautifulSoup(browser.page_source, "html.parser")

# place = "광화문"
# enter = "맛집"
# base_url = f"https://map.naver.com/v5/search/{place}{enter}?c=13,0,0,0,dh" # 기본 url
# base_url = browser.get(base_url)

# results = []
# soup = BeautifulSoup(browser.page_source, "html.parser")
# class_find_1 = soup.find_all('div', class_ = "Ryr1F")

# for class_find_div in class_find_1:
#   class_find_2 = class_find_div.find_all('li')
#   print(class_find_2)
 
# response = get(base_url)
