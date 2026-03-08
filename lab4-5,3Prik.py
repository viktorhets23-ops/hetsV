import math

epsilon = float(input("Введіть необхідну точність ε (наприклад, 0.001): "))

n = 1
prev_pi = 0
current_pi = 0

while True:
    factorial_n = math.factorial(n)
    n_over_e_pow_n = (n / math.e) ** n

    current_pi = ((factorial_n / n_over_e_pow_n) ** 2) / (2 * n)

    if n > 1 and abs(current_pi - prev_pi) < epsilon:
        break
        
    prev_pi = current_pi
    n += 1

print(f"\nНеобхідна кількість членів ряду (n): {n}")
print(f"Обчислене значення π: {current_pi:.6f}")
print(f"Еталонне значення π: {math.pi:.6f}")