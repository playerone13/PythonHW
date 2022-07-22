num_1 = float(input("введите первое число - "))
num_2 = float(input("Введите второе число -"))
if num_2 == 0:
    print("Деление на ноль запрещено!")
else:
    def int_func():
        return float(num_1 / num_2)
    print(int_func)
