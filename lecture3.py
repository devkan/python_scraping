from requests import get

#################################
# for loop 
##################################
print("for loop....................")


websites = (
  "google.com",
  "airbnb.com",
  "https://twitter.com",
  "facebook.com",
  "https://tiktok.com"
)

results = {}

for website in websites:
  if not website.startswith("https://"): # if not
    website = f"https://{website}" # f string
    
  response = get(website) # https://developer.mozilla.org/ko/docs/Web/HTTP/Status 참조
  
  #print(response.status_code)

  if response.status_code == 200:
    results[website] = "OK"
    #print(f"{website} is OK")
  else:
    results[website] = "FAILED"
    #print(f"{website} is not OK")

print(results)