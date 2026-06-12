word = input("Введите слово из строчных латинских букв: ")

a_count = word.count("a")
e_count = word.count("e")
i_count = word.count("i")
o_count = word.count("o")
u_count = word.count("u")

vowCount = a_count + e_count + i_count + o_count + u_count
conCount = len(word) - vowCount

print(f'Количество букв a: {a_count or False}.')
print(f'Количество букв e: {e_count or False}.')
print(f'Количество букв i: {i_count or False}.')
print(f'Количество букв o: {o_count or False}.')
print(f'Количество букв u: {u_count or False}.')
print(f'Количество гласных букв: {vowCount}.')
print(f'Количество согласных букв: {conCount}.')