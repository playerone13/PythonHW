def my_func(x, y):
    global my_func1
    abs(y)
    my_func1 = x ** y
    return my_func1
print(my_func(2, -3))
