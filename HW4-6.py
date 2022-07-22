from itertools import count, cycle

print('Программа генерирует целые числа начиная с указанного. Для генерации следующего числа необходимо нажать Enter', 'Для выходна нажмите Q')
for i in count(int(input('Введите стартовое число'))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

print('Программа повторяет элементы спискаю Для генерации следующего повторения необходимо нажать Enter', 'Для выхода из программы нажмите Q')
u_list = input('Ведите список, разделяя элементы пробелом: ').split()
iter_ = cycle(u_list)
quit= None

while quit != 'q':
    print(next(iter_), end='')
    quit = input()
