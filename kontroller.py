from datetime import datetime

import mysql.connector
from menu import Menu
from owner import Owner
from owner_repo import Owner_repo
from pet import Pet
from pet_repo import Pet_repo
from pet_type import PetType
from pet_type_repo import Pet_type_repo


class Controller:
    def __init__(self):
        self._pet_repo: Pet_repo = Pet_repo()
        self._pet_type_repo: Pet_type_repo = Pet_type_repo()
        self._owner_repo: Owner_repo = Owner_repo()

    def add_pet(self):
        pet_name = input("Введите имя пета ")
        owner:Owner = self.get_owner()
        if owner is None:
            return
        pyt_type: PetType = self.get_pet_type()
        if pyt_type is None:
            return
        pet = Pet(0,pet_name,owner.id, pyt_type.id)
        return self._pet_repo.add(pet)

    def add_owner(self, user_name = None):
        new_owner = Owner(0, input("Фамилия-> ") if user_name is None else user_name, input("Имя-> "), datetime(*[int(x) for x in (input("День Рождения-> ").split("."))]),input("Адрес-> "),input("Телефон-> "))
        new_owner.id = self._owner_repo.add(new_owner)
        return new_owner

    def show_all_owner_pet(self):
        owner = self.get_owner()
        result = self._pet_repo.find(lambda p: p.ownerid == owner.id)
        for i in result:
            print(self.get_pet_info(i))

    def show_pet_by_type(self):
        pet_type = self.get_pet_type()
        result = self._pet_repo.find(lambda p: p.petType == pet_type.id)
        for i in result:
            print(self.get_pet_info(i))

    def get_owner(self):
        user_name = input("Введите свою фамилию ")
        all_user = self._owner_repo.find(lambda p: p.lastName == user_name)
        if len(all_user) == 0:
            print("Такой хозяин не найден ")
            menu = Menu()
            menu.AddMenuItem("Добавить нового хозяина", False)
            menu.AddMenuItem("Завершить операцию", True)
            menu.Show()
            if menu.GetValueFromInput("->"):
                return None
            return self.add_owner(user_name)
        if len(all_user) > 1:
            menu_uzer = Menu()
            for i, value in enumerate(all_user):
                menu_uzer.AddMenuItem(f"{value.firstName} {value.lastName} {value.phone}", i)
            menu_uzer.Show()
            return Owner(*all_user[menu_uzer.GetValueFromInput("Выберите владельца ")])
        return Owner(*all_user[0])

    def get_pet_type(self):
        pet = input("Тип животного ")
        pet_type = self._pet_type_repo.find(lambda p: p.typeName == pet)
        if len(pet_type) == 0:
            print("Такой тип животного не найден ")
            menu = Menu()
            menu.AddMenuItem(f"Добавить новый тип животного {pet}?", False)
            menu.AddMenuItem("Завершить операцию", True)
            menu.Show()
            if menu.GetValueFromInput("->"):
                return None
            pet_type = PetType(0, pet)
            pet_type.id = self._pet_type_repo.add(pet_type)
        else:
            pet_type = pet_type[0]
        return pet_type

    def search_pet_type_by_id(self, id):
        return self._pet_type_repo.findbyid(id)

    def search_owner_by_id(self, id):
        return self._owner_repo.findbyid(id)

    def test(self):
        ptr = Owner_repo()
        temp = ptr.find(lambda p: p.address == "Kiev")
        for i in temp:
            print(i)

    def get_pet_info(self,pet: Pet):
        owner = self.search_owner_by_id(pet.ownerid)
        pet_type = self.search_pet_type_by_id(pet.petType)
        return f"Имя пета {pet.name} имя хозяина {owner.firstName} тип животного {pet_type.typeName}"

