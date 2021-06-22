
# coding: utf-8

# In[15]:


import pandas as pd
student1=pd.Series({'국어':100,'영어':80,'수학':90})
print(student1, '\n')

percentage = student1 / 200 
#student1이 숫자로 구성되어 있기 때문에 숫자로 나누면 다 나눠짐 숫자상관x

print(percentage, '\n')
print("percentage type: ",type(percentage))

student2=pd.Series({'수학':80,'국어':90,'영어':80})

addition = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1/student2
print("division type: ",type(division), '\n')

#사칙연산 결과를 데이터프레임으로 합치기 (시리즈>데이터프레임)
result=pd.DataFrame([addition,subtraction,multiplication,division],
                   index=['덧셈','뺄셈','곱셈','나눗셈'])
print(result,'\n',"result type: ",type(result),'\n\n')
print("덧셈: ","\n",addition,'\n\n',"뺄셈: ","\n",subtraction,'\n\n',
      "곱셈: ","\n",multiplication,'\n\n',"나눗셈: ","\n",division)

