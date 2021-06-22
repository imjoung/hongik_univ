
# coding: utf-8

# In[2]:


import pandas as pd
#k:v구조를 갖는 딕셔너리를 만들고 , 변수 dict_data에 저장
dict_data={'a':[1,3],'b':[2,3],'c':[3,3]}
sr=pd.Series(dict_data)
print(type(sr))
print("\n")
print(sr)


# In[4]:


import pandas as pd
#리스트를 시리즈로 변환하여 변수 sr에 저장
list_data=['2021-05-19',3.14,'ABC',100,True]
sr=pd.Series(list_data)
print(sr, '\n')

idx=sr.index
val=sr.values
print("sr.index : ", idx)
print("sr.index type: ", type(idx))
print("sr.values : ", val)
print("sr.values type : ", type(val))


# In[5]:


import pandas as pd
#튜플을 시리즈로 변환
tup_data=('영인','2010-05-01','여',True)
sr=pd.Series(tup_data,index=['이름','생년월일','성별','학생여부'])
print(sr,'\n')

print(sr[0],'\n')
print(sr['이름'])


# In[7]:


print(sr[[1,2]], '\n')
print(sr[['생년월일','성별']], '\n')

print(sr[1:2], '\n')
print(sr['생년월일':'성별'])

a=range(1,7)
print(a)
for idx in a:
    print(idx)

test=sr['생년월일':'성별']
print(test)
type(test)

