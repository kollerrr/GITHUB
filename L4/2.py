
sw = input('введите программу ')

if sw == 'game':
    print('угадай число')
    for i in range(3):
        a = (input('введите число '))
        if a == 'end':
             break
        if a == 5:
            print('вы выиграли билет на концерт')
        else: 
            print (f'осталось попыток: {[2-i]}')