# Задание №1

# Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:

# top_up(X) - пополнить на X
# count_1000() - выводит сколько целых тысяч осталось в кассе
# take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег

class CashRegister:
    def __init__(self, money = 0):
        self.money = money
        
    def top_up(self, amount):
        self.money += amount
        
    def count_1000(self):
        return self.money // 1000
    
    def take_away(self, amount):
        if amount > self.money:
            print("Недостаточно денег в кассе")
        else:
            self.money -= amount
            
cashbox = CashRegister()

command = ""

print("Доступные команды:")
print("top_up - пополнить кассу")
print("take_away - снять деньги")
print("count_1000 - показать количество полных тысяч")
print("balance - показать остаток")
print("stop - выход")

while command != "stop":
    command = input("Введите команду: ")

    if command == "top_up":
        amount = int(input("Введите сумму: "))
        cashbox.top_up(amount)

    elif command == "count_1000":
        print(f"Целых тысяч: {cashbox.count_1000()}")

    elif command == "take_away":
        amount = int(input("Введите сумму: "))
        cashbox.take_away(amount)

    elif command == "balance":
        print(f"В кассе: {cashbox.money}")

    elif command != "stop":
        print("Неизвестная команда")