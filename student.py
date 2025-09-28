from abc import ABC, abstractmethod
class Student(ABC):
    def __init__(self,stud_id,stud_name,stud_course,stud_batch,stud_DOB):
        self.__stud_id = stud_id
        self.__stud_name = stud_name
        self.__stud_course = stud_course
        self.__stud_batch = stud_batch
        self.__stud_DOB = stud_DOB

    @abstractmethod
    def showStudents(self):
        print("Student ID : {}\nStudent name : {}\nStudent course : {}\nStudent batch : {}\nDate of birth : {}".format(self.__stud_id,self.__stud_name,self.__stud_course,self.__stud_batch,self.__stud_DOB))


class BCIdegreeStudent(Student):
    def __init__(self,stud_id,stud_name,stud_course,stud_batch,stud_DOB):
        super().__init__(stud_id,stud_name,stud_course,stud_batch,stud_DOB)


    def showStudents(self):
        super().showStudents()


class BCIdiplomaStudent(Student):
    def __init__(self,stud_id,stud_name,stud_course,stud_batch,stud_DOB):
        super().__init__(stud_id,stud_name,stud_course,stud_batch,stud_DOB)
        

    def showStudents(self):
        super().showStudents()


class BCIcertificateStudent(Student):
    def __init__(self,stud_id,stud_name,stud_course,stud_batch,stud_DOB):
        super().__init__(stud_id,stud_name,stud_course,stud_batch,stud_DOB)


    def showStudents(self):
        super().showStudents()