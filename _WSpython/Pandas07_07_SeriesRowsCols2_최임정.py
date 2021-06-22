
# coding: utf-8

# In[2]:


import pandas as pd

exam_data={'이름':['서준','우현','인아'],
          '수학':[90,80,70],
          '영어':[98,89,95],
          '음악':[85,95,100],
          '체육':[100,90,90]}
df=pd.DataFrame(exam_data)
print(df,'\n')

#이름 열을 새로운 인덱스로 지정하고 df객체에 변경사항 반영
df.set_index('이름',inplace=True)
print(df,'\n')

#df의 특정원소 1개 선택 (서준의 음악점수)
a=df.loc['서준','음악']
print(a,'\n')
b=df.iloc[0,2]
print(b,'\n')


# In[4]:


#서준의 음악,체육 점수
c=df.loc['서준',['음악','체육']]
print(c,'\n')
d=df.iloc[0,[2,3]]
print(d,'\n')
e=df.loc['서준','음악':'체육']
print(e, '\n')
f=df.iloc[0,2:]
print(f,'\n')

#서준과 우현의 음악,체육점수
g=df.loc[['서준','우현'],['음악','체육']]
print(g,'\n')
h=df.iloc[[0,1],[2,3]]
print("df.iloc[[0,1],[2,3]]\n",h,'\n')
i=df.loc['서준':'우현','음악':'체육']
print("df.loc['서준':'우현','음악':'체육']\n",i,'\n')
j=df.iloc[0:2,2:]
print(j)


# In[5]:


df.loc[:,['음악','체육']]


# In[6]:


print(df)
df.iloc[:,[2,3]]


# In[7]:


df.iloc[:,2:4]

