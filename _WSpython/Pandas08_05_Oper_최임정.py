
# coding: utf-8

# In[1]:


import pandas as pd

scientists =pd.read_csv('../data/scientists.csv')
ages=scientists['Age']


# In[2]:


print(ages+ages)


# In[3]:


print(ages*ages)


# In[4]:


print(ages+100)


# In[5]:


print(ages*2)


# In[6]:


print(pd.Series([1,100]))
#1,100이 들어있는 series 생성


# In[8]:


print(ages,'\n\n')
print(pd.Series([1,100]),'\n\n')
print(ages+pd.Series([1,100]))
#pd.Series([1,100])은 2행까지밖에 없어서 나머지는 다 nan값


# In[9]:


print(ages)


# In[11]:


rev_ages=ages.sort_index(ascending=False)
#오름차순 정렬
#76543210순서
print(rev_ages)


# In[13]:


print(rev_ages*2)

