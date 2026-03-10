text = input("Введіть речення: ")
words = text.split()

print("Слова, в яких немає літер, що повторюються:")
for word in words:
  
    clean_word = word.strip(".,!?()[]{}\"'").lower()
    
  
    if len(clean_word) > 0 and len(clean_word) == len(set(clean_word)):
        print(word)