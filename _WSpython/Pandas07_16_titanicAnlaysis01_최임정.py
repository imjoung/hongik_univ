
# coding: utf-8

# In[10]:


import pandas as pd
import seaborn as sns


# In[13]:


titanic=sns.load_dataset('titanic')
print(titanic.columns,"\n",titanic.shape)
titanic.head()


# In[22]:


#4 age 최소, 최대
print("최소 나이는 : ", titanic['age'].min())
print("최대 나이는 : ", titanic['age'].max())


# In[37]:


#5 성별별 survived 개수
sur1_m=titanic[(titanic['survived']==1)& (titanic['sex']=='male')]
sur1_f=titanic[(titanic['survived']==1)& (titanic['sex']=='female')]

print(len(titanic['survived']))
print("survive male : ",len(sur1_m),"명")
print("survive female : ",len(sur1_f),"명")


# In[36]:


#6 남자, 여자 명수
print("total male : ",len(titanic['sex']=='male'))
print("total female : ",len(titanic['sex']=='female'))

