
# coding: utf-8

# In[1]:


import pandas
df= pandas.read_csv('../data/gapminder.tsv',sep='\t')
df.head(3)


# In[2]:


df.shape


# In[3]:


loc00=df.loc[0]
loc00


# In[4]:


type(loc00)


# In[5]:


df.loc[90:100]


# In[6]:


print(df.loc[99])


# In[7]:


df.tail(3)


# In[8]:


print(df.loc[-1]) #-1이라는 행이 없음으로 오류


# In[9]:


len(df)

