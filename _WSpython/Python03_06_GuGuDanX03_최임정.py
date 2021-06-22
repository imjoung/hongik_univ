'''
다중 for문: for문 안에 for문

outer for 
	inner for
'''




for i in range(2,4):
	print("outer : ", i)
	for j in range(1,4):
		print("inner : ", j,end = " ")
