#Q1.
kor=80
eng=75
math=55
sum=kor+eng+math
ave=sum/3
print(ave)

#Q2.
print("="*15)
x=13
if x%2==0:
	print("x는 짝수입니다.")
else : 
	print("x는 홀수입니다.")
#2로 나누었을때 나머지수가 1이면 홀수, 0이면 짝수이다.

#Q3.
print("="*15)
pin="881120-1068234"
yyyymmdd=pin[:6] #0부터5까지
num=pin[7:] #7부터끝까지
print(yyyymmdd)
print(num)

#Q4.주민번호 성별을 나타내는 숫자 출력(뒷자리에서 첫번째)
print("="*15)
pin="881120-1068234"
print(pin[7])

#Q5.
print("="*15)
a="a:b:c:d"
b=a.replace(":","#")
print(b)

#Q6.
print("="*15)
a=[1,3,5,4,2]
a.sort() #오름차순정렬
print(a)
a.reverse() #내림차순정렬
print(a)

#Q7.
print("="*15)
a=['Life','is','too','short']
result=" ".join(a) #a리스트를 다 띄워서 result에 join
print(result)

#Q8.
print("="*15)
a=(1,2,3)
a=a+(4,)
print(a)

#Q9.
print("="*15)
a=dict()
a['name']='python'
a[('a',)]='python'
#a[[1]]='python' [1]은 리스트라 변할수 있다. 딕셔너리key값에 어울리지 않는다.
a[250]='python'


#Q10.B에 해당하는 값 출력
print("="*15)
a={'A':90,'B':80,'C':70}
result=a.pop('B')
print(a)
print(result)

#Q11.
print("="*15)
a=[1,1,1,2,2,3,3,3,4,4,5]
aSet=set(a)
b=list(aSet)
print(b)

#Q12.
print("="*15)
a=b=[1,2,3]
a[1]=4
print(b)
#a와b는 같다. a[1]값이 변경되니까 자동으로 b[1]값도 바뀐다.
