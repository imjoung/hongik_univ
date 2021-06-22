
# coding: utf-8

# In[9]:


import pandas as pd
deptDB=pd.read_csv('../data/deptDB.csv',header = None)
sawonDB=pd.read_csv('../data/sawonDB.csv',header = None)
gogekDB=pd.read_csv('../data/gogekDB.csv',header = None)

deptDB.columns=['deptno','dname','loc']
sawonDB.columns=['sabun','saname','deptno','sajob','sapay','sahire',
                'sasex','samgr']
gogekDB.columns=['gobun','goname','gotel','gojumin','godam']

#작은따옴표 삭제
sawonDB['saname']=sawonDB['saname'].str.strip("' '")
sawonDB['sajob']=sawonDB['sajob'].str.strip("' '")
sawonDB['sahire']=sawonDB['sahire'].str.strip("' '")
sawonDB['sasex']=sawonDB['sasex'].str.strip("' '")

deptDB['dname']=deptDB['dname'].str.strip("' '")
deptDB['loc']=deptDB['loc'].str.strip("' '")

gogekDB['goname']=gogekDB['goname'].str.strip("' '")
gogekDB['gotel']=gogekDB['gotel'].str.strip("' '")
gogekDB['gojumin']=gogekDB['gojumin'].str.strip("' '")

#빈공간 삭제
sawonDB['saname']=sawonDB['saname'].str.strip()
sawonDB['sajob']=sawonDB['sajob'].str.strip()
sawonDB['sahire']=sawonDB['sahire'].str.strip()
sawonDB['sasex']=sawonDB['sasex'].str.strip()

deptDB['dname']=deptDB['dname'].str.strip()
deptDB['loc']=deptDB['loc'].str.strip()

gogekDB['goname']=gogekDB['goname'].str.strip()
gogekDB['gotel']=gogekDB['gotel'].str.strip()
gogekDB['gojumin']=gogekDB['gojumin'].str.strip()


# In[10]:


sajobChk=sawonDB[(sawonDB['sajob']=='대리')|(sawonDB['sajob']=='사원')]
sajobChk


# In[12]:


print(sajobChk.groupby(['sajob'])['sabun'].count(), "\n")
print(sajobChk.groupby(['sajob'])['sabun'].count()>=4, "\n")
print((sajobChk.groupby(['sajob'])['sabun'].count()>=4).values, "\n")

sajobCntChk=(sajobChk.groupby(['sajob'])['sabun'].count()>=4)
print(sajobCntChk)

sajobChkResult=sajobCntChk[sajobCntChk.values]
print(sajobChkResult)


# In[ ]:


#문제9
q9_job_meanpay = sawonDB['sajob'].unique()
a=sawonDB.groupby('sajob')['sapay'].count()
print(q9_job_meanpay)

for idx in q9_job_meanpay:
    payMeanlst = []
    chk = sawonDB[sawonDB['sajob'] == idx]
    if sawonDB.groupby('sajob')['sapay'].count()[idx] >=4:
        if idx == '사원':
            chkAll = sawonDB[sawonDB['sajob'] == idx]
            print("%s님들의 평균 급여는 %.2f입니다."%(idx,chkAll['sapay'].mean()))
        elif idx == '대리':
            chkAll = sawonDB[sawonDB['sajob'] == idx]
            print("%s님들의 평균 급여는 %.2f입니다."%(idx,chkAll['sapay'].mean()))

