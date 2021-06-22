
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
titanic.head(3)


# In[4]:


titanic = sns.load_dataset('titanic')
print('='*40, 'head', '='*40)
print(titanic.head())
print('='*40, 'tail', '='*40)
print(titanic.tail())
print('='*40, 'shape', '='*40)
print(titanic.shape)
print('='*40, 'info', '='*40)
print(titanic.info())


# In[5]:


for idx in titanic.columns:
    print("[ %s ]\n"%idx)
    print(titanic[idx].unique())
    print("="*80)


# In[6]:


#5.성별 생존률의 개수
q5_survived_cnt = titanic[titanic['survived'] ==1]
q5_survived_cnt.groupby('sex')['survived'].count()

