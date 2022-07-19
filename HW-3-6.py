def int_func(word):
    latin_char = 'fergrehrthrghrthgjh'
    return word.title() if not set(word).difference(latin_char) else False

words = input('Введите слова разделенные пробелами -').split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w), ' ')