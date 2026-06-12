# Задание №1

# Сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте, сколько из них равны нулю, и выведите это количество.

numbersCount = int(input("Введите количество проверяемых чисел: "))

zeroCount = 0

for i in range(numbersCount):
  tempNumber = int(input("Введите целое число: "))
  if tempNumber == 0 :
      zeroCount += 1
      
print(zeroCount)