
# coding: utf-8

# In[37]:


import pandas as pd
deptDB=pd.read_csv('../data/deptDB.csv',header = None)
sawonDB=pd.read_csv('../data/sawonDB.csv',header = None)
gogekDB=pd.read_csv('../data/gogekDB.csv',header = None)

deptDB.columns=['deptno','dname','loc']
sawonDB.columns=['sabun','saname','deptno','sajob','sapay','sahire',
                'sasex','samgr']
gogekDB.columns=['gobun','goname','gotel','gojumin','godam']
sawonDB.head()


# In[56]:


#작은따옴표 삭제
sawonDB['saname']=sawonDB['saname'].str.strip("' '")
sawonDB['sajob']=sawonDB['sajob'].str.strip("' '")
sawonDB['sahire']=sawonDB['sahire'].str.strip("' '")
sawonDB['sasex']=sawonDB['sasex'].str.strip("' '")

deptDB['dname']=deptDB['dname'].str.strip("' '")
deptDB['loc']=deptDB['loc'].str.strip("' '")

sawonDB.head()


# In[53]:


#빈공간 삭제
sawonDB['saname']=sawonDB['saname'].str.strip()
sawonDB['sajob']=sawonDB['sajob'].str.strip()
sawonDB['sahire']=sawonDB['sahire'].str.strip()
sawonDB['sasex']=sawonDB['sasex'].str.strip()

sawonDB.head()


# In[40]:


#문제1
q1_lst88=[]
for idx in range(len(sawonDB)):
    q1_lst88.append(sawonDB['sahire'].str.strip()[idx][0:4] =='1988')
sawonDB.loc[q1_lst88]


# In[41]:


#문제2
q2_lst04=[]
for idx in range(len(sawonDB)):
    q2_lst04.append(sawonDB['sahire'][idx][6:8] == '04')
sawonDB.loc[q2_lst04]


# In[42]:


#문제3
q3_sabun=sawonDB[sawonDB['sabun']%2 == 0]
q3_sabun


# In[43]:


#문제1,2,3 
sawon_1998 = sawonDB[sawonDB['sahire'].str.contains('1988')]
print(sawon_1998,"\n")

sawon_april = sawonDB[sawonDB['sahire'].str.contains('/04')]
print(sawon_april,"\n")

slist=[]
for i,value in enumerate(sawonDB['sabun']):
    if value %2 ==0:
        slist.append(i)
print(sawonDB.iloc[slist])


# In[44]:


#문제4
q4_job_pay = sawonDB.groupby('sajob')['sapay'].mean()
print(q4_job_pay,"\n")

#####반증
job_lst = sawonDB['sajob'].unique()
print(job_lst)
for idx in job_lst:
    chkAll = sawonDB[sawonDB['sajob'] == idx]
    print("%s님의 급여는 %.2f입니다." %(idx,chkAll['sapay'].mean()))


# In[45]:


#문제5
q5_job_pay = sawonDB.groupby(['sajob','sasex'])['sapay'].mean()
print(q5_job_pay)


# In[46]:


#문제6
q6_pay_inc = sawonDB['sapay']+(sawonDB['sapay'] *0.1)
sawonDB['sainc_pay'] = q6_pay_inc
sawonDB


# In[57]:


#문제7
q7_com_30 = sawonDB[sawonDB['deptno'] == 30]
print("전산부 직원의 평균 연봉 : ", q7_com_30['sapay'].mean())


# In[58]:


#merge를 이용해서 dept와 sawon을 deptno로 연결 
deptSawon = deptDB.merge(sawonDB, how='inner', on = 'deptno')
deptSawon.tail()


# In[60]:


#문제7
q7_com_30 = deptSawon[deptSawon['dname'] == '전산부']
print("전산부 직원의 평균 연봉 : ", q7_com_30['sapay'].mean())


# In[59]:


#문제8
columnsSort = sawonDB.columns.sort_values(ascending=True)
print(columnsSort)

sawonDB[columnsSort]


# In[29]:


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

