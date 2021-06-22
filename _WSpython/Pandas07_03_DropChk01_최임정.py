
# coding: utf-8

# In[3]:


import pandas as pd

exam_data={'수학':[90,80,70],'영어':[98,89,95],
          '음악':[85,95,100],'체육':[100,90,90]}
df=pd.DataFrame(exam_data)
print(df,"\n")

df=pd.DataFrame(exam_data,index=['서준','우현','인아'])
print(df,"\n")

#데이터프레임df를 복제하여 df2에 저장, df2의 '우현'행 삭제
df2=df[:]
df2.drop('우현',inplace=True)
print(df2,"\n")

#데이터프레임df를 복제하여 df2에 저장, df2의 '우현','인아'행 삭제
df3=df[:]
df3.drop(['우현','인아'],axis=0,inplace=True)
print(df3)


# In[5]:


import pandas as pd
exam_data={'수학':[90,80,70],'영어':[98,89,95],
          '음악':[85,95,100],'체육':[100,90,90]}
df=pd.DataFrame(exam_data)
print(df,"\n")

df=pd.DataFrame(exam_data,index=['서준','우현','인아'])
print(df,"\n")

#수학  열 삭제 axis=1
df4=df[:]
df4.drop('수학',axis=1,inplace=True)
print(df4)

#영어,음악 열 삭제 
df5=df[:]
df5.drop(['영어','음악'],axis=1,inplace=True)
print(df5)

