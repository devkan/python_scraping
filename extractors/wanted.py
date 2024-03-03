from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv


class wantedScraper:
    def __init__(self, keyward):
        self.keyward = keyward
        self.jobs_db = []

        self.get_data()
        self.html_parser()
        self.make_csv()
       
        

    def get_data(self):
        p = sync_playwright().start()
        browser = p.chromium.launch(headless= False) # headless = True로 하면 content를 못 가져옴. 체크할것
        page = browser.new_page()
        move_page = f"https://www.wanted.co.kr/search?query={self.keyward}&tab=position"
        print(move_page)
        
        page.goto(move_page)
        
        for x in range(5):
            time.sleep(3)
            page.keyboard.down('End')
        self.content = page.content()
        
        p.stop() # 이거 사용하지 않으면 Async 관련된 오류 발생함
        

    def html_parser(self):
        print("html parsing..")
        
        soup = BeautifulSoup(self.content, 'html.parser')
        jobs = soup.find_all('div', class_='JobCard_container__FqChn')

        for job in jobs:
            link = f"https://www.wanted.co.kr/{job.find('a')['href']}"
            title = job.find('strong', class_='JobCard_title__ddkwM').text
            company_name = job.find('span', class_='JobCard_companyName__vZMqJ').text
            location = job.find('span', class_='JobCard_location__2EOr5').text
            reward = job.find('span', class_='JobCard_reward__sdyHn').text
            
            job ={
                'title':title,
                'company_name': company_name,
                'location': location,
                'reward': reward,
                'link': link
            }
            print(job)
            self.jobs_db.append(job)
        
        
    def make_csv(self):
        print("make csv..")
        file = open(f'./jobs/{self.keyward}.csv', 'w', encoding="utf-8")
        writter = csv.writer(file)
        if self.jobs_db == []:
            writter.writerow(['NO DATA'])
        else:
            writter.writerow(['title', 'company_name', 'location', 'reward', 'link'])
        
        for job in self.jobs_db:
            writter.writerow(job.values())
        file.close()
