def tagging(number):

    return f'<a href="tel:{number}">{number}</a>'

number = str(input())
print(tagging(number))