
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
print(titanic.columns,'\n',titanic.shape)
df=titanic.loc[:,['age','fare']] #age랑fare열만 df에 저장
print(df.tail(),'\n') #밑 5줄만 출력
print(type(df),'\n') #dataframe형식

addition = df+10 #데이터프레임인 df에 10을 더하면 ?
print(addition.tail(), '\n') #결측치는 뭘해도 결측치
print(type(addition))

