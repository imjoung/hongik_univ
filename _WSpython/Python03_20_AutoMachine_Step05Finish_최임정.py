menu=['오렌지','딸기','복숭아','망고','포도','종료']
money=[1000,2500,1500,2000,2000]
print("*****홍익대학교 과일 판매머신 V03*****")

for i in range(0,5):
	print("%d번 %5s : %d원"%(i+1,menu[i],money[i]))
print("6번은 %s입니다."%(menu[5]))

print("="*30)



for n in range(1,6):
	n= input("구매번호를 입력하세요 (1~5): ")
	n= int(n)
	if n==6:
		print("1에서 5까지의 숫자를 입력하세요. 종료되었습니다.")
		break
	print("선택한 과일은 %s이고 %d원입니다."%(menu[n-1],money[n-1]))


	coin= input("코인을 투입하세요: ")
	coin= int(coin)

	print("투입된 금액은 %d원 입니다."%coin)
	print("="*30)
	if (coin-money[n-1]>0):
		print("거스름돈은 %5d원 입니다."%(coin-money[n-1]))
	else :
		print("금액이 부족합니다.")
		break