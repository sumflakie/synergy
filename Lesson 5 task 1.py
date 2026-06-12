inputNumber = int(input("Введите целое число: "))

if inputNumber % 2 != 0 :
    print("Число не является четным")
elif inputNumber < 0 :
    print("Отрицательное четное число")
elif inputNumber == 0 :
    print("Нулевое число")
else:
    print("Положительное четное число")
    
    
