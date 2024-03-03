import requests

keywords = [
  "flutter",
  "python",
  "golang"
]


#블럭된 사이트를 우회해서 스크래핑 하는 코드

r = requests.get("https://remoteok.com/remote-flutter-jobs", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"})
print(r.status_code)
print(r.content)


"""
503
b'<html>\n<head><title>503 Service Temporarily Unavailable</title></head>\n<body>\n<center><h1>503 Service Temporarily Unavailable</h1></center>\n<hr><center>nginx</center>\n</body>\n</html>\n'
그냥 접근하면 이처럼 503 에러가 뜨면서 거부를 하게 된다.
이를 해결하기 위해서는 크롬 개발자에서 request header에서 user-agent를 세팅해 주면 된다.

Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36

"""