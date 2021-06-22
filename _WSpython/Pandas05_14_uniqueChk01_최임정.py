
# coding: utf-8

# In[1]:


import pandas as pd
s=pd.Series([1,3,5,7,7])
s


# In[2]:


s.unique() #겹치지 않는 값


# In[4]:


s.nunique() #겹치지 않는 값의 개수 

