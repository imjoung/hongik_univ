
# coding: utf-8

# In[6]:


import pandas
df=pandas.read_csv('../data/gapminder.tsv',sep='\t')
print(type(df))
print(type(df['pop']))


# In[7]:


grouped_year_df=df.groupby('year')
print(type(grouped_year_df))
print(grouped_year_df['pop'])


# In[8]:


grouped_year_df['pop'].mean()

