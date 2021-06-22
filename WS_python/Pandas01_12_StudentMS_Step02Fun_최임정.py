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

def inputData():
	for jj in range(len(idList)):
		dic[idList[jj]]=scoreList[jj]

def PrintList():
	print(menu[Nummenu-1])
	for ML in range(len(MenuList)):
		print(MenuList[ML],end="\t")
	print()
	print("="*80)
	for j in dic.keys():
		print("%s \t %d \t %d \t %d \t %d"%(j,dic[j][0],dic[j][1],dic[j][2],sum(dic[j])))

	

for a in range(len(idList)):
	dic[idList[a]]=scoreList[a]

print("{0:=^66}".format(" 메 뉴 선 택 "))
for i in range(0,5):
	print(menu[i],end=" ")
print(end="\n")
#print("%s %s %s %s %s"%(menu[0],menu[1],menu[2],menu[3],menu[4]))
print("="*70)

while True:
	Nummenu=int(input("{0:^58}".format("메뉴의 번호를 선택하세요")))
	if Nummenu == 1:
		print("%s"%menu[0])
	elif Nummenu==2:
		print("%s"%menu[1])
	elif Nummenu==3:
		'''
		print("%s"%menu[2])
		

		for x in range(0,7):
			print(MenuList[x],end="\t")
		print(end="\n")
		'''
		for i in range(len(dic)):
			inputData()
		PrintList()
		print("\n")

	elif Nummenu==4:
		print("%s"%menu[3])
		
	elif Nummenu==9:
		print("%s"%menu[4])
		break
	else :
		print("번호를 확인하세요")