#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
PATH = "COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/"
doc = pd.read_csv(PATH + "04-01-2020.csv", encoding='utf-8-sig')


# In[3]:


doc.head()


# In[4]:


#series 추출하기
#하나의 feature(cloumn)만 추출해서 하면 됨


# In[7]:


countries = doc['Country_Region']
countries.head()


# In[8]:


print(countries.size, countries.count())


# In[9]:


countries.value_counts()


# In[10]:


#필요한 칼럼만 선택하기 (필요없는 데이터열 제거)
#여러의 칼럼을 선택하면 별도의 데이터 프레임이 됨


# In[11]:


covid_stat = doc[['Confirmed','Deaths','Recovered']]
covid_stat.head


# In[14]:


doc = pd.read_csv(PATH + "04-01-2020.csv", encoding = 'utf-8-sig')


# In[17]:


doc_us = doc[doc['Country_Region']=='US']
doc_us


# In[19]:


#없는 데이터 처리하기
#raw data 에는 결측지가 많기 때문에 몇 개인지 등을 확인해야함
#isnull() 사용


# In[20]:


doc = pd.read_csv(PATH+"01-22-2020.csv", encoding='utf-8-sig')
doc.isnull().sum()


# In[ ]:


#없는 데이터 삭제하기
#dropna() : 결측지가 없는 행을 모두 삭제


# In[21]:


doc = pd.read_csv(PATH+"01-22-2020.csv", encoding='utf-8-sig')
doc = doc.dropna()
doc.head()


# In[22]:


doc = pd.read_csv(PATH+"01-22-2020.csv", encoding='utf-8-sig')
doc = doc.dropna(subset=['Confirmed'])
doc.head()


# In[23]:


#fillna() - 특정값으로 결측치를 대체 가능한 함수


# In[24]:


doc = pd.read_csv(PATH+"01-22-2020.csv", encoding='utf-8-sig')
doc = doc.fillna(0)
doc.head()


# In[25]:


#특정 키값을 기준으로 데이터 합치기
#raw data 계속해서 가공이 필요함
#groupby() 특정 칼럼을 기준으로 그룹화 : 중복된 행을 합치는 것
#sum() : 합쳐서 보여줌


# In[26]:


doc = pd.read_csv(PATH + "04-01-2020.csv", encoding = 'utf-8-sig')
doc.head()


# In[27]:


doc = doc.groupby('Country_Region').sum()
doc.head()


# In[28]:


#groupby를 사용하면 countryregion으로 인덱스가 변경되었음을 알 수 있음


# In[29]:


doc.columns


# In[30]:


doc.index


# In[31]:


doc[doc.index == 'US']


# In[32]:


#데이터 프레임 칼럼 타입 변경하기
#astype() 활용할 수 있음


# In[35]:


doc = pd.read_csv(PATH + '01-22-2020.csv', encoding = 'utf-8-sig')
doc = doc[['Country/Region', 'Confirmed']]
doc = doc.dropna(subset = ['Confirmed'])
doc = doc.astype({'Confirmed' : 'int64'})
doc.info()


# In[ ]:


#doc[[]] 형태로 필요한 칼럼만 선택
#subset 특정 칼럼에 없는 데이터 삭제
#astype({:}) 형태로 특정 칼럼의 데이터 타입 변경 - 위의 경우 int로 데이터 타입을 변경한 것


# In[36]:


doc.head()


# In[37]:


#float에서 정수로 데이터 타입이 변경된 것 


# In[41]:


#ducplicated() : 중복행 확인하는 함수
#drop_ducplicates() : 중복 행 삭제중복값


# In[43]:


doc = pd.read_csv("COVID-19-master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv", encoding='utf-8-sig')
doc = doc[['iso2', 'Country_Region']]
doc


# In[44]:


doc.duplicated()


# In[45]:


doc = doc.drop_duplicates(subset='Country_Region', keep='last')
doc


# In[46]:


#중복된 경우, 처음과 마지막 행 중 어느 행을 남길지 결정을 해주어야함


# In[ ]:




