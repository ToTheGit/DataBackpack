from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs  ##from (folder name) import (function name)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
#replit 작동용 코드
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)


Number=[]
Title=[]
Author=[]
Time=[]
View=[]
Recommendation=[]
Comment=[]
Text=[]


index=[2] #44173
#for문
for indexs in index:
  url = f"https://gall.dcinside.com/board/view/?id=casino2&no={indexs}"
  response = browser.get(url)
  soup = BeautifulSoup(browser.page_source, "html.parser")
  
  number = url.split("no=")[-1]
  print(number)
  title = soup.find("span", class_="title_subject").text
  print(title)
  author = soup.find("span", class_="ip")
  
  if author:
      author = author.text
  else:
      author = soup.find("span", class_="nickname").text
  print(author)
  time = soup.find("span", class_="gall_date")["title"]
  print(time)
  view = soup.find("span", class_="gall_count").text
  print(view)
  recommendation = soup.find("span", class_="gall_reply_num").text
  print(recommendation)
  comment = soup.find("span", class_="gall_comment").text
  print(comment)
  text = ""
  write=soup.find("div", class_="write_div")
  # if write.find_all("p"):
  for i in write.find_all("p"):
    if i.find("span"):
      text += i.find("span").text
    else:
      text += i.text
  # else:
  for j in write.find_all("div"):
    if not (j.find("img") | j.find("a")):
      if j.find("div"):
        text += j.find("div").text
      else:
        text += j.text
      
        
    # if not i.find("img"):
  text = text.replace("<br>","//")
  print(text)
  
  Number.append(number)
  Title.append(title)
  Author.append(author)
  Time.append(time)
  View.append(view)
  Recommendation.append(recommendation)
  Comment.append(comment)
  Text.append(text)
  # Saving data as a CSV file
data = {
    "Number": Number,
    "Title": Title,
    "Author": Author,
    "Time": Time,
    "View": View,
    "Recommendation": Recommendation,
    "Comment": Comment,
    "Text": Text,
}

df = pd.DataFrame(data)
df.to_csv("output.csv", index=False)










# search_term = "python"
# base_url = "https://kr.indeed.com/jobs?q="
# url = browser.get(f"{base_url}{search_term}")
  
# soup = BeautifulSoup(browser.page_source, "html.parser")
# job_list = (soup.find("ul", class_="jobsearch-ResultsList"))
# jobs = job_list.find_all('li', recursive=False)
# print(len(jobs))
# for job in jobs:
#   print(job)
#   print("/////////////////////////////////")
  

#403 봇 에러 해결방법
# Selenium: use code -> 브라우저 자동화 -> control

# print(len(jobs))

# def say_hello(name, age):
#   print(f"Hello {name} you are {age} years old")

# say_hello("nico", 12)
# say_hello(age=12, name="nico")

# list_of_numbers = [1, 2, 3]
# first, second, third = list_of_numbers
# print(first, second, third)

# from requests import get
# from bs4 import BeautifulSoup


# url = "https://data.seoul.go.kr/SeoulRtd/" # 기본 url
#   # search_term = "python" # 검색 varialbe
#   # response = get(f"{base_url}{keyword}")
# response = get(url, headers={'User-Agent':'chrome/111'}) #접속할 url, 브라우저 정보
# results = []
# soup = BeautifulSoup(response.text, "html.parser") 
    #response.text: html -> python entity(not just string)
# <div class="report_home_traffic_info">
# 	                            <h4>잔여주차공간</h4>
# 	                            <div>
# 	                                <a class="color_soso help" onclick="show_parking(); "><b class="rpt_parking rpt_data">12</b></a>
# 	                                <span class="help_text ml-5">잔여공간</span>/
# 	                                <span class="help rpt_total_parking rpt_data">280</span>
# 	                                <span class="help_text ml-5">총 주차공간</span>
# 	                                <span class="btn_more_parking btn_small_more">자세히</span>
# 	                            </div>
# 	                        </div>
# park = soup.find_all('div', class_= "report_home_traffic_info") # class 파라미터
# park
# for park_div in park:
#   park_span = park_div.find_all('span')
# park_span.pop(0)
# print(park_span)



  # graph_posts.pop(-1) #view all 제거
  # for post in job_posts: #loop in job_posts(li lists) 
  #   anchor = post.find_all('a') 
  #   anchor = anchor[1] #li lists 중에 2번째 anchor 얻기
  #   link = anchor['href'] #link for jobs 
  #   company, kind, region = anchor.find_all('span', class_="company") ##company info in span to variables
  #   title = anchor.find('span', class_='title')
  #       # print(company.string, kind.string, region.string, title.string)
  #   job_data = { # 저장안하면 사라짐 -> line 11
  #     'link' : f"https://weworkremotely.com{link}", #.string: remove tag -> only print string
  #     'company' : company.string,
  #     'region' : region.string,
  #     'position' : title.string
  #   }
  #   results.append(job_data) #results list에 영구히 저장
