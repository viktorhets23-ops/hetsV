def filter_by_start_char(filename, char):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith(char):
                    print(line.strip())
    except FileNotFoundError:
        print("Файл не знайдено!") [cite: 871, 872]

# Приклад використання
char_to_find = input("Введіть початковий символ: ")
filter_by_start_char("input.txt", char_to_find)