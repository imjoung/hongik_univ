
# coding: utf-8

# In[2]:


import random
import pandas as pd

scientists =pd.read_csv('../data/scientists.csv')
random.seed(42)
random.shuffle(scientists['Age'])
print(scientists['Age'])

