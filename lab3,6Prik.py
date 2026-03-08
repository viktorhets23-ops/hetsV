a = float(input("Сторона a: "))
b = float(input("Сторона b: "))
c = float(input("Сторона c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Рівносторонній")
    elif a == b or a == c or b == c:
        print("Рівнобедрений")
    else:
        print("Різносторонній")
else:
    print("Трикутник не існує")