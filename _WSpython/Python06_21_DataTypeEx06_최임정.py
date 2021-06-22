vi01=20
vi02=30
print("교환전 값 :",vi01,vi02)

temp=vi01 #temp에 vi01을 대입
vi01=vi02 #vi01에 vi02를 대입
vi02=temp #vi02에 temp를 대입 
# => vi01과 vi02의 값이 바뀜

print("교환후 값 :",vi01,vi02)

a=3
b=5
print("교환전 값:",a,b)
a,b=b,a #a를 b로 b를a로 바꿈
print("교환후 값:",a,b)