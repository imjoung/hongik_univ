a={'name':'imjoung','phone':'01089960000','birth':'1009'}
print(a.get('name'))
#get함수: get(key값)은 value값을 출력할 수 잇ㅆ음
print("="*20)

print(a.get('adress'))
# 없는 key값을 입력하면 none으로 돌려준다.
print(a['adress'])
#key의 오류를 발생
print("="*20)