
# coding: utf-8

# In[40]:


datalist=[28,31,24,25,30,32,20,30,30,31,26,31]
print(datalist)
print("데이터의 총 개수는 : ",len(datalist))


# In[62]:


def mMean():
    print("데이터의 평균값은 : ",sum(datalist)/len(datalist))
def mMedian():
    #data sort
    datalist.sort()
    if len(datalist) % 2 ==1:
        print("데이터의 중앙값은 : ", datalist[int(len(datalist))//2])
    else:
        print("데이터의 중앙값은 : ", (datalist[int(len(datalist))//2] +
             datalist[int(len(datalist))//2]+1) /2)


# In[63]:


mMean()


# In[64]:


mMedian()

