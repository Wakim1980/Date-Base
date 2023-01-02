import mysql.connector

from model_object import ModelObject


class Repository:
    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost", user="root",password="root",database="pet_manager")
        self.cursor = self.mydb.cursor(buffered=True)

    def _add(self, param: ModelObject, qwery: str) -> int:
        t = tuple(x for x in param)[1:]
        self.cursor.execute(qwery, t)
        self.mydb.commit()
        return self.cursor.lastrowid

    def _remove(self, id: int, table: str):
        self.cursor.execute(f"delete from {table} where id = {id}")
        self.mydb.commit()

    def _findbyid(self, id: int, table: str):
        self.cursor.execute(f"select * from {table} where id = {id}")
        return self.cursor.fetchone()

    def _getall(self,table: str):
        self.cursor.execute(f"select * from {table}")
        return self.cursor.fetchall()

    def _find(self, predicate,table):
        result = []
        temp = self._getall(table)
        for i in temp:
            if predicate(i):
                result.append(i)
        return result


