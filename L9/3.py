"""
Напишите программу, которая будет складывать числа, введенные пользователем.
Сигналом к окончанию ввода должна служить пустая строка.
Отобразите на экране сумму значений (или 0.0, если пользователь сразу же пропустил ввод). 
Решите эту задачу с использованием рекурсии. В вашей программе не должны присутствовать циклы.
Подсказка. В теле вашей рекурсивной функции должен производиться запрос одного числа у пользователя, 
после чего должно быть принято решение о том, производить ли еще один рекурсивный вызов. 
Ваша функция не должна принимать аргументов, а возвращать будет числовое значение
"""
def count_num(a):

    a = int(input())
    if a == -1:
        return s
    else:
        s += a
        return f(s)

print(count_num(2))