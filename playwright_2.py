from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

# 가상모드 활성화 뒤에 실해애야 정상 작동한다.
# 01.Python_Web_Scrapper> .\dev\Scripts\activate
# 01.Python_Web_Scrapper> cd dev
# 01.Python_Web_Scrapper\dev> python playwright_2.py

pw = sync_playwright().start()
browser = pw.chromium.launch(headless=False) # 크롬 브라우저 실행. 디폴트는 headless=True임
page = browser.new_page() # 새 페이지 생성(새로이 탭을 만드는 것과 같음)
page.goto("https://www.wanted.co.kr/jobsfeed") # 해당 페이지로 이동
time.sleep(3) # 초단위로 대기함. 3초간 대기


page.click("button.Aside_searchButton__Xhqq3") #button의 class name을 이용하여 클릭
time.sleep(3)

# placeholder로 접근한 이유는 css의 명이 차후 바뀔수 있을거 같아서, 바꾸지 않을 것으로 placeholder를 사용함
# 그리고 검색어로 flutter를 입력
page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter") # placeholder를 이용하여 검색창에 "데이터 엔지니어"를 입력

page.keyboard.down("Enter") # 엔터키를 누름
time.sleep(3)

page.click("a#search_tab_position") # a태그의 id를 이용하여 클릭
time.sleep(3)

for x in range(3): # 3번 스크롤을 내림
  page.keyboard.down("End") # End키를 누름(그럼 스크롤이 맨 밑으로 내려감)
  time.sleep(3)


#print(page.content()) # 페이지의 내용을 출력
content = page.content()

page.screenshot(path="wanted_playwright.png") # 스크린샷 찍기
pw.stop() # 브라우저 종료

soup = BeautifulSoup(content, "html.parser") # BeautifulSoup으로 파싱
jobs = soup.find_all("div", class_="JobCard_container__FqChn") # div태그의 class명이 JobCard_container__FqChn인 것을 찾음

jobs_db = [] # 빈 리스트 생성
for job in jobs:
  link = job.find("a")["href"] # a태그를 찾음
  job_link = f"https://www.wanted.co.kr{link}" # 링크를 만듬
  title = job.find("string", class_="JobCard_title__ddkwM").text
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


print(jobs_db)  
print(len(jobs_db))
