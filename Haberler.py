import requests
from bs4 import  BeautifulSoup
url="http://ekonomi.haber7.com/"
response=requests.get(url)
html_iceriği=response.content
soup=BeautifulSoup(html_iceriği,"html.parser")
print("Kur Degeri")
kur=soup.find_all("a",{"class":"economy-exchange-rate-content dollar"})
for i in kur:
    print(i.text)
print("*************")
print("Ekonomi Haberleri")
ekonomi=soup.find_all("div",{"class":"home-economy-news row"})
haberler=[]
haberler2=[]
for i in ekonomi:
   haberler.append(i.text)
for value in haberler:
  print(value) 
print("**************")
print("Günün Haberleri")
gününhaberi=soup.find_all("span",{"class":"title"})
for i in gününhaberi:
    haberler2.append(i.text)
for value in haberler2:
    print(value)
