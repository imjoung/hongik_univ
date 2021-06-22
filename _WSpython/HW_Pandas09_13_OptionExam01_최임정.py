
# coding: utf-8

# In[1]:


import pandas as pd
sawonDB=pd.read_csv('../data/sawonDB.csv',header = None)

sawonDB.columns=['sabun','saname','deptno','sajob','sapay','sahire',
                'sasex','samgr']

#작은따옴표 삭제
sawonDB['saname']=sawonDB['saname'].str.strip("' '")
sawonDB['sajob']=sawonDB['sajob'].str.strip("' '")
sawonDB['sahire']=sawonDB['sahire'].str.strip("' '")
sawonDB['sasex']=sawonDB['sasex'].str.strip("' '")

#빈공간 삭제
sawonDB['saname']=sawonDB['saname'].str.strip()
sawonDB['sajob']=sawonDB['sajob'].str.strip()
sawonDB['sahire']=sawonDB['sahire'].str.strip()
sawonDB['sasex']=sawonDB['sasex'].str.strip()

sawonDB.head()


# In[2]:


name_sawon1=input("사원이름을 입력하세요 : ")

print("%s사원의 급여는 %d입니다."%(name_sawon1,sawonDB[sawonDB['saname']==name_sawon1]['sapay']))


# In[15]:


#문제 11
name_sawon2=input("사원이름을 입력하세요 : ")
if int(sawonDB[sawonDB['saname']==name_sawon2]['sapay']) >= 3000:
    print("상위소득자입니다.")
elif int(sawonDB[sawonDB['saname']==name_sawon2]['sapay']) <3000 and int(sawonDB[sawonDB['saname']==name_sawon2]['sapay']) >= 2000:
    print("중간소득자입니다.")
else :
    print("월급조정대상자입니다.")

