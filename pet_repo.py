
from pet import Pet
from repository import Repository


class Pet_repo(Repository):
    def __init__(self):
        super().__init__()

    def add(self, param: Pet)-> int:
        return super()._add(param, "insert pets(name,ownerId,petType) values(%s,%s,%s)")

    def remove(self, id: int):
        super()._remove(id, "pets")

    def find(self, predicate):
        result = []
        temp = self.getall()
        for i in temp:
            if predicate(i):
                result.append(i)
        return result

    def findbyid(self, id: int) -> Pet:
        temp = super()._findbyid(id, "pets")
        if temp is None:
            return None
        return Pet(*temp)

    def getall(self) -> list[Pet]:
        temp = super()._getall("pets")
        return [Pet(*x) for x in temp]