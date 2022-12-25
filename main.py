from kontroller import Controller
from menu import Menu
import os
clear = lambda: os.system("cls")
kontroller = Controller()


menu = Menu()
menu.AddMenuItem("Добавить домашнее животное",kontroller.add_pet)
menu.AddMenuItem("Добавить хозяина",kontroller.add_owner)
menu.AddMenuItem("Показать всех петов владельца",kontroller.show_all_owner_pet)
menu.AddMenuItem("Найти всех животных по виду ",kontroller.show_pet_by_type)
menu.AddMenuItem("Тест",kontroller.test)
menu.AddMenuItem("Выйти из программы",exit)

while True:
    menu.Show()
    menu.GetValueFromInput("->")()
    input("Нажмите Enter для продолжения ")
    clear()
# конец файла










