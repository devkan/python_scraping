from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

# 가상모드 활성화 뒤에 실해애야 정상 작동한다.
# 01.Python_Web_Scrapper> .\dev\Scripts\activate
# 01.Python_Web_Scrapper> cd dev
# 01.Python_Web_Scrapper\dev> python insta.py


pw = sync_playwright().start()
browser = pw.chromium.launch(headless=False) # 크롬 브라우저 실행. 디폴트는 headless=True임
page = browser.new_page() # 새 페이지 생성(새로이 탭을 만드는 것과 같음)
page.goto("https://www.instagram.com/apple/") # 해당 페이지로 이동
time.sleep(3) # 초단위로 대기함. 3초간 대기


#print(page.content()) # 페이지의 내용을 출력
content = page.content()

page.screenshot(path="wanted_playwright.png") # 스크린샷 찍기
pw.stop() # 브라우저 종료

soup = BeautifulSoup(content, "html.parser") # BeautifulSoup으로 파싱
follower = soup.find("ul", class_="x78zum5 x1q0g3np xieb3on").text # div태그의 class명이 JobCard_container__FqChn인 것을 찾음

print(follower)

