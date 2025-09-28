from abc import ABC, abstractmethod
class Salary(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def showsalary(self):
        pass

class BCINonAcademicSalary(Salary):
    def __init__(self,name,salary,commission):
        super().__init__(name)
        self.salary = salary
        self.commission = commission

    def cal_salary(self):
        return self.salary +self.commission

    def showsalary(self):
        print("Employee name : {}\nSalary : Rs.{}\nCommission : Rs.{}".format(self.name,self.cal_salary(),self.commission))
        print("----------------------------------------------------------------\n")

class BCIAcademicSalary(Salary):
    def __init__(self,name,hourly_rate,hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def cal_salary(self):
        return self.hourly_rate * self.hours_worked
    
    def showsalary(self):
        print("Employee name : {}\nSalary : Rs.{}".format(self.name,self.cal_salary()),)
        print("----------------------------------------------------------------\n")

        


