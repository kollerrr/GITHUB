# сумма цифр трехзнач числа (без использования циклов)

def digit_sum(number):
    
    n1 = number // 100
    n2 = (number // 10) % 10
    n3 = number % 10

    return(sum([n1,n2,n3]))

number = int(input())
print(digit_sum(number))