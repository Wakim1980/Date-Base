class ModelObject:
    def __init__(self, id: int):
        self._id = id


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self,velue:int):
        self._id =velue


    def __iter__(self):
        return ModelObjectIter(self)

    def __eq__(self, other):
        return tuple(self.__dict__.values()) == tuple(other.__dict__.values())

    def __str__(self):
        return f"{tuple(self)}"[1:-1]


class ModelObjectIter:
    def __init__(self, modelObject):
        self._modelObject = modelObject
        self._current = 0
        self._fields = tuple(modelObject.__dict__.keys())

    def __iter__(self):
        return self

    def __next__(self):
        if self._current >= len(self._fields):
            raise StopIteration
        element = self._modelObject.__dict__[self._fields[self._current]]
        self._current += 1
        return element






