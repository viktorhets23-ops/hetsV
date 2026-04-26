def product_of_negatives(filename):
    product = 1
    found = False
    try:
        with open(filename, 'r') as file:
            for line in file:
               
                numbers = map(int, line.split())
                for num in numbers:
                    if num < 0:
                        product *= num
                        found = True
        
        if found:
            print(f"Добуток від'ємних чисел: {product}")
        else:
            print("Від'ємних чисел у файлі не знайдено.")
    except FileNotFoundError:
        print("Файл не знайдено!") [cite: 871, 872]


product_of_negatives("numbers.txt")