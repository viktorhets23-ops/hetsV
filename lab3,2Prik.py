a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))

if a == b == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
else:
    print(0)