# расстояние между числами на числовой оси

def distance(num1, num2):
    
    dist = abs(num1 - num2)  # abs - функция модуля
    return(dist)

num1 = int(input())
num2 = int(input())

print(distance(num1, num2))