f=open("새파일.txt",'r')
lines=f.readlines()
print(lines)

print("="*30)

for line in lines:
	print(line)
f.close()
