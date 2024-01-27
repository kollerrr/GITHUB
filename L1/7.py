# бюджет 1572, сколько единиц товара можно купить

def count_check(cost):
    
    count = 1572 // cost
    return count

cost = int(input())

print(count_check(cost))