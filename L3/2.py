
def total_sum(total, time):

    if time not in range(8,23):
        return 'error'
    else:
        if time in range(10,13):
            total //= 2
        elif time in range(20,23):
            total //= 4

        return total

total = int(input('сумма к оплате'))
time = int(input('время'))

print(total_sum(total, time))