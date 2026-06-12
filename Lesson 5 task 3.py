minSum = float(input("Введите минимальную сумму инвестиций: "))
mike = float(input("Введите количество долларов у Майкла: "))
ivan = float(input("Введите количество долларов у Ивана: "))

if mike >= minSum and ivan >= minSum :
    print("2")
elif mike >= minSum and ivan < minSum :
    print("Mike")
elif mike < minSum and ivan >= minSum :
    print("Ivan")
elif mike + ivan >= minSum :
    print("1")
else :
    print("0")