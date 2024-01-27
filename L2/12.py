
def price_wout_tags(price):

    price = price.replace('&nbsp;', '').replace('span', '').replace('/', '').replace('>', '').replace('p', '').replace('<', '')
    price_plus_1 = int(price) + 1
    
    return str(price_plus_1)


price = str(input())
print(price_wout_tags(price))
