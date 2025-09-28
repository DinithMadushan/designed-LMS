from abc import ABC, abstractmethod
class Falcuties(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def showFaculties(self):
        pass


class BCIFaculties(Falcuties):
    def __init__(self,name):
        super().__init__(name)

    def showFaculties(self):
        print("Faculty name : ",self.name)



