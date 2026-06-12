# Задание №3

# Во входную строку водится последовательность чисел через пробел. 
# Для каждого числа выведите слово ”YES” (в отдельной строке), если это число ранее встречалось в последовательности или ”NO”, если не встречалось.

numberArray = list(map(int, input("Введите числа через пробел: ").split()))

numbersSeen = set()

for number in numberArray:
    if number in numbersSeen:
        print("YES")
    else:
        print("NO")
        numbersSeen.add(number)