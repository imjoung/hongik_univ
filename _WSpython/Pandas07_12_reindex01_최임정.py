
# coding: utf-8

# In[4]:


import pandas as pd
dict_data={'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],
          'c3':[10,11,12],'c4':[13,14,15]}
df=pd.DataFrame(dict_data,index=['r0','r1','r2'])
print(df,'\n')

#index값이 더 많으니까 nan값 생김
new_index=['r0','r1','r2','r3','r4']
ndf=df.reindex(new_index)
print(ndf,'\n')

#reindex로 발생한 nan값을 숫자0으로 채우기
new_index=['r0','r1','r2','r3','r4']
ndf2=df.reindex(new_index,fill_value=0)
print(ndf2)

