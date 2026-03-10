
text = input("Введіть текстовий рядок: ")

last_comma_index = text.rfind(',')

if last_comma_index != -1:
    print(f"Позиція останньої коми: {last_comma_index}")
else:
    print("У введеному рядку немає ком.")