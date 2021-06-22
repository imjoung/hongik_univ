
# coding: utf-8

# In[23]:


import pandas as pd

df = pd.DataFrame([[1,2,3,4],[100,200,300,400],[1000,2000,3000,4000]],
                      index = ['1','2','3'], columns=['a','b','c','d'])
#mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
#          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
#          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 }]
#df = pd.DataFrame(mydict)
df


# In[24]:


type(df.iloc[0])


# In[25]:


df.iloc[0]


# In[26]:


df.iloc[[0]]


# In[27]:


df.iloc[[0,1]]


# In[28]:


df.iloc[:3]


# In[29]:


df.iloc[[True,False,True]]


# In[30]:


df.iloc[0,1]


# In[31]:


df.iloc[[0,2],[1,3]] #라벨,컬럼


# In[15]:


df.iloc[1:3,0:3]


# In[13]:


df.iloc[:,[True,False,True,False]]

