
def number_simplifier(number_w_symbols):

    # number_w_symbols = number_w_symbols.replace('-', '').replace(')', '').replace('(', '').replace(' ', '')


    if number_w_symbols.find('-'):
        number_w_symbols = number_w_symbols.replace('-', '')
    if number_w_symbols.find(')'):
        number_w_symbols = number_w_symbols.replace(')', '')
    if number_w_symbols.find('('):
         number_w_symbols = number_w_symbols.replace('(', '')
    if number_w_symbols.find(' '):
        number_w_symbols = number_w_symbols.replace(' ', '')
    
    return number_w_symbols


number_w_symbols = str(input())
print(number_simplifier(number_w_symbols))

