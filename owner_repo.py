from owner import Owner
from repository import Repository


class Owner_repo(Repository):
    def __init__(self):
        super().__init__()

    def add(self, param: Owner)-> int:
        return super()._add(param, "insert owner(firstName,lastName,birthday,address,phone) value (%s,%s,%s,%s,%s)")

    def remove(self, id: int):
        super(Owner_repo, self)._remove(id,"owner")

    def find(self, predicate):
        result: list[Owner] = []
        temp = self.getall()
        for i in temp:
            if predicate(i):
                result.append(i)
        return result

    def findbyid(self, id: int) -> Owner:
        result = super(Owner_repo, self)._findbyid(id,"owner")
        if result is None:
            return
        return Owner(*result)

    def getall(self) -> list[Owner]:
        owner = super(Owner_repo, self)._getall("owner")
        return [Owner(*x) for x in owner]
