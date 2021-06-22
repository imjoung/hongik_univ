
# coding: utf-8

# ### 기본 함수 선언 연습 01
# <h1> 기본 연습 </h1>
# <h2> 기본 연습 </h2>
# <h3> 기본 연습 </h3>
# <h4> 기본 연습 </h4>
# <h5> 기본 연습 </h5>
# HTML : Hyper Text Markup Language

# In[3]:


def add(a,b):
    return a+b
a=3
b=4
c=add(a,b)

print("%d + %d = : %d"%(a,b,c))


# In[4]:


def add(a,b):
    return a,b,a+b
a,b,result=add(b=5,a=3)
print("%d + %d = %d"%(b,a,result))


# In[5]:


def say():
    return 'Hi'
print(say())


# In[8]:


def add2(a,b):
    print("%d, %d의 합은 %d입니다."%(a,b,a+b))
print(add2(3,4))


# In[9]:


def say2():
    print('Hi')
    
say2()

