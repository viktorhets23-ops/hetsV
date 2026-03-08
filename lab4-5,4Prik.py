a = float(input("Введіть початок відрізка (і параметр) a: "))
b = float(input("Введіть кінець відрізка b: "))
h = float(input("Введіть крок h: "))
z = float(input("Введіть граничне значення z для зупинки: "))

x = a
count_greater_than_z = 0

print(f"\n{'x':<10} | {'y = f(x)':<10}")
print("-" * 25)


while x <= b + 1e-9:
    y = a / (x**2 + 1) + x / (a**2 + 1)
    
    print(f"{x:<10.4f} | {y:<10.4f}")

    if y > z:
        count_greater_than_z += 1
        if count_greater_than_z == 3:
            print(f"\n--> Табулювання припинено: знайдено три значення y > {z}")
            break
            
    x += h