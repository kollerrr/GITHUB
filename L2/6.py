
def op_code_extraction(phone_number):
    op_code = phone_number[2:5]

    return op_code

phone_number = str(input())
print(op_code_extraction(phone_number))