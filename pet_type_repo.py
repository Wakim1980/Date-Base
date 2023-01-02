import mysql.connector

from pet_type import PetType


class Pet_type_repo:
    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost", user="root", password="root",database = "pet_manager")
        self.cursor = self.mydb.cursor(buffered=True)

    def add(self,param: PetType)-> int:
        t = tuple(x for x in param)[1:]
        self.cursor.execute("insert pettype(typeName) values(%s)", t)
        self.mydb.commit()
        return self.cursor.lastrowid

    def remove(self,id :int):
        self.cursor.execute(f"delete from pettype where id = {id}")
        self.mydb.commit()

    def find(self,predicate) -> list[PetType]:
        result: list[PetType] = []
        temp = self.getall()
        for i in temp:
            if predicate(i):
                result.append(i)
        return result

    def findbyid(self,id: int) -> PetType:
        self.cursor.execute(f"select * from pettype where id = {id}")
        pettype = self.cursor.fetchone()
        return PetType(*pettype) if pettype is not None else None

    def getall(self)-> list[PetType]:
        self.cursor.execute(f"select * from pettype ")
        allpettype = self.cursor.fetchall()
        return [PetType(*x) for x in allpettype]


