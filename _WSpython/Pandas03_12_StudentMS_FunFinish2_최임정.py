menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ',' 9. 메뉴종료 ']
menuChk = ['1','2','3','4','9']
itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

dic = {}
deleteIDList = []
idx = 0;

#dic안에 넣는거 key값:idlist value값:scorelist
for a in range(len(idList)):
	dic[idList[a]]=scoreList[a]

print("{0:=^66}".format(" 메 뉴 선 택 "))
for i in range(0,5):
	print(menu[i],end=" ")
print(end="\n")
print("="*70)
#----------------------------------------------------

def Mainpg():
	Nummenu=int(input("{0:^58}".format("메뉴의 번호를 선택하세요")))
	if Nummenu ==1:
		DelID()
	elif Nummenu ==2:
		SignIn()
	elif Nummenu ==3:
		PrintList(Nummenu)
		
	elif Nummenu ==4:
		PassList()
	elif Nummenu ==9:
		exit()
	else :
		print("\t\t 없는 번호입니다. 다시 입력해주세요")
#----------------------------------------------------
def inputData():
	for jj in range(len(idList)):
		dic[idList[jj]]=scoreList[jj]
#----------------------------------------------------
def Passchk(j):
	if (sum(dic[j])/3)>=70:
		print("합격")
	else :
		print("불합격")

def PrintList(Nummenu):
	print(menu[Nummenu-1])
	for ML in range(len(MenuList)):
		print(MenuList[ML],end="\t ")
	print()
	print("="*80)
	
	for j in dic.keys():
		print("%s \t %d \t %d \t %d \t %d \t %.2f"%(j,dic[j][0],dic[j][1],dic[j][2],sum(dic[j]),(sum(dic[j])/3)),"\t",end=' ')
		Passchk(j)

#----------------------------------------------------

def DelID():
	print("\t\t 회원 삭제 Algorithm Chk")
	deleteID =input("\t\tID를 입력하세요: ")
	if deleteID in idList:
		print("\t\t아이디가 있습니다.")
		del dic[deleteID]
		print("\t\tID : %s가 삭제되었습니다."%deleteID)
		deleteIDList.append(deleteID)

	elif deleteIDList not in idList:
		print("\t\t해당 ID가 없습니다.")



#----------------------------------------------------

def SignIn():
	print("\t\t 추가 등록 Algorithm Chk")
	plusID=input("\t\tID를 입력하세요: ")
	if plusID in deleteIDList:
		print("\t\t탈퇴한 회원은 가입이 불가합니다.")
	elif plusID in idList:
		print("\t\t중복 아이디가 있습니다.")
	else:
		a=int(input("필기값을 입력하세요: "))
		b=int(input("실기값을 입력하세요: "))
		c=int(input("인성값을 입력하세요: "))
		dic[plusID]=[a,b,c]

		
		


#----------------------------------------------------

def PassList():
	print("\t\t 합격생 목록 Algorithm Chk")
	
while True:
	Mainpg()
	'''
	Nummenu=int(input("{0:^58}".format("메뉴의 번호를 선택하세요")))
	if Nummenu == 1:
		DelID()
	elif Nummenu==2:
		SignIn()
	elif Nummenu==3:
		for i in range(len(dic)):
			inputData()
		PrintList()
		print("\n")

	elif Nummenu==4:
		PassList()
		
	elif Nummenu==9:
		print("%s"%menu[4])
		break
	else :
		print("번호를 확인하세요")
		exit()
	'''