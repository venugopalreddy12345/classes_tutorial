class student:
	percentage_raise_in_fee=1.05
	def __init__(self,name,age,branch,fee):
		self.name=name
		self.age=age
		self.branch=branch
		self.fee=fee
	def email(self):
		return self.name+"@gmail.com"
	def raise_fee(self):
		return self.fee*self.percentage_raise_in_fee
std1=student("jack",22,"cse",2000)
std2=student("rgv",19,"ece",3000)
print(std1.name)
print(std1.email())
print(student.email(std2))
print(std1.raise_fee())
print(std2.raise_fee())
