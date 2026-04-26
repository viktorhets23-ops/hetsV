class ArithmeticOperation:
    
    
    def __init__(self, operand1, operand2):
       
        self.a = operand1
        self.b = operand2

    def get_sum(self):
      
        return self.a + self.b

    def get_product(self):
       
        return self.a * self.b

# Перевірка завдання 1
op = ArithmeticOperation(10, 5)
print(f"Операнди: 10 та 5")
print(f"Сума: {op.get_sum()}")
print(f"Добуток: {op.get_product()}")