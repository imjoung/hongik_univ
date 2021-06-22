
# coding: utf-8

# In[6]:


import pandas as pd

scientists =pd.read_csv('../data/scientists.csv')
ages=scientists['Age']
print("max age: ",ages.max())
print("mean age: ",ages.mean())


# In[9]:


print("age > age avg :", "\n",ages[ages>ages.mean()])


# In[10]:


print(ages>ages.mean()) #age[]로 안하면 true/false


# In[11]:


print(type(ages>ages.mean()))


# In[12]:


manual_bool_values=[True,True,False,False,True,True,False,True]
#true/false를 이용해서도 출력가능 
print(ages[manual_bool_values])

