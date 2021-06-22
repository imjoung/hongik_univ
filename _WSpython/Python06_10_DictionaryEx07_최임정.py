a={'name':'imjoung','phone':'01089960000','birth':'1009'}
print(a.get('adress','bar'))
#딕셔너리 안에 찾으려는 key값(adress)가 없을 경우 디폴트 값(bar"-")을 정할 수 있음
print("="*20)

a={'name':'imjoung','phone':'01089960000','birth':'1009'}
print('name'in a)
print('email' in a)
#in을 이용해 해당 key가 딕셔너리 안에 있는지 조사하기 