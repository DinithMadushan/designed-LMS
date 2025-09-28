from abc import ABC, abstractmethod
class Course(ABC):

    def __init__(self,courseName,courseCode,courseCredit,courseFee):
        self.__courseName = courseName
        self.__courseCode = courseCode
        self.__courseCredit = courseCredit
        self.__courseFee  = courseFee

    @abstractmethod
    def showCourses(self):
        print(" Course name : {}\n Course code : {}\n Course credits : {}\n Course Fee : {}".format(self.__courseName,self.__courseCode,self.__courseCredit,self.__courseFee))


class BCIDegree(Course):
    
    def __init__(self,courseName,courseCode,courseCredit,courseFee):
        super().__init__(courseName,courseCode,courseCredit,courseFee)

    def showCourses(self):
        super().showCourses()
        print("\n-------------------------------------------------------------")


class BCIDiploma(Course):

    def __init__(self,courseName,courseCode,courseCredit,courseFee):
        super().__init__(courseName,courseCode,courseCredit,courseFee)

    def showCourses(self):
        super().showCourses()
        print("\n-------------------------------------------------------------")

class BCICertificate(Course):
    
    def __init__(self,courseName,courseCode,courseCredit,courseFee):
        super().__init__(courseName,courseCode,courseCredit,courseFee)

    def showCourses(self):
        super().showCourses()
        print("\n-------------------------------------------------------------")