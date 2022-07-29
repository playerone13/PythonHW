from random import randint
my_list = [randint(10, 20000) for _ in range(10000)]
uniq_list = [el for el in my_list if my_list.count(el) == 1]
print(uniq_list)
