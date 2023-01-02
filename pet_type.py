from model_object import ModelObject


class PetType(ModelObject):
    def __init__(self, id=0, typeName=""):
        super().__init__(id)
        self._typeName: str = typeName

    @property
    def typeName(self):
        return self._typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self._typeName = typeName















