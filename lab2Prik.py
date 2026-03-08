
import math

def calculate_y(x):

    numerator = math.exp(-x) - 4 * x - (math.log(x))**3
    
    denominator = math.log10(abs(x + 1)) + (1 / math.tan(x**2 - 1))
    
    return numerator / denominator

try:
    x = 4
    result = calculate_y(x)
    print(f"При x = {x}, y = {result}")
except ValueError:
    print("Помилка: x має бути > 0 для логарифма")
except ZeroDivisionError:
    print("Помилка: ділення на нуль")