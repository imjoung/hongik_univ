
# coding: utf-8

# In[2]:


import pandas
df= pandas.read_csv('../data/gapminder.tsv',sep='\t')
small_range = list(range(5))
print(small_range)
print(type(small_range))


# In[3]:


df.head(3)


# In[4]:


subset=df.iloc[:,small_range] #small_range가 0,1,2,3,4라 5인 gdp잘림
subset.head()


# In[5]:


small_range=list(range(3,6))
small_range


# In[6]:


subset=df.iloc[:,small_range]
subset.head()


# In[7]:


small_range=list(range(0,6,2)) #0에서 5까지 2칸
subset=df.iloc[:,small_range]
subset.head()

