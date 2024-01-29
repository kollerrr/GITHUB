total = int(input('стоимость покупок '))

while total != 0:
    if total % 2 == 0:
        while total % 2 == 0:
            total /= 2
    else:
        total -= 0.15*total

print(f'к оплате: {total}')