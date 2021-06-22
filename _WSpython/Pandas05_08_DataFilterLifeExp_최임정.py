
# coding: utf-8

# In[2]:


import pandas as pd
s=pd.Series([4,2,0,8])
s


# In[3]:


s.max()


# In[4]:


s.min()


# In[11]:


df= pd.read_csv('../data/gapminder.tsv',sep='\t')
iloc_life=df.iloc[:,[False,False,False,True,False,False]]
iloc_life


# In[13]:


print(iloc_life.max())
print(iloc_life.min())
#iloc 최대기대수명, 최소기대수명


# In[17]:


life_df=df['lifeExp']
print(life_df.max())
print(life_df.min())
#컬럼명으로 최대기대수명, 최소기대수명


# In[18]:


loc_life=df.loc[:,'lifeExp']
print(loc_life.max())
print(loc_life.min())
#loc로 최대기대수명, 최소기대수명

