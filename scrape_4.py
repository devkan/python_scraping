import requests
from bs4 import BeautifulSoup


response = requests.get(
    "https://berlinstartupjobs.com/engineering/",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
)

#print(response.status_code)
#print(response.content)
soup = BeautifulSoup(response.content, "html.parser")
jobs = soup.find("ul", class_="jobs-list-items").find_all("li")
print(jobs)

skills = [
    "python",
    "typescript",
    "javascript",
    "rust"
]

