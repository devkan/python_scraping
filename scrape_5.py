import requests
from bs4 import BeautifulSoup


header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
all_jobs = []


def scrape_page(url):
  print(f"\nScraping page {url} .........................................")
  response = requests.get(url, headers=header)
  #print(response.content)

  soup = BeautifulSoup(response.content, "html.parser")
  jobs = soup.find("ul", class_="jobs-list-items").find_all("li")
  #print(jobs)

  
  for job in jobs:
    title = job.find("h4", class_="bjs-jlid__h").get_text()
    company = job.find("a", class_="bjs-jlid__b").text # get_text()대신에 text를 사용해도 된다. 함수 아님 주의


    url = job.find("h4", class_="bjs-jlid__h").find("a")["href"]
    description = job.find("div", class_="bjs-jlid__description").text
    


    print(title, " - ", company, "-", url)

    job_data = {
      "title": title,
      "company": company,
      "description": description,
      "url": url
    }
    
    all_jobs.append(job_data)


def get_pages(url):
  response = requests.get(url, headers=header)
  soup = BeautifulSoup(response.content, "html.parser")
  
  return len(soup.find("ul", class_="bsj-nav").find_all("a", class_="page-numbers"))
  # len은 배열의 길이를 반환하고, find_all은 배열을 반환한다.


skills = [
    "python",
    "typescript",
    "javascript",
    "rust"
]
# https://berlinstartupjobs.com/skill-areas/javascript/

target_url = "https://berlinstartupjobs.com/engineering/"
total_pages = get_pages(target_url)
#print(total_pages)

# range는 count() 같은 것임
for x in range(total_pages):
  url = f"https://berlinstartupjobs.com/engineering/page/{x+1}/"
  scrape_page(url)
  
print("\n\nskill page scraping .............................................")
for skill in skills:
  url = f"https://berlinstartupjobs.com/skill-areas/{skill}/"
  scrape_page(url)
  
print(all_jobs)