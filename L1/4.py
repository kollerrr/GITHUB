# найти сумму, мин и макс из входных чисел

def oper(num1, num2, num3):

    nums = [num1, num2, num3]

    summa = sum(nums)
    maximum = max(nums)
    minimum = min(nums)

    return(summa, maximum, minimum)

num1 = int(input())
num2 = int(input())
num3 = int(input())


print(oper(num1, num2, num3))