
# coding: utf-8

# In[48]:


import pandas as pd
deptDB=pd.read_csv('../data/deptDB.csv',header = None)
sawonDB=pd.read_csv('../data/sawonDB.csv',header = None)
gogekDB=pd.read_csv('../data/gogekDB.csv',header = None)

deptDB.columns=['deptno','dname','loc']
sawonDB.columns=['sabun','saname','deptno','sajob','sapay','sahire',
                'sasex','samgr']
gogekDB.columns=['gobun','goname','gotel','gojumin','godam']
sawonDB.head()


# In[50]:


#작은따옴표 삭제
sawonDB['saname']=sawonDB['saname'].str.strip("' '")
sawonDB['sajob']=sawonDB['sajob'].str.strip("'  '")
sawonDB['sahire']=sawonDB['sahire'].str.strip("' '")
sawonDB['sasex']=sawonDB['sasex'].str.strip("' '")


# In[52]:


#빈공간 삭제
sawonDB['saname']=sawonDB['saname'].str.strip()
sawonDB['sajob']=sawonDB['sajob'].str.strip()
sawonDB['sahire']=sawonDB['sahire'].str.strip()
sawonDB['sasex']=sawonDB['sasex'].str.strip()

sawonDB.head()


# In[36]:


#문제1
q1_lst88=[]
for idx in range(len(sawonDB)):
    q1_lst88.append(sawonDB['sahire'].str.strip()[idx][0:4] =='1988')
sawonDB.loc[q1_lst88]


# In[5]:


#문제2
q2_lst04=[]
for idx in range(len(sawonDB)):
    q2_lst04.append(sawonDB['sahire'][idx][6:8] == '04')
sawonDB.loc[q2_lst04]

