class student:
	def __init__(self,name,age,branch,fee):
		self.name=name
		self.age=age
		self.branch=branch
		self.fee=fee
	def email(self):
		return self.name+"@gmail.com"
std1=student("jack",22,"cse",2000)
std2=student("rgv",19,"ece",3000)
print(std1.name)
print(std1.email())
print(student.email(std2))