from abc import ABC, abstractmethod
class Average(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def showAverage(self):
        pass

class BCIDegreeAverage(Average):
    def __init__(self, mid_marks, assignments_marks, paper_marks):
        self._mid_marks = mid_marks
        self._assignment_marks = assignments_marks
        self._paper_marks = paper_marks

    def calculate_average(self):
        total_marks = sum(self._mid_marks) + sum(self._assignment_marks) + sum(self._paper_marks)
        total_items = len(self._paper_marks)
        return round(total_marks / total_items,2)

    def showAverage(self):
        print(f"Degree Average : {self.calculate_average()}")
        print("\n-------------------------------------------------------------")


class BCIDiplomaAverage(Average):
    def __init__(self, assignments_marks, paper_marks):
        self._assignment_marks = assignments_marks
        self._paper_marks = paper_marks

    def calculate_average(self):
        total_marks = sum(self._assignment_marks) + sum(self._paper_marks)
        total_items =len(self._paper_marks)
        return round(total_marks / total_items,2)

    def showAverage(self):
        print(f"Diploma Average : {self.calculate_average()}")
        print("\n-------------------------------------------------------------")


class BCICertificateAverage(Average):
    def __init__(self, paper_marks):
        self._paper_marks = paper_marks

    def calculate_average(self):
        return round(sum(self._paper_marks) / len(self._paper_marks),2)

    def showAverage(self):
        print(f"Certificate Course Average : {self.calculate_average()}")
        print("\n-------------------------------------------------------------")
