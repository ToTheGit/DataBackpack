from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
  base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term=" # 기본 url
  # search_term = "python" # 검색 varialbe
  response = get(f"{base_url}{keyword}")
  if response.status_code != 200: #검색 되는건지 확인 if문
    print("Can't request website")
  else: #검색되면 진행
    results = []
    soup = BeautifulSoup(response.text, "html.parser") 
    #response.text: html -> python entity(not just string)
    jobs = soup.find_all('section', class_= "jobs") # class 파라미터
    for job_section in jobs: #loop in jobs class
      job_posts = job_section.find_all('li') #lists of li in jobs class
      job_posts.pop(-1) #view all 제거
      for post in job_posts: #loop in job_posts(li lists) 
        anchor = post.find_all('a') 
        anchor = anchor[1] #li lists 중에 2번째 anchor 얻기
        link = anchor['href'] #link for jobs 
        company, kind, region = anchor.find_all('span', class_="company") ##company info in span to variables
        title = anchor.find('span', class_='title')
        # print(company.string, kind.string, region.string, title.string)
        job_data = { # 저장안하면 사라짐 -> line 11
          'link' : f"https://weworkremotely.com{link}", #.string: remove tag -> only print string
          'company' : company.string,
          'region' : region.string,
          'position' : title.string
        }
        results.append(job_data) #results list에 영구히 저장
    return results