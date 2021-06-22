
# coding: utf-8

# In[11]:


import pandas as pd
df1=pd.read_excel("./../DataSet/datalabPractice01.xlsx")
df2=pd.read_excel("./../DataSet/datalabPractice01.xlsx",                  sheet_name="Sheet1",usecols=[0,1,2],skiprows=[0],                  skipfooter=2, header = None)
print(df2.columns,"\n")
print(df2,"\n")
print(df1)

