from playwright.sync_api import sync_playwright
import time

# 가상모드 활성화 뒤에 실해애야 정상 작동한다.
# 01.Python_Web_Scrapper> .\dev\Scripts\activate
# 01.Python_Web_Scrapper> cd dev
# 01.Python_Web_Scrapper\dev> python playwright_1.py

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False) # 크롬 브라우저 실행. 디폴트는 headless=True임
page = browser.new_page() # 새 페이지 생성(새로이 탭을 만드는 것과 같음)
page.goto("https://www.instagram.com/apple/") # 해당 페이지로 이동
time.sleep(3)

page.screenshot(path="first_playwright.png") # 스크린샷 찍기
