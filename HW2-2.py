list = input("Введите числа c пробелами - ").split()
for i in range(1, len(list), 2):
    list.insert(i -1, list.pop(i))
print(list)