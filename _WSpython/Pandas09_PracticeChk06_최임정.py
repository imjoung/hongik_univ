
# coding: utf-8

# In[1]:


import pandas as pd

s1=pd.Series(['Mouse','dog','house and parrot','23'])
s1.str.contains('og')


# In[2]:


ind=pd.Index(['Mouse','dog','house and parrot','23'])
ind.str.contains('23')


# In[3]:


#case=False:대소문자 구별x
s1.str.contains('OG',case=False)


# In[4]:


s1.str.contains('house|dog')


# In[6]:


s1.str.contains('\\d')


# s2=pd.Series(['40','40,0','41','41,0','35'])
# s2.str.contains('.0')

# In[7]:


s2=pd.Series(['40','40.0','41','41.0','35'])
s2.str.contains('.0')

