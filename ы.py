import random

class Cipher:
    def __init__(self, number):
        self.__number = number

    def __encapsulate(self):
        operation = random.choice(['+', '-', '*', '/'])
        operand = random.randint(1, 10)

        if operation == '+':
            self.__number += operand
        elif operation == '-':
            self.__number -= operand
        elif operation == '*':
            self.__number *= operand
        elif operation == '/':
            if operand != 0:
                self.__number /= operand
            else:
                print("Ошибка деления на ноль! Пропуск операции деления.")

    def __str__(self):
        self.__encapsulate()
        return f"Result: {self.__number}"


number = int(input("Enter a number: "))
cipher = Cipher(number)
print(cipher)
