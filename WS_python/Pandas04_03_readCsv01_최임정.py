
# coding: utf-8

# In[8]:


import pandas
df=pandas.read_csv("./../DataSet/read_csv_sample.csv")
import pandas as pd


# In[9]:


file_path="C:/_WShongik210518/DataSet/read_csv_sample.csv"
df=pd.read_csv(file_path)
print(df)
print(type(df))

