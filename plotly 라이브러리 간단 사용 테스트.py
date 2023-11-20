#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


#plotly 라이브러리 활용
#pandas의 데이터 프레임을 바로 iplot() 시각화 가능
#가볍게 데이터 확인할 때는 iplot() 


# In[2]:


get_ipython().system('pip install plotly chart_studio -- upgrade')


# In[4]:


get_ipython().system('pip install cufflinks')


# In[5]:


import chart_studio.plotly as py
import cufflinks as cf
cf.go_offline(connected=True)


# In[6]:


#numpy 라이브러리 활용


# In[6]:


import numpy as np
np.random.rand(6)


# In[7]:


import numpy as np
np.random.rand(6, 2)


# In[12]:


#무작위적으로 행렬을 활용 implot 함수의 이해를 위해


# In[8]:


import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(10,2), columns = ['A', 'B'])
df.head()


# In[14]:


#기본 사용법 : 데이터 프레임.iplot(kind=그래프종류)


# In[9]:


cf.help()


# In[10]:


df.iplot(kind='bar')


# In[18]:


#주로 bar와 scatter그래프를 그릴 때 iplot() 함수를 사용해서 처리해줄 수 있음
#cf.help('bar')로 옵션을 확인해줄 수 있음
#series로도 그래프를 그릴 수 있다는 점


# In[11]:


df.iplot(kind='bar', barmode='stack') #누적그래프 


# In[20]:


df.iplot(kind='bar', orientation = 'h')


# In[12]:


df.iplot(kind='scatter', mode='lines+markers')


# In[14]:


df.iplot(kind='scatter',fill=True)


# In[13]:


df.iplot(kind='scatter',
        fill=True,
        xTitle='toss and turn',
        yTitle='nightmare',
        title = 'chronic fatigue')


# In[16]:


themes = cf.getThemes()
themes


# In[17]:


for theme_item in themes :
    df.iplot(kind='scatter',
            theme=theme_item,
            fill=True,
            xTitle='toss and turn',
             yTitle='nightmare',
             title = 'chronic fatigue')


# 참고 사이트 
# https://plotly.com/python/reference/#layout-title
