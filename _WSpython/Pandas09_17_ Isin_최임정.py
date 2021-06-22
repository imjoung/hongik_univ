
# coding: utf-8

# In[3]:


import pandas as pd
s=pd.Series(['lama','cow','lama','beetle','lama','hippo']
            ,name='animal')
s


# In[4]:


#or 
s.isin(['cow','lama'])

