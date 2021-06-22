a=1
def vartest(a):
	a=a+1
	return a

a=vartest(a)
print(a)

print("="*20)

#global은 외부의 변수를 직접 사용할때 사용. 권장은 x 
a=1
def vartest():
	global a
	a = a+1
vartest()
print(a)
