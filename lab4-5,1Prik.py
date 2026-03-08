N = int(input("Введіть кількість членів N: "))
b1 = float(input("Введіть перший член послідовності b1: "))
r = float(input("Введіть знаменник прогресії r (r != 1): "))

if r == 1:
    print("Помилка: r не може дорівнювати 1 за умовою.")
else:
    product = 1
    current_term = b1
    for _ in range(N):
        product *= current_term
        current_term *= r 
        
    print(f"Добуток перших {N} членів: {product}")