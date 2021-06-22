
# coding: utf-8

# In[1]:


import random
import pandas as pd

scientists =pd.read_csv('../data/scientists.csv')
print(scientists.columns)


# In[3]:


scientists_dropped=scientists.drop(['Age'],axis=1)
#axis=1 행삭제 => age행 삭제
print(scientists_dropped.columns)

