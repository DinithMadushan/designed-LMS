from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self,emp_id,name):
        self.__emp_id = emp_id
        self.__name = name

    @abstractmethod
    def showEmployee(self):
        print("Employee ID : {}\nEmployee Name : {}".format(self.__emp_id,self.__name))

class BCI_salary_Employee(Employee):
    def __init__(self,emp_id,name):
        super().__init__(emp_id,name)

    def showEmployee(self):
        super().showEmployee()
        print("\n-------------------------------------------------------------")

class BCI_Lecture_Employee(BCI_salary_Employee):
    def __init__(self,emp_id,name):
        super().__init__(emp_id,name)
    def showEmployee(self):
        super().showEmployee()
        print("\n-------------------------------------------------------------")


class BCI_Admin_Employee(BCI_salary_Employee):
    def __init__(self,emp_id,name):
        super().__init__(emp_id,name)
    def showEmployee(self):
        super().showEmployee()
        print("\n-------------------------------------------------------------")


class BCI_com_basedEmployee(Employee):
    def __init__(self,emp_id,name):
        super().__init__(emp_id,name)

    def showEmployee(self):
        super().showEmployee()
        print("\n-------------------------------------------------------------")


class BCI_Marketing_Employee(BCI_com_basedEmployee):
    def __init__(self,emp_id,name):
        super().__init__(emp_id,name)
    def showEmployee(self):
        super().showEmployee()
        print("\n-------------------------------------------------------------")


class BCI_part_time_Employee(Employee):
    def __init__(self,emp_id,name):
        super().__init__(emp_id,name)

    def showEmployee(self):
        super().showEmployee()
        print("\n-------------------------------------------------------------")


class BCI_Cleaner_Employee(BCI_part_time_Employee):
    def __init__(self,emp_id,name):
        super().__init__(emp_id,name)
    def showEmployee(self):
        super().showEmployee()
        print("\n-------------------------------------------------------------")
