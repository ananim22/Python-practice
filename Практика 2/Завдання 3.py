def process_set(A, x):
    B = A.copy()
    if x in B:
        B.remove(x)
        print(f"\nСимвол '{x}' був наявний у множині, тому його видалено.")
    else:
        B.add(x)
        print(f"\nСимвол '{x}' був відсутній у множині, тому його додано.")
        
    return B

input_string = input("Введіть елементи множини A (через пробіл): ")
set_A = set(input_string.split())

symbol_x = input("Введіть символ 'x': ")
print(f"\nВаша початкова множина A: {set_A}")
set_B = process_set(set_A, symbol_x)
print(f"Сформована множина B: {set_B}")