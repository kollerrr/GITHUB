

def initials(fio):
    
    initial = fio.split(' ')
    name = f'{(str(initial[1]))[0]}.'
    patronymic = f'{(str(initial[2]))[0]}.'
    
    res = ' '.join([initial[0], name, patronymic])

    return res

fio = str(input())
print(initials(fio))