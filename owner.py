from datetime import datetime

from model_object import ModelObject


class Owner(ModelObject):
    def __init__(self, id=0, firstName="", lastName="", birthday=datetime(1960,1,1), address="", phone=""):
        super().__init__(id)
        self._firstName: str = firstName
        self._lastName: str = lastName
        self._birthday: datetime = birthday
        self._address: str = address
        self._phone: str = phone


    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self,firstName:str):
        self._firstName = firstName

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self,lastName:str):
        self._lastName = lastName

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self,birthday: datetime):
        self._birthday =birthday

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self,address:str):
        self._address = address

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone:str):
        self._phone = phone






