
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
deptDB=pd.read_csv('../data/deptDB.csv',header = None)
sawonDB=pd.read_csv('../data/sawonDB.csv',header = None)
gogekDB=pd.read_csv('../data/gogekDB.csv',header = None)


# In[ ]:


deptDB


# In[ ]:


deptDB.columns=['deptno','dname','loc']
deptDB.head()


# In[2]:


sawonDB.columns=['sabun','saname','deptno','sajob','sapay','sahire',
                'sasex','samgr']
sawonDB.head()


# In[ ]:


gogekDB.columns=['gobun','goname','gotel','gojumin','godam']
gogekDB.head()


# In[ ]:


gogekDB.replace("'","", regex=True)


# In[25]:


sawonDB.replace("'","", regex=True)


# In[ ]:


deptDB.replace("'","", regex=True)


# In[56]:


#문제1
for i in range (len(sawonDB)):
   if sawonDB['sahire'][i][4:6]=='88':
    print(sawonDB.loc[i],'\n','='*20)


# In[64]:


#문제2
for a in range (len(sawonDB)):
   if sawonDB['sahire'][a][7:9]=='04':
    print(sawonDB.loc[a],'\n','='*20)

