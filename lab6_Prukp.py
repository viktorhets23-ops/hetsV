import random
print("--- Завдання 1 ---")
my_list = [10, 20, 30, 40, 50, 60]
my_list.insert(1, -5)
min_val = min(my_list)
max_val = max(my_list)
my_list.insert(2, [1, 2, 3])
my_list.append("Гец Віктор")
list_length = len(my_list)
print("Список:", my_list)
print(f"Мінімальний елемент: {min_val}, Максимальний: {max_val}")
print(f"Кількість елементів: {list_length}\n")



print("--- Завдання 2 ---")
C = ["Ноутбук", "Мишка", "Клавіатура", "Монітор"]
A = [15, 50, 30, 10]                              
B = [25000, 800, 1500, 7000]                      
total_value = sum(qty * price for qty, price in zip(A, B))
average_price = sum(B) / len(B)
max_qty_index = A.index(max(A))
most_abundant_product = C[max_qty_index]
print(f"Загальна вартість товарів: {total_value} грн")
print(f"Середня ціна: {average_price} грн")
print(f"Найбільше на складі: {most_abundant_product} ({max(A)} шт.)\n")


print("--- Завдання 3 ---")
random_list = [random.randint(-50, 50) for _ in range(25)]
A1 = [x for x in random_list if x > 0]
A2 = [x for x in random_list if x < 0]
print("Початковий список:", random_list)
print("Додатні (А1):", A1)
print("Від'ємні (А2):", A2, "\n")


print("--- Завдання 4 ---")
users = ["Mark", "Tom", "Bob", "Alice", "Tom", "Bill", "Tom", "Alex", "Shaun", "Mark"]
print(f"Tom зустрічається: {users.count('Tom')} разів")
print(f"Mark зустрічається: {users.count('Mark')} разів")
print(f"Alice зустрічається: {users.count('Alice')} разів")
print(f"John зустрічається: {users.count('John')} разів")
users.pop(2)
if "Tom" in users:
    users.remove("Tom")
print("Оновлений список:", users, "\n")


print("--- Завдання 5 ---")
text_info = "івапа віапв. іаві павіавп і."
count_a = text_info.lower().count('а')
print(f"Кількість символів 'а': {count_a}")
formatted_text = text_info.replace(". ", ".\n")
print("Текст по реченнях:\n" + formatted_text, "\n")


print("--- Завдання 6 ---")
my_str = "Віктор КН-3 Компютерні науки"
parts = my_str.split(" ")
print("Група:", parts[1])
my_str = my_str.replace("Віктор", "Гец")
print("Змінений рядок:", my_str)
words = my_str.split(" ")
print(f"Кількість слів у рядку: {len(words)}\n")


print("--- Завдання 7 ---")
my_list_words = ["Python", "це", "дуже", "патужна", "мова"]

joined_list = " 🚀 ".join(my_list_words)
print("Зі списку:", joined_list)
simple_string = "Рядок"
joined_string = "-".join(simple_string)
print("З простого рядка:", joined_string, "\n")


print("--- Завдання 8 ---")
for i in range(1, 11):
    if i % 2 == 0:
        print(f"Число {i} (парне) -> квадрат = {i**2}")
    else:
        print(f"Число {i} (непарне) -> куб = {i**3}")