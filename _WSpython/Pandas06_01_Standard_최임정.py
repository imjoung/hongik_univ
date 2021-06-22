
# coding: utf-8

# In[162]:


datalist=[28,31,24,25,30,32,20,30,31,26,31]
print(datalist)
print("데이터의 총 개수는 : ",len(datalist))
dev=[] #편차
var=[] #분산


# In[163]:


def mMean():
    ave=sum(datalist)/len(datalist)
    print("데이터의 평균값은 : ",ave)
    return ave
def mMedian():
    #data sort
    datalist.sort()
    if len(datalist) % 2 ==1:
        print("데이터의 중앙값은 : ", datalist[int(len(datalist))//2])
    else:
        print("데이터의 중앙값은 : ", (datalist[int(len(datalist))//2] +
             datalist[int(len(datalist))//2]+1) /2)
def avelist(datalist):
    #평균
    return sum(datalist)/len(datalist)
def mDeviation():
    #편차
    ave=sum(datalist)/len(datalist)
    for i in datalist:
        dev.append(i-ave)
    print("데이터의 편차는 :", dev)


def mVariance():
    for a in dev:
        var.append(a**2)
    print("데이터의 분산은 : ", sum(var)/(len(var)-1))

def mStandardDeviation():
    #표준편차:분산의 제곱근
    sdv=(sum(var)/(len(var)-1))**0.5
    print("데이터의 표준편차는 : ",sdv)
    
def mRange():
    ran=max(datalist)-min(datalist)
    print("데이터의 범위는 : ",ran)
    return ran


# In[164]:


mMean()
mMedian()
mDeviation()
mVariance()
mStandardDeviation()
mRange()


# In[166]:


import pandas as pd

da=pd.Series(datalist)
print("Built-in 정렬 sort_values() : \n",da.sort_values(ascending=True))
print("Built-in 평균 mean() : %d" %da.mean())
print("Built-in 중위수 median() : %d" %da.median())
print("Built-in 분산 var() : %d" %da.var())
print("Built-in 표준편차 std() : %f" %da.std())
print("Built-in 제 1사분위수 quantile() : %d" %da.quantile(q=0.25))
print("Built-in 제 2사분위수 quantile() : %d" %da.quantile(q=0.5))
print("Built-in 제 3사분위수 quantile() : %d" %da.quantile(q=0.75))

