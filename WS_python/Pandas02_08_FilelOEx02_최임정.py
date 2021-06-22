f1=open("새파일.txt",'r')
line =f1.readline()
print(line)
f1.close()
print("="*30)

f=open("새파일.txt",'r')
line=f2.read()
print(line)

#while True:
#	line=f2.readline()
#	if not line : break
#	print(line)
f2.close()