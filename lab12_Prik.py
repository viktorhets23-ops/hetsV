
def calculate_recursive(n):

    if n == 1:
        return 1 / (1 + 0.5)
    return 1 / (n + calculate_recursive(n - 1))

def calculate_iterative(n):
   
    result = 1 + 0.5
    for i in range(1, n + 1):
        result = i + (1 / result if i > 1 else 0)
        # Для коректного ланцюгового дробу йдемо знизу вгору
    
    # Прямий розрахунок ітераційно знизу вгору:
    res = 1 + 0.5
    for i in range(1, n):
        res = (i + 1) + 1 / res
    return 1 / res


calculate_lambda = lambda n: 1/(1+0.5) if n == 1 else 1/(n + calculate_lambda(n-1))

def main():
    try:
        print("Програма для обчислення рекурсивної залежності (Варіант 15)")
        n = int(input("Введіть натуральне число n: "))
        
        if n < 1:
            raise ValueError("Число n повинно бути натуральним (n >= 1).")

        print(f"\nРезультати для n = {n}:")
        print(f"1. Рекурсивний метод: {calculate_recursive(n):.10f}")
        print(f"2. Ітераційний метод (цикл): {calculate_iterative(n):.10f}")
        
        try:
            print(f"3. Lambda-вираз: {calculate_lambda(n):.10f}")
        except RecursionError:
            print("3. Lambda-вираз: Перевищено глибину рекурсії.")

    except ValueError as e:
        print(f"Помилка введення: {e}")
    except Exception as e:
        print(f"Виникла непередбачена помилка: {e}")

if __name__ == "__main__":
    main()