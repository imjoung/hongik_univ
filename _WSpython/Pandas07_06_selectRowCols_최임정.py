
# coding: utf-8

# In[2]:


import pandas as pd

exam_data={'수학':[90,80,70],'영어':[98,89,95],
          '음악':[85,95,100],'체육':[100,90,90]}

df=pd.DataFrame(exam_data, index=['서준','우현','인아'])
print(df,'\n') 

label1=df.loc['서준'] #loc
position1=df.iloc[0] #iloc
print(label1,'\n')
print(position1, '\n')


# In[5]:


#행 인덱스를 사용해서 2개 이상의 행 선택
label2=df.loc[['서준','우현']]
position2=df.iloc[[0,1]]
print(label2,'\n')
print(position2,'\n')

#행 인덱스의 범위를 지정하여 행 선택
label3=df.loc['서준':'우현']
position3=df.iloc[0:1]
print(label3,'\n')
print(position3)


# In[7]:


import pandas as pd

exam_data={'이름':['서준','우현','인아'],
           '수학':[90,80,70],'영어':[98,89,95],
          '음악':[85,95,100],'체육':[100,90,90]}
df=pd.DataFrame(exam_data)
print(df,'\n')
print(type(df),'\n')

#수학 점수데이터만 선택 , 변수 math에 저장
math1=df['수학']
print(math1,'\n')
print(type(math1),'\n')

#영어 점수데이터만 선택, 변수 english에 저장
english=df.영어
print(english,'\n')
print(type(english),'\n')


# In[8]:


#음악,체육 데이터를 선택 변수 music_gym에 저장
music_gym=df[['음악','체육']]
print(music_gym,'\n')
print(type(music_gym),'\n')

#수학 데이터를 선택 변수 math2에 저장
math2=df[['수학']]
print(math2,'\n')
print(type(math2))

