
# coding: utf-8

# In[11]:


import pandas
df=pandas.read_csv("./../DataSet/read_csv_sample.csv")
import pandas as pd


# In[14]:


file_path="C:/_WShongik210518/DataSet/read_csv_sample.csv"
df=pd.read_csv(file_path,header=None)
print(df)
print(type(df))
df1=pd.read_csv(file_path,index_col='c0')
print(df1)

