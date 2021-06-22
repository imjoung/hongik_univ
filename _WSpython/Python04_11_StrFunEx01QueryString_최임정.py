vurl="https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=7&acq=python&qdt=0&ie=utf8&query=python"
a=(vurl.split('?')and vurl.split('&'))
print(a)
del a[0]
print(a)

print("Querystring의 개수: %d"%len(a))

