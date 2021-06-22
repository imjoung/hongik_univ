def say_myself(name,old,man=True):
	print("나의 이름은 %s입니다." %name)
	print("나이는 %d살입니다." %old)
	if man:
		print("남자입니다.")
	else:
		print("여자입니다.")
say_myself("소나무",27)
print("="*20)
say_myself("최임정",26,False)
print("="*20)

#say_myself 함수에 3개의 매개변수 초깃값을 미리 설정하고
#마지막 인수인 man이 true이면 남자입니다. 아니면 여자입니다를 출력