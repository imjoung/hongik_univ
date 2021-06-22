
# coding: utf-8

# In[124]:


datalist=[28,31,24,25,30,32,20,30,31,26,31]
print(datalist)
print("데이터의 총 개수는 : ",len(datalist))


# In[159]:


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
def mDeviation():
    #편차
    ave=sum(datalist)/len(datalist)
    dev=[]
    for i in datalist:
        dev.append(i-ave)
    print("데이터의 편차는 :", end=' ')
    for j in dev:
        print(j,end='  ')


# In[160]:


mMean()
mMedian()
mDeviation()

