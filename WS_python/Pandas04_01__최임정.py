
import random
lst=[]

def recursive(m) :
	if(chk == len(lst)) :   #인원수 == 숫자
		return

	for i in range(m) :
		num = random.randint(1,len(name))
		if num not in lst :
			lst.append(num)  # 3:2
		else:
			recursive(chk -len(lst))  # 2

while True :
	name = input("4인 이상의 이름을 입력하세요. (Space Bar로 구분한다.)") .split()
	if len(name) >=4 :
		for i in name :
			print(i,end=' ')
		print('')

		chk = len(name)
		lst=[]
		cnt=0

		recursive(chk)
		print(lst)