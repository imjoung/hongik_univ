
# coding: utf-8

# In[1]:


import pandas as pd
scientists = pd.DataFrame(data={'Occupation':['Chemist','Statistician'],
     'Born':['1920-07-25','1846-06-13'],'Died':['1958-04-16','1937-10-16'],
     'Age':[37,61]},index=['Rosaline Franklin','William Gosset'],
                          columns=['Occupation','Born','Age','Died'])
print(scientists)


# In[4]:


first_row=scientists.loc['William Gosset']
print(type(first_row))
print(first_row)


# In[5]:


print(first_row.index)
print(first_row.values)
print(first_row.keys())
print(first_row.index[0])
print(first_row.keys()[0])


# In[6]:


print(scientists,"\n\n")
ages=scientists['Age']
print(ages)


# In[7]:


print(ages.mean())
print(ages.min())
print(ages.max())
print(ages.std())

