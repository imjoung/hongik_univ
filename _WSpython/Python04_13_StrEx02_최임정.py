#[0:2]는 l i 까지 0,1만 출력
#-0이나 +0이나 같다
#그래서 -는 맨 오른쪽부터 -1로 시작 


a="Life is too short, You need Python"
print(a[3],a[0],a[12],a[-1],a[-0],a[-2],a[-5])

print(a[0:2],a[5:7],a[12:17])
print(a[19:])
print(a[:5])
print(a[:])
print(a[19:-7])