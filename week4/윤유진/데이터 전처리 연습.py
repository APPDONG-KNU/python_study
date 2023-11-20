#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
PATH = "COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/"
doc = pd.read_csv(PATH + "04-01-2020.csv", encoding='utf-8-sig')
doc.head()


# In[2]:


#head를 통해 데이터를 우선적으로 파악한 후 필요한 데이터를 뽑아냄
#columns를 활용해서 데이터명을 바꿔줌


# In[3]:


doc = pd.read_csv(PATH + "01-22-2020.csv", encoding = 'utf-8-sig')
try :
    doc = doc[['Province_State', 'Country_Region', 'Confirmed']]
except :
    doc = doc[['Province/State', 'Country/Region', 'Confirmed']]
    doc.columns = ['Province_State', 'Country_Region', 'Confirmed']
    
doc.head()


# In[4]:


doc = pd.read_csv(PATH + "01-22-2020.csv", encoding = 'utf-8-sig')
try :
    doc = doc[['Province_State', 'Country_Region', 'Confirmed']]
except :
    doc = doc[['Province/State', 'Country/Region', 'Confirmed']]
    doc.columns = ['Province_State', 'Country_Region', 'Confirmed']
doc = doc.dropna(subset=['Confirmed'])
doc = doc.astype({'Confirmed':'int64'})
doc.head()


# In[7]:


#dropna를 이용해서 없는 것 제거
#데이터 타입 - float에서 int로 변환해줌


# In[8]:


country_info = pd.read_csv("COVID-19-master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv", encoding='utf-8-sig')
country_info.head()


# In[9]:


test_df = pd.merge(doc, country_info, how='left', on='Country_Region')
test_df.head()


# In[10]:


test_df.isnull().sum()


# In[11]:


nan_rows = test_df[test_df['iso2'].isnull()]
nan_rows.head()


# In[12]:


import json

with open('COVID-19-master/csse_covid_19_data/country_convert.json', 'r', encoding='utf-8-sig') as json_file:
    json_data = json.load(json_file)
    print (json_data.keys())


# In[13]:


#column 값을 변경하기 위해 apply() 함수 활용
#func이라는 새로운 함수 제작 - 전체 행을 리턴하는 함수를 만듦


# In[14]:


def func(row) :
    if row['Country_Region'] in json_data :
        row['Country_Region'] = json_data[row['Country_Region']]
    return row


# In[17]:


doc = doc.apply(func, axis=1)
doc.head()


# In[18]:


#Country_Region이라는 칼럼값을 확인해서, 국가명이 다르게 기재되어 있을 경우에만 지정한 국가명으로 변경함


# In[19]:


data = '01-22-2020.csv'
data_column = data.split(".")[0].lstrip('0').replace('-','/')
data_column


# In[21]:


#lstrip, rstrip : 맨 앞에서부터 특정 문자열 삭제함수
#replace() 활용해서 바꿔주는 것


# In[22]:


doc.columns = ['Province_State', 'Country_Region', data_column]
doc.columns


# In[23]:


doc.head()


# In[26]:


# 중복데이터 합치기 : groupby() 함수를 활용해서 그룹별로 데이터를 집계함
# mean, sum을 활용해서 처리해주면 됨


# In[27]:


doc.groupby('Country_Region').sum()


# In[29]:


import json

with open('COVID-19-master/csse_covid_19_data/country_convert.json', 'r', encoding='utf-8-sig') as json_file:
    json_data = json.load(json_file)

def country_name_convert(row):
    if row['Country_Region'] in json_data:
        return json_data[row['Country_Region']]
    return row['Country_Region']

def create_dateframe(filename):

    doc = pd.read_csv(PATH + filename, encoding='utf-8-sig')  # 1. csv 파일 읽기
    try:
        doc = doc[['Country_Region', 'Confirmed']]  # 2. 특정 컬럼만 선택해서 데이터프레임 만들기
    except:
        doc = doc[['Country/Region', 'Confirmed']]  # 2. 특정 컬럼만 선택해서 데이터프레임 만들기
        doc.columns = ['Country_Region', 'Confirmed']
    doc = doc.dropna(subset=['Confirmed'])     # 3. 특정 컬럼에 없는 데이터 삭제하기
    doc['Country_Region'] = doc.apply(country_name_convert, axis=1)   # 4. 'Country_Region'의 국가명을 여러 파일에 일관되게 변경하기
    doc = doc.astype({'Confirmed': 'int64'})   # 5. 특정 컬럼의 데이터 타입 변경하기
    doc = doc.groupby('Country_Region').sum()  # 6. 특정 컬럼으로 중복된 데이터를 합치기

    # 7. 파일명을 기반으로 날짜 문자열 변환하고, 'Confirmed' 컬럼명 변경하기
    date_column = filename.split(".")[0].lstrip('0').replace('-', '/') 
    doc.columns = [date_column]
    return doc


# In[30]:


json_data


# In[33]:


doc1 = create_dateframe("01-22-2020.csv")
doc2 = create_dateframe("04-01-2020.csv")


# In[34]:


doc2.head()


# In[35]:


doc = pd.merge(doc1, doc2, how='outer', left_index=True, right_index=True)
doc.head()


# In[36]:


doc = doc.fillna(0)
doc


# In[37]:


#결측치를 fillna함수를 활용해서 0으로 대체하였음
#os 라이브러리의 list 함수 사용해서 리스트 형태로 데이터를 가져옴


# In[42]:


import os

PATH = 'COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/'
file_list = os.listdir(PATH)
csv_list = list ()

for file in file_list :
    if file.split(".")[-1] == 'csv' :
        csv_list.append(file)

print (csv_list)


# In[43]:


csv_list.sort()
csv_list


# In[44]:


#sort 디폴트 값 = 오름차순

