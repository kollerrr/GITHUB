
def increase_check(lst):

    if len(lst) < 2:
        return '-'

    for i in range(len(lst)-1):
        if lst[i] + 1 != lst[i+1]:
            return '-'
    return '+'

lst = input()
print(increase_check(lst))