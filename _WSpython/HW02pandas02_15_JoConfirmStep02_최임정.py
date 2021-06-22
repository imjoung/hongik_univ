import random

while True:
	a_list=[]
	new_list=[]
	a_list=input("4인 이상의 이름을 입력하세요.(종료:0): ").split()
	if '0' in a_list:
		print("종료되었습니다.")
		exit()
	elif len(a_list)<4:
		print("^\t명수를 확인하세요.")
		continue

	elif len(a_list)>=4:
			num=random.randint(1,len(a_list))
			for x in range(0,len(a_list)):
				for y in range(1,len(a_list)):
					if a_list[x] != a_list[y]:
						new_list.append(a_list[x])
						break
				else :
					print("중복되었습니다.")
					break
	for i in new_list:
		print(i,end=' ')

