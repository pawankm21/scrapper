from bs4 import BeautifulSoup as bs
import requests

URL="https://gogoanime2.org/search/"
anime_name=input("search anime name: " )
anime_name=anime_name.replace(' ','-')
print(anime_name)
URL=URL+anime_name
r=requests.get(URL)
print(anime_name)
soup=bs(r.text,'html.parser')
anime_list=[]
for link in soup.find_all('a'):
    if link.get("href") is not None and anime_name in link.get("href"):
        anime_list.append("https://gogoanime2.org/"+link.get("href"))

for link in anime_list:
    print(link)

