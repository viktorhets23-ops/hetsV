A = int(input("Введіть число A: "))
B = int(input("Введіть число B: "))


is_A_odd = A % 2 != 0
is_B_odd = B % 2 != 0
is_diff_negative = (A - B) < 0

result = is_A_odd and is_B_odd and is_diff_negative

print(f"Твердження є {result}")