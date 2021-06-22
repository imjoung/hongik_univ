for x in range(2,10):
	print(" # %d 단"%x, end="     ") 
print("\n")
print("="*120)

for i in range(2,10):
	for j in range(2,10):
		print("%d x %d = %2d"%(j,i,i*j),end="  ")
	print("\n")
		