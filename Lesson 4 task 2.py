inputNumber = int(input("Введите целое пятизначное число: "))

ones = inputNumber % 10
tens = (inputNumber // 10) % 10
hundreds = (inputNumber // 100) % 10
thousands = (inputNumber // 1000) % 10
tenThousands = (inputNumber // 10000) % 10

result = ((tens ** ones) * hundreds) / (tenThousands - thousands)

print(f"Результат: {result}")