class Menu:
    def __init__(self):
        self._menuItems = {}

    def AddMenuItem(self, itemText: str, value):
        self._menuItems[len(self._menuItems) + 1] = [itemText, value]

    def Show(self):
        for index, value in self._menuItems.items():
            print(f"{index}. {value[0]}")

    def GetAssosiatedValue(self, userChoise: int):
        if userChoise in self._menuItems.keys():
            return self._menuItems[userChoise][1]
        return None

    def GetUserInput(self, text: str):
        userInput = input(text)
        if userInput.isnumeric():
            result = int(userInput)
            if result > 0 and result <= len(self._menuItems):
                return result
        return None

    def GetValueFromInput(self, text: str):
        userChoise = self.GetUserInput(text)
        if userChoise == None:
            return None
        return self.GetAssosiatedValue(userChoise)

