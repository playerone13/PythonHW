def sum_num():
    a = 0
    while True:
        in_list = input('введите чила или нажмите q для выхода -').split()
        for num in in_list:
            if num == 'q':
                return a
            else:
                try:
                    a += int(num)
                except ValueError:
                    print('чтобы выйти нажмите q -')

        print(f'сумма чисел = {a}')
print(sum_num())




