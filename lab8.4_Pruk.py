text = input("Введіть текстовий рядок: ")
words = text.split()


f_groups = {}

for word in words:
    clean_word = word.strip(".,!?()[]{}\"'")
  
    count_f = clean_word.lower().count('f')
    

    if count_f not in f_groups:
        f_groups[count_f] = []
    f_groups[count_f].append(clean_word)

print("Слова, згруповані за кількістю літер 'F':")
for count, group_words in f_groups.items():
  
    if count > 0: 
        print(f"Слова з кількістю 'F' = {count}: {', '.join(group_words)}")