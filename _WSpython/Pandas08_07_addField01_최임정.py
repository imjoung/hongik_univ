
# coding: utf-8

# In[1]:


import pandas as pd

scientists =pd.read_csv('../data/scientists.csv')


# In[2]:


print(scientists['Born'].dtype)
print(scientists['Died'].dtype)
#object : 문자열


# In[4]:


born_datetime=pd.to_datetime(scientists['Born'],format='%Y-%m-%d')
print(born_datetime)


# In[5]:


died_datetime=pd.to_datetime(scientists['Died'],format='%Y-%m-%d')
print(died_datetime)


# In[6]:


died_datetime2=died_datetime-born_datetime
#산 기간? 죽은 날짜-산 날짜
print(died_datetime2)


# In[11]:


scientists['born_dt'],scientists['died_dt']=(born_datetime,died_datetime)
print(scientists)
#born_dt와 died_dt가 추가된걸 볼 수 있음


# In[10]:


print(scientists.shape)
#총 8개의 열과 7개의 행을 가지고 있음 

