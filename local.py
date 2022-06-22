import requests
from bs4 import BeautifulSoup
import html5lib
import pandas as pd

url = 'https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi'
r = requests.get(url)

content = BeautifulSoup (r.content , 'html.parser')


name = content.find_all('div',{"class":"_4rR01T"})
price = content.find_all('div',{"class":"_30jeq3 _1_WHN1"})
print (name[0])
print (price[0])

nm=[]
pr=[]
for i in name:
    nm.append(i.text)
for j in price:
    pr.append(j.text)

data = {'name':nm , 'price':pr}
df = pd.DataFrame(data)
print (df)
