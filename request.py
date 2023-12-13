import requests
from bs4 import BeautifulSoup
url="https://softwarica.edu.np/"
response=requests.get(url)
print(response.url)
print(response.status_code)





r=requests.get(url)

print(r)

print(r.status_code)

print(r.url)

htmlcontent=(r.content)

print(htmlcontent)

soup=BeautifulSoup(htmlcontent, 'html.parser')

print(soup.prettify())

print(soup.title)
print(type(soup.title))
print(type(soup.title.string))
print(soup)
