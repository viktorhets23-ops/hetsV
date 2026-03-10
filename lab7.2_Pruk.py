import random

# Отримуємо дані від користувача для визначення розмірності
name = input("Введіть ваше ім'я: ")
surname = input("Введіть ваше прізвище: ")

n = len(name) # кількість стовпців
m = len(surname) # кількість рядків

print(f"\nКількість літер в імені (n) = {n}")
print(f"Кількість літер в прізвищі (m) = {m}\n")

# а) дійсні числа від 0 до 1
matrix_a = [[random.random() for _ in range(n)] for _ in range(m)]

# б) цілі числа від -10 до 10 включно
matrix_b = [[random.randint(-10, 10) for _ in range(n)] for _ in range(m)]

# в) цілі додатні числа від 0 до 20 включно
matrix_c = [[random.randint(0, 20) for _ in range(n)] for _ in range(m)]

# г) дійсні числа від -10 до 10
matrix_d = [[random.uniform(-10, 10) for _ in range(n)] for _ in range(m)]

# Виведення матриці (б) для наочності
print("Згенерована матриця (б) [цілі числа від -10 до 10]:")
for row in matrix_b:
    # Вирівнюємо вивід елементів матриці
    print(" ".join(f"{x:4}" for x in row))

print("\n" + "-"*40 + "\n")

# 5. Генерація магічного квадрата (n = m)
print("5. Генерація магічного квадрата")

# Сіамський метод генерування магічного квадрата працює для непарних розмірів.
size = n
if size % 2 == 0:
    print(f"Оскільки довжина імені (n={size}) є парною, для Сіамського методу розмір буде збільшено до {size + 1}.")
    size += 1

# Створюємо порожню квадратну матрицю, заповнену нулями
magic_square = [[0] * size for _ in range(size)]

# Початкова позиція: верхній рядок, середній стовпець
i, j = 0, size // 2

for num in range(1, size * size + 1):
    magic_square[i][j] = num
    
    # Рухаємось по діагоналі вгору і вправо
    next_i, next_j = (i - 1) % size, (j + 1) % size
    
    # Якщо наступна клітинка вже зайнята, просто спускаємось на рядок нижче
    if magic_square[next_i][next_j] != 0:
        i = (i + 1) % size
    else:
        i, j = next_i, next_j

print(f"\nМагічний квадрат розміром {size}x{size}:")
for row in magic_square:
    print(" ".join(f"{x:4}" for x in row))

# Для перевірки 
magic_constant = sum(magic_square[0])
print(f"\nМагічна константа (сума кожного рядка, стовпця та діагоналі) = {magic_constant}")