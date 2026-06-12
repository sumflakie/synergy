# Задание №1

# Есть родительский класс:

 

# class Transport:

#    def __init__(self, name, max_speed, mileage):

# self.name = name
# self.max_speed = max_speed
# self.mileage = mileage
 
# Создайте объект Autobus, который унаследует все переменные и методы родительского класса Transport и выведете его.
# Ожидаемый результат вывода:

# Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Autobus(Transport):
    pass

name = input("Введите название автомобиля: ")
max_speed = int(input("Введите максимальную скорость: "))
mileage = int(input("Введите пробег: "))

bus = Autobus(name, max_speed, mileage)

print(f"Название автомобиля: {bus.name}. Скорость: {bus.max_speed}. Пробег: {bus.mileage}.")