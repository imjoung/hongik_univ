names = []
names = input("4인 이상의 이름을 입력하세요 : ")
names = names.split(' ')
if len(names)>=4:
	print(names,"입력되었습니다.")
elif len(names)<4:
	print("명수를 확인하세요 (4인 이상)")


