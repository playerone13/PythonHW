goods = []
feauters = {'название': '', 'цена': '', 'колличество': '', 'единица измерения': ''}
analytics = {'название': [], 'цена': [], 'колличество': [], 'единица измерения': []}
num = 0

while True:
    if input('Для выхода из приложения нажмите Q, для продолжения ENTER: ').upper() == 'Q':
        break
    num +=1
    for f in feauters.keys():
        prop = input(f'Введите значение свойства {f} - ')
        feauters[f] = int(prop) if f in ('цена', 'колличество') else prop
        analytics[f].append(feauters[f])
    goods.append((num, feauters.copy()))
    print(f"\nСтруктура товаров\n{goods}")
    print(f"\nТекущая аналитика по товарам\n{'*' * 30}")
    for key, value in analytics.items():
        print(f"{key[:25]:>30}: {value}")
    print('*' * 30)