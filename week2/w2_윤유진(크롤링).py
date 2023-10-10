#!/usr/bin/env python
# coding: utf-8

# In[1]:


#HTML 기본 웹 크롤링

import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.mk.co.kr/news/stock/10842752') 
soup = BeautifulSoup(res.content, 'html.parser')
mydata = soup.find('title')
print(mydata.get_text())


# In[2]:


#파이썬 기본 문법 (1)

name = ''
while name != "orange":
    name = input("What's your name?")
    print ("Hi, "+ name + " So, Is that your favorite fruit?")


# In[4]:


#파이썬 기본 문법 (2)

number = input()

print (number[8:10])
location = int(number[8:10])

if location >=0 and location <=8 :
    print("서울")
elif location >=9 and location <=12 :
    print("부산")

