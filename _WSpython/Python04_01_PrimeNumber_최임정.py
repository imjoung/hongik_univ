
count=0

while True:
	n=int(input("20이상의 수를 입력하세요: "))

	if 0 <n <20 :
		print("범위에 맞는 값을 입력하세요:")
	
	elif n>=20:
		for x in range(1,n+1):
			for y in range(1,x+1):
				if x%y ==0:
					count=count+1

			if count==2:
				print("%d 소수 O"%x)
				count=0
			elif count>2:
				print("%d 소수 X"%x)
				count=0
			elif count<2:
				print("%d 소수 X"%x)
				count=0
					
	else :
		print("0을 입력하여 종료되었습니다.")
		break

