from model_object import ModelObject


class Pet(ModelObject):
    def __init__(self, id=0, name="", ownerId=0, petType=0):
        super().__init__(id)
        self._name: str = name
        self._ownerId: int = ownerId
        self._petType: int = petType

    @property
    def saveQuery(self):
        return "insert into pets (name,ownerId,petType) values(%s,%s,%s)"


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name:str):
        self._name = name

    @property
    def ownerid(self):
        return self._ownerId

    @ownerid.setter
    def ownerid(self, ownerId: int):
        self._ownerId = ownerId

    @property
    def petType(self):
        return self._petType

    @petType.setter
    def petType(self, petType:str):
        self._petType =petType










