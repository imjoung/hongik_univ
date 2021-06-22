
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv('../data/gapminder.tsv',sep='\t')
unList=df['year'].unique()


# In[17]:


for idx in unList:
    print(idx,"년 ====> 1 :")
    grYear=df[df['year'] == idx]
    print("총", len(grYear),"개 \n ====> 2 :\n", grYear.head(3),
         "\n ====> 3 (총개수, 컬럼개수) : ", grYear.shape)
    print(idx,"년의 평균값은 : ",grYear["lifeExp"].mean())
    print("\n", "="*50, "\n")

