
fruit=['apple','melon','grape','strawberry']
r=[]
a=0

while True:
	n=int(input("10이상의 수를 입력하세요: "))

	if 0 <n <10 :
		print("10이상의 수를 입력하세요:")
	
	elif n>=10:
		for x in range(1,n+1):

			r.append(a)
			if len(r)%3==0:
				print("%d. "%x+'[apple]')
			if len(r)%4==0:
				print("%d. "%x+'[melon]')
			if len(r)%5==0:
				print("%d. "%x+'[grape]')
			if len(r)%8==0:
				print("%d. "%x+'[strawberry]')
			else :
				print("%d. "%x)
			

			

			'''

			if count%3==0:
				print("%d. [%s]"%(x,fruit[0]))

				
			elif count%4==0:
				print("%d. [%s]"%(x,fruit[1]))
				
			elif count%5==0:
				print("%d. [%s]"%(x,fruit[2]))
				
			elif count%8==0:
				print("%d. [%s]"%(x,fruit[3]))
				
			else:
				print("%d."%x)
			'''		
	else :
		print("0을 입력하여 종료되었습니다.")
		break


