#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[23]:


doc = pd.read_excel("ISSUE_HW_DAY.xlsx")


# In[24]:


doc.head()


# In[25]:


doc.tail()


# In[26]:


doc.shape


# In[27]:


doc.info()


# In[28]:


doc.columns


# In[29]:


doc.describe()


# In[31]:


doc.corr()
doc.corr(numeric_only=True)


# In[ ]:


#문자칼럼을 판다스 라이브러리에서 자동으로 제외하기 때문에 numeeric_only=True 옵션 기재
#피어슨 상관계수 바탕의 corr() 함수 사용


# In[21]:


df = pd.DataFrame()


# In[12]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[32]:


plt.figure(figsize=(4,4))
sns.heatmap(data = doc.corr(), annot=True, fmt ='.3f', linewidths=0.3, cmap='Greys' )


# https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
