
def total_sum(time, item1_price, item2_price, item3_price):


    if time not in range(8,23):
        return 'error'
    else:
        total = item1_price + item2_price + item3_price

        if time in range(10,13):
            total //= 2
        elif time in range(20,23):
            total //= 4

        if item1_price < item2_price < item3_price:
            total //= 2
        elif item1_price > item2_price > item3_price:
            total //= 3

        return f'к оплате:{total}'

item1_price = int(input('стоимость товара1 '))
item2_price = int(input('стоимость товара2 '))
item3_price = int(input('стоимость товара3 '))

# total = int(input('сумма к оплате '))
time = int(input('время '))


print(total_sum(time, item1_price, item2_price, item3_price))
