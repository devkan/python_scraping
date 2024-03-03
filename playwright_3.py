from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

# 가상모드 활성화 뒤에 실해애야 정상 작동한다.
# 01.Python_Web_Scrapper> .\dev\Scripts\activate
# 01.Python_Web_Scrapper> cd dev
# 01.Python_Web_Scrapper\dev> python playwright_3.py

pw = sync_playwright().start()
browser = pw.chromium.launch(headless=False) # 크롬 브라우저 실행. 디폴트는 headless=True임
page = browser.new_page() # 새 페이지 생성(새로이 탭을 만드는 것과 같음)
page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position") # 해당 페이지로 이동
time.sleep(3) # 초단위로 대기함. 3초간 대기


for x in range(3): # 3번 스크롤을 내림
  page.keyboard.down("End") # End키를 누름(그럼 스크롤이 맨 밑으로 내려감)
  time.sleep(3)

#print(page.content()) # 페이지의 내용을 출력
content = page.content()

#page.screenshot(path="wanted_playwright.png") # 스크린샷 찍기
pw.stop() # 브라우저 종료

soup = BeautifulSoup(content, "html.parser") # BeautifulSoup으로 파싱
jobs = soup.find_all("div", class_="JobCard_container__FqChn") # div태그의 class명이 JobCard_container__FqChn인 것을 찾음

jobs_db = [] # 빈 리스트 생성
for job in jobs:
  link = job.find("a")["href"] # a태그를 찾음
  job_link = f"https://www.wanted.co.kr{link}" # 링크를 만듬
  title = job.find("strong", class_="JobCard_title__ddkwM").get_text()
  company = job.find("span", class_="JobCard_companyName__vZMqJ").text
  location = job.find("span", class_="JobCard_location__2EOr5").text
  reward = job.find("span", class_="JobCard_reward__sdyHn").text
  
  job = {
    "title": title,
    "company": company,
    "location": location,
    "reward": reward,
    "link": job_link
  }
  jobs_db.append(job)

'''
File "D:\KAN_WebWork\Python\85.NomadCoder\01.Python_Web_Scrapper\dev\playwright_3.py", line 29, in <module>
  title = job.find("string", class_="JobCard_title__ddkwM").text
AttributeError: 'NoneType' object has no attribute 'text'

이런 오류가 발생하면 해당 selector를 못 찾아서 발생한 오류이다.
.text를 사용하거나 .get_text()를 사용하면 된다.

'''

#print(jobs_db)  
print(len(jobs_db))

# csv로 저장
file = open("jobs.csv", "w", encoding="utf-8")
writer = csv.writer(file)
writer.writerow(["title", "company", "location", "reward", "link"])

for job in jobs_db:
  writer.writerow(job.values()) #job.values()는 job에서 value만 가져옴
  
file.close()  