text = input("Введіть текстовий рядок: ")


words = text.split()

print("Слова з вилученою останньою літерою:")
for word in words:

    if len(word) > 0:
        print(word[:-1], end=' ')
print()