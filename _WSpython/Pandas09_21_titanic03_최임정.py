
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
titanic=sns.load_dataset('titanic')
print(titanic.columns,"\n",titanic.shape)
titanic.head()


# In[2]:


#7 연령대별 사망자수 확인 

age0=titanic[(titanic['age']>=0) & (titanic['age']<=10)]
age1=titanic[(titanic['age']>10) & (titanic['age']<=20)]
age2=titanic[(titanic['age']>20) & (titanic['age']<=30)]
age3=titanic[(titanic['age']>30) & (titanic['age']<=40)]
age4=titanic[(titanic['age']>40) & (titanic['age']<=50)]
age5=titanic[(titanic['age']>50) & (titanic['age']<=60)]
age6=titanic[(titanic['age']>60) & (titanic['age']<=70)]
age7=titanic[(titanic['age']>70) & (titanic['age']<=80)]

print(len(age1))

print("0-10세 사망자수 : ", len(age0['survived']==0))
print("10-20세 사망자수 : ", len(age1['survived']==0))
print("20-30세 사망자수 : ", len(age2['survived']==0))
print("30-40세 사망자수 : ", len(age3['survived']==0))
print("40-50세 사망자수 : ", len(age4['survived']==0))
print("50-60세 사망자수 : ", len(age5['survived']==0))
print("60-70세 사망자수 : ", len(age6['survived']==0))
print("70-80세 사망자수 : ", len(age7['survived']==0))

