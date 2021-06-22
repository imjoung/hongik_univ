
# coding: utf-8

# In[3]:


import pandas as pd
import seaborn as sns


# In[4]:


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


# In[11]:


#7 연령대별 사망자수 확인 

age0=titanic[(titanic['age']>=0) & (titanic['age']<=10)]
age1=titanic[(titanic['age']>=11) & (titanic['age']<=20)]
age2=titanic[(titanic['age']>=21) & (titanic['age']<=30)]
age3=titanic[(titanic['age']>=31) & (titanic['age']<=40)]
age4=titanic[(titanic['age']>=41) & (titanic['age']<=50)]
age5=titanic[(titanic['age']>=51) & (titanic['age']<=60)]
age6=titanic[(titanic['age']>=61) & (titanic['age']<=70)]
age7=titanic[(titanic['age']>=71) & (titanic['age']<=80)]

print("0-10대  남자 사망자수 : ", len((age0['survived']==0) & (age0['sex']=='male')),
     "\t//\t여자 사망자수 : ", len((age0['survived']==0) & (age0['sex']=='female')))
print("10-20대  남자 사망자수 : ", len((age1['survived']==0) & (age1['sex']=='male')),
     "\t//\t여자 사망자수 : ", len((age1['survived']==0) & (age1['sex']=='female')))
print("20-30대  남자 사망자수 : ", len((age2['survived']==0) & (age2['sex']=='male')),
     "\t//\t여자 사망자수 : ", len((age2['survived']==0) & (age2['sex']=='female')))
print("30-40대  남자 사망자수 : ", len((age3['survived']==0) & (age3['sex']=='male')),
     "\t//\t여자 사망자수 : ", len((age3['survived']==0) & (age3['sex']=='female')))
print("40-50대  남자 사망자수 : ", len((age4['survived']==0) & (age4['sex']=='male')),
     "\t//\t여자 사망자수 : ", len((age4['survived']==0) & (age4['sex']=='female')))
print("50-60대  남자 사망자수 : ", len((age5['survived']==0) & (age5['sex']=='male')),
     "\t//\t여자 사망자수 : ", len((age5['survived']==0) & (age5['sex']=='female')))
print("60-70대  남자 사망자수 : ", len((age6['survived']==0) & (age6['sex']=='male')),
     "\t//\t여자 사망자수 : ", len((age6['survived']==0) & (age6['sex']=='female')))
print("70-80대  남자 사망자수 : ", len((age7['survived']==0) & (age7['sex']=='male')),
     "\t//\t여자 사망자수 : ", len((age7['survived']==0) & (age7['sex']=='female')))

