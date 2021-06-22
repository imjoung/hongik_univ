
# coding: utf-8

# In[58]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
deptDB=pd.read_csv('../data/deptDB.csv',header = None)
sawonDB=pd.read_csv('../data/sawonDB.csv',header = None)
gogekDB=pd.read_csv('../data/gogekDB.csv',header = None)


# In[59]:


deptDB


# In[60]:


deptDB.columns=['deptno','dname','loc']
deptDB.head()


# In[61]:


sawonDB.columns=['sabun','saname','deptno','sajob','sapay','sahire',
                'sasex','samgr']
sawonDB.head()


# In[62]:


gogekDB.columns=['gobun','goname','gotel','gojumin','godam']
gogekDB.head()


# In[63]:


gogekDB.replace("'","", regex=True)


# In[64]:


sawonDB.replace("'","", regex=True)


# In[65]:


deptDB.replace("'","", regex=True)

