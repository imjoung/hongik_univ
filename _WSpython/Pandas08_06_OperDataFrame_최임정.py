
# coding: utf-8

# In[1]:


import pandas as pd

scientists =pd.read_csv('../data/scientists.csv')


# In[2]:


print(scientists[scientists['Age']>scientists['Age'].mean()])
#age평균보다 큰 age들만 출력


# In[3]:


print(scientists.loc[[True,True,False,True]])


# In[4]:


print(scientists *2)
#숫자인 age는 곱하기2 되고 나머지 문자들은 이어짐 (2번)

