klist=[2,5,6,1,2,8,33,77,12]
#print(klist.sort())
temp=0

for i in range (len(klist)):
	for j in range (len(klist)):
		if klist[i]>klist[j]:
			continue
		elif klist[i]<klist[j]:

			temp=klist[j]
			klist[j]=klist[i]
			klist[i]=temp
			#빈 공간인 temp에 klist[j]를 넣고
			#klist[j]에는 [i]를 넣고
			#[i]에 temp를 넣으면
			#결국엔 i와 j는 바뀌게 된다 
			
			
print(klist)
klist.reverse()
print(klist)