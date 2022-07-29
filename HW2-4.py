words = str(input("введите слова через пробел - ")).split()
for i, words in enumerate(words, 1):
    print(f'{i}) {words[:10]}')