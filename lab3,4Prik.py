bracket = input("Введіть символ-дужку: ")

if bracket == "(":
    print("Відкрита кругла дужка")
elif bracket == ")":
    print("Закрита кругла дужка")
elif bracket == "[":
    print("Відкрита квадратна дужка")
elif bracket == "]":
    print("Закрита квадратна дужка")
elif bracket == "{":
    print("Відкрита фігурна дужка")
elif bracket == "}":
    print("Закрита фігурна дужка")
else:
    print("Це не дужка")