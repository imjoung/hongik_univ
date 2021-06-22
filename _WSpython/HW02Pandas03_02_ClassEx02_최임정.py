class Fourcal:
	def setdata(self,first,second):
		self.first=first
		self.second=second
a=Fourcal()

Fourcal.setdata(a,2,3)
print(a.first,a.second)
a.setdata(4,5)
print(a.first,a.second)