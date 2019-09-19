import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.google.com/");
#print(result.status_code)
if result.status_code >= 200 and result.status_code <= 206:
    print("website accessed successfully")

#print(result.headers)

pageSrc = result.content
print(pageSrc)

spaghetti = BeautifulSoup(pageSrc, 'lxml')