# поиск почты в тексте с использованием модуля re (регулярные выражения)

import re

def find_email(text):
    return re.findall('\S+@\S+', text)

text = str(input())
print(find_email(text))