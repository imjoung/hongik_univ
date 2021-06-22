
# coding: utf-8

# In[48]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
deptDB=pd.read_csv('../data/deptDB.csv',header = None)
sawonDB=pd.read_csv('../data/sawonDB.csv',header = None)
gogekDB=pd.read_csv('../data/gogekDB.csv',header = None)


# In[49]:


deptDB


# In[44]:


deptDB.columns=['deptno','dname','loc']
deptDB.head()


# In[45]:


sawonDB.columns=['sabun','saname','deptno','sajob','sapay','sahire',
                'sasex','samgr']
sawonDB.head()


# In[46]:


gogekDB.columns=['gobun','goname','gotel','gojumin','godam']
gogekDB.head()

