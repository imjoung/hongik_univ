
# coding: utf-8

# In[ ]:


import pandas as pd
#데이터프레임 만들기
scientists=pd.DataFrame({
    'Name':['Rosaline Franklin','William Gosset'],
    'Occupation':['Chemist','Statistician'],
    'Born':['1920-07-25','1876-06-13'],
    'Died':['1958-04-16','1937-10-16'],
    'Age':[37,61]})
print(scientists)


# In[3]:


import pandas as pd

scientists = pd.DataFrame(data={'Occupation':['Chemist','Statistician'],
     'Born':['1920-07-25','1846-06-13'],'Died':['1958-04-16','1937-10-16'],
     'Age':[37,61]},index=['Rosaline Franklin','William Gosset'],
                          columns=['Occupation','Born','Age','Died'])
print(scientists)


# In[6]:


from collections import OrderedDict

scientists=pd.DataFrame([
    ('Name',['Rosaline Franklin','William Gosset']),
    ('Occupation',['Chemist','Statistician']),
    ('Born',['1920-07-25','1876-06-13']),
    ('Died',['1958-04-16','1937-10-16']),
    ('Age',[37,61])])
print(scientists)
print(type(scientists[0]))


# In[8]:


from collections import OrderedDict

scientists=pd.DataFrame(OrderedDict([
    ('Name',['Rosaline Franklin','William Gosset']),
    ('Occupation',['Chemist','Statistician']),
    ('Born',['1920-07-25','1876-06-13']),
    ('Died',['1958-04-16','1937-10-16']),
    ('Age',[37,61])]))
print(scientists)

#Name''''''이 컬럼이름으로 올라옴 

