from abc import ABC, abstractmethod
class Contact(ABC):
    def __init__(self,address,phone,email):
        self.address = address
        self.phone = phone
        self.email = email

    @abstractmethod
    def showContact(self):
        pass

class BCIContact(Contact):
    def __init__(self, address, phone,email):
        super().__init__(address, phone,email)

    def showContact(self):
        print("\nBCI Campus Address : ",self.address ,"\nContact : ",self.phone,"\nEmail   : ",self.email)