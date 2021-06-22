#조건1
print("***홍익대학교 과일 판매머신 V01 ***")
print("1.orange")
print("2.strawberry")
print("3.peach")
print("4.mango")
print("5.grape")
print("6.종료")

while True:
	no=int(input("구매 번호를 입력하세요(1~6) : "))
	if no==1 :
		print("1번 orange는 1000원입니다.")
	elif no==2:
		print("2번 strawberry는 2500원입니다.")
	elif no==3:
		print("3번 peach는 1500원입니다.")
	elif no==4:
		print("4번 mango는 2000원입니다.")
	elif no==5:
		print("5번 grape는 2000원입니다.")
	else:
		print("6번 종료되었습니다.")
		break


