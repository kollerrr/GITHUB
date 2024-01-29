
def sale_to_0(total,sale):

    while total != 0:
        total -= (sale / 100)*total
        if total == 0:
            print('0')
            break
    return total

total = float(input('сумма '))
sale = float(input('процент скидки в % '))

print(sale_to_0(total,sale))