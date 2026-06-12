# Задание №2

# Создайте класс Черепашка, который хранит позиции x и y черепашки, а также s - количество клеточек, на которое она перемещается за ход

# у этого класс есть методы:

# go_up() - увеличивает y на s
# go_down() - уменьшает y на s
# go_left() - уменьшает x на s
# go_right() - увеличивает y на s
# evolve() - увеличивает s на 1
# degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
# count_moves(x2, y2) - возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции

import math

class Turtle:
    def __init__(self, x = 0, y = 0, s = 1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s - 1 <= 0:
            print("Скорость не может быть меньше или равна 0")
        else:
            self.s -= 1

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x) 
        dy = abs(y2 - self.y)

        return math.ceil(dx / self.s) + math.ceil(dy / self.s)

x = int(input("Введите начальную координату X: "))
y = int(input("Введите начальную координату Y: "))
s = int(input("Введите скорость: "))

turtle = Turtle(x, y, s)

print("Доступные команды:")
print("go_up")
print("go_down")
print("go_left")
print("go_right")
print("evolve - увеличивает скорость на 1")
print("degrade - уменьшает скорость на 1")
print("count_moves - количество ходов от текущей позиции до заданной")
print("position - текущая позиция черепашки")
print("stop")

command = ""

while command != "stop":
    command = input("Введите команду: ")

    if command == "go_up":
        turtle.go_up()

    elif command == "go_down":
        turtle.go_down()

    elif command == "go_left":
        turtle.go_left()

    elif command == "go_right":
        turtle.go_right()

    elif command == "evolve":
        turtle.evolve()
        print(f"Скорость: {turtle.s}")

    elif command == "degrade":
        turtle.degrade()
        print(f"Скорость: {turtle.s}")

    elif command == "count_moves":
        x2 = int(input("Введите X цели: "))
        y2 = int(input("Введите Y цели: "))

        print(f"Минимальное количество шагов: {turtle.count_moves(x2, y2)}")

    elif command == "position":
        print(f"Текущая позиция: ({turtle.x}, {turtle.y})")
        print(f"Скорость: {turtle.s}")

    elif command != "stop":
        print("Неизвестная команда")