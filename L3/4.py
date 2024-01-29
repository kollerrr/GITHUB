
category = str(input('категория товара '))

if category == 'продукты':
    price = int(input('введите цену '))

    if price < 100:
        print("Попробуйте нашу выпечку!")
    elif 100 < price <= 500:
        print("Как насчёт орехов в шоколаде?")
    elif price >= 500:
        print("Попробуйте экзотические фрукты!")
else:
    print('загляните в товары для дома')