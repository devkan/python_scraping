import requests
from bs4 import BeautifulSoup

#def scrape_page(url):
  

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"
response = requests.get(url)
#content = response.content
#print(content)

soup = BeautifulSoup(response.content, "html.parser")
jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]
# section의 id가 category-2인 것을 찾아서 jobs에 저장
# class는 예약어이기에 파이썬에서는 class_로 사용해야 한다.
# id="category-2" 로 접근시 이처럼 하면 된다.
# 한줄만 가져올때는 find, 리스트 전체를 가져올때는 find_all을 사용하면 된다.
# [1:-1] 은 맨 처음과 맨 마지막으로 제외한다는것이다.

#print(jobs)
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[1]) # 2
print(a[0:5]) #[1, 2, 3, 4, 5]
print(a[1:]) # [2, 3, 4, 5, 6, 7, 8, 9]
print(a[1:-1]) # [2, 3, 4, 5, 6, 7, 8]
print(a[1:-5]) # [2, 3, 4]

letters = ["a", "b", "c"]
a, str_b, c = letters #이렇게 하면 unpack이 가능해 진다. 대신 갯수는 동일해야 한다.
print(a) # 'a'
print(str_b) # 'b'
print(c) # 'c'

"""


"""
title : <span class="title">Technical Cofounder(s) for B2B Email Service Provider startup</span>

<span class="company">Stealth B2B Email Service Provider startup</span>
<span class="company">Full-Time</span>
region : <span class="region company">Anywhere in the World</span>

"""

all_jobs = []

for job in jobs:
  title = job.find("span", class_="title").get_text()
  region = job.find("span", class_="region").text # get_text()대신에 text를 사용해도 된다. 함수 아님 주의
  
  company, position, _ = job.find_all("span", class_="company")
  # class="company"로 된 데이타가 3개여서 변수 세개를 할당한 것이고, 
  # 마지막 company는 region으로 이미 사용해서 무시기하기 위해서 _를 사용한 것임

  url = job.find("div", class_="tooltip").next_sibling["href"]
  #company = company.text
  #position = position.text
  
  print(title, " - ", company, position, region, "\n")

  job_data = {
    "title": title,
    "company": company.text,
    "position": position.text,
    "region": region,
    "url": f"https://weworkremotely.com/{url}"
  }
  all_jobs.append(job_data)


print(all_jobs)