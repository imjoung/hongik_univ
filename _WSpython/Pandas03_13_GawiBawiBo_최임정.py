import sys
import random
bawi=['가위','바위','보']

def gawi():
	if int(xx) == usermenu :
		print("비겼습니다.")
	elif int(xx) > usermenu :
		print("computer가 이겼습니다.")
	elif int(xx) < usermenu :
		print("user가 이겼습니다.")


menulist=['1.가위','2.바위','3.보','9.종료']
for i in menulist:
	print(i,end=" ")
print("\n")
while True:
	usermenu = int(input("번호를 선택하세요: "))
	if usermenu ==9:
		print("종료되었습니다.")
		sys.exit()
	elif usermenu >=4 or usermenu ==0:
		print("번호를 확인하세요")
	elif usermenu <4 and usermenu >0:
		xx=random.randint(1,3)
		print("com : ",bawi[xx-1],"/","User : ",bawi[usermenu-1])
		gawi()

