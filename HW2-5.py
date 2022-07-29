list = [1, 3, 5, 5, 6, 7, 3, 9, 1]
new_number = int(input('введите новый номер рейтинг - '))
i = 0
for n in list:
    if new_number <= n:
        i +=1

    elif new_number > n:
        break
list.insert(i, float(new_number))
print(list)