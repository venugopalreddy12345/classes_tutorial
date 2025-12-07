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
	@classmethod
	def split_str(cls,string):
		name,age,branch,fee=string.split("-")
		return cls(name,age,branch,fee)
	@staticmethod
	def is_work_day(day):
		if day.weekday()==5 or day.weekday()==6:
			return True
		return False


std1=student("jack",22,"cse",2000)
std2=student("rgv",19,"ece",3000)

print(std1.name)
print(std1.email())
print(student.email(std2))
print(std1.raise_fee())
print(std2.raise_fee())
std3=student.split_str("bruce-21-ece-2000")
print(std3.branch)
import datetime
my_date=datetime.date(2025,12,7)
print(student.is_work_day(my_date))
class teacher(student):
	def __init__(self,name,age,branch,salary,teachername):
		super().__init__(name,age,branch,fee=None)
		self.teachername=teachername
		self.salary=salary
t1=teacher("hook",34,"cse",60000,"puri")
print(t1.teachername)