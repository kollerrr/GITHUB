# перевернуть число из прошлой задачи

def flip(number):
    
    n1 = number // 100
    n2 = (number // 10) % 10
    n3 = number % 10

    return f'{n3}{n2}{n1}'

number = int(input())
print(flip(number))  