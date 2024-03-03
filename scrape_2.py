import requests
from bs4 import BeautifulSoup

all_jobs = []

def scrape_page(url):
  print(f"Scraping page {url}")
  response = requests.get(url)

  soup = BeautifulSoup(response.content, "html.parser")
  jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

  
  for job in jobs:
    title = job.find("span", class_="title").get_text()
    region = job.find("span", class_="region").text # get_text()대신에 text를 사용해도 된다. 함수 아님 주의

    company, position, _ = job.find_all("span", class_="company")
    # class="company"로 된 데이타가 3개여서 변수 세개를 할당한 것이고, 
    # 마지막 company는 region으로 이미 사용해서 무시기하기 위해서 _를 사용한 것임

    url = job.find("div", class_="tooltip").next_sibling["href"]
    #company = company.text
    #position = position.text

    #print(title, " - ", company, position, region, "\n")
 
    job_data = {
      "title": title,
      "company": company.text,
      "position": position.text,
      "region": region,
      "url": f"https://weworkremotely.com/{url}"
    }
    all_jobs.append(job_data)

def get_pages(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")

  return len(soup.find("div", class_="pagination").find_all("span", class_="page"))
  # len은 배열의 길이를 반환하고, find_all은 배열을 반환한다.


target_url = "https://weworkremotely.com/remote-full-time-jobs"
total_pages = get_pages(target_url)

# range는 count() 같은 것임
for x in range(total_pages):
  url = f"https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings?page={x+1}"
  scrape_page(url)
  
print(all_jobs)