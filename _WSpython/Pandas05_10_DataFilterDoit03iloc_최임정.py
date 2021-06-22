
# coding: utf-8

# In[1]:


import pandas
df=pandas.read_csv('../data/gapminder.tsv',sep='\t')
df.head(3)


# In[2]:


df.iloc[1]


# In[3]:


df.iloc[99]


# In[4]:


df.iloc[-1]


# In[6]:


print(df.tail(1))
print()
print(df.shape)
print()
print(df.iloc[1703])


# In[7]:


print(df.iloc[[0,99,999]])

