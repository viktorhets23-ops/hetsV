import random_utils  

def main():
    try:
        # Отримуємо кількість елементів від користувача
        count = int(input("Введіть кількість випадкових чисел: "))
        
        if count < 0:
            print("Кількість не може бути від'ємною.")
            return

        # Викликаємо функцію з модуля, використовуючи префікс (ім'я модуля та крапка) 
        random_numbers = random_utils.generate_random_list(count)
        
        print(f"Згенерований список: {random_numbers}")

    except ValueError:
        print("Помилка: введіть ціле число.")

if __name__ == "__main__":
    main()