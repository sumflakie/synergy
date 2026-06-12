# Задание №2

# Вводится натуральное число X. Подсчитайте количество натуральных делителей числа X (включая 1 и само число). x ≤ 2e9 (2 миллиарда)

number = int(input("Введите натуральное: "))

devidersCount = 0
i = 1

while i * i <= number:
    if number % i == 0:
        devidersCount += 1
        
        if i != number // i:
            devidersCount += 1
            
    i += 1
    
print(devidersCount)