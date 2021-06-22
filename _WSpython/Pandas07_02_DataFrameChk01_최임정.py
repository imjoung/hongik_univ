
# coding: utf-8

# In[1]:


import pandas as pd
dict_data={'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],
          'c3':[10,11,12],'c4':[13,14,15]}
df=pd.DataFrame(dict_data)
print(type(df), '\n')
print(df)


# In[2]:


import pandas as pd
df=pd.DataFrame([[15,'남','덕영중'],[17,'여','수리중']],
               index=['준서','예은'],
               columns=['나이','성별','학교'])
#행 인덱스, 열 이름 확인하기
print(df,'\n') #데이터프레임
print(df.index,'\n') #행 인덱스
print(df.columns,'\n') #열 이름

#행 인덱스, 열 이름 변경하기
df.index=['학생1','학생2']
df.columns=['연령','남녀','소속']

print(df,'\n') #데이터프레임
print(df.index,'\n') #행 인덱스
print(df.columns,'\n') #열 이름


# In[6]:


import pandas as pd
df=pd.DataFrame([[15,'남','덕영중'],[17,'여','수리중']],
               index=['준서','예은'],
               columns=['나이','성별','학교'])
print("df==========",'\n',df,'\n')

redf=df.rename(columns={'나이':'연령','성별':'남녀','학교':'소속'})
df.rename(index={'준서':'학생1','예은':'학생2'})

print("redf==========",'\n',redf,'\n')
print("df==========",'\n',df,'\n')

#inplace=True 
df.rename(columns={'나이':'연령','성별':'남녀','학교':'소속'},inplace=True)
df.rename(index={'준서':'학생1','예은':'학생2'},inplace=True)

print("df==========",'\n',df,'\n')

