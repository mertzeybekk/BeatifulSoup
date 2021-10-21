import requests
from bs4 import  BeautifulSoup
url=" http://www.imdb.com/chart/top"
response=requests.get(url)
html_icerigi= response.content
soup=BeautifulSoup(html_icerigi,"html.parser")
basliklar=soup.find_all("td",{"class":"titleColumn"})
ratingler=soup.find_all("td",{"class":"ratingColumn imdbRating"})
imdb=float(input("lütfen imdb puan girin"))
for baslik,rating in zip(basliklar,ratingler):
    baslik=baslik.text
    rating=rating.text
    baslik=baslik.strip()
    baslik=baslik.replace("\n","")
    rating=rating.replace("\n","")
    if (float(rating)>imdb):
        print("Film ismi: {} Filmin Ratingi : {}".format(baslik,rating))