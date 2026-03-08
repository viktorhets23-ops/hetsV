N = int(input("Введіть кількість рядків N (2 <= N < 30): "))
M = int(input("Введіть параметр M (2 <= M < 30): "))

if 2 <= N < 30 and 2 <= M < 30:
    for i in range(1, N + 1):
        row = []

        for j in range(M + 1):
            row.append(str(i * 10 + j))
        print(" ".join(row))
else:
    print("Помилка: N та M повинні бути в діапазоні [2, 30).")