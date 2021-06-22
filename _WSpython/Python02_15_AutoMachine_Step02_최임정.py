menu=['오렌지','딸기','복숭아','망고','포도','종료']
money=[1000,2500,1500,2000,2000]
print("*****홍익대학교 과일 판매머신 V03*****")

for i in range(0,5):
	print(i+1,"번",menu[i],":",money[i],"원")
print("==============================")

while True:
	n= input("구매번호를 입력하세요 (1~6): ")
	n= int(n)
	if n == 1:
		print(menu[n-1], "는", money[n-1], "원입니다.")
	elif n ==2:
		print(menu[n-1], "는", money[n-1], "원입니다.")
	elif n ==3:
		print(menu[n-1], "는", money[n-1], "원입니다.")
	elif n ==4:
		print(menu[n-1], "는", money[n-1], "원입니다.")
	elif n ==5:
		print(menu[n-1], "는", money[n-1], "원입니다.")
	else:
		print("종료되었습니다.")
		break
