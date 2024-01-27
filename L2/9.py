
def hyphen_to_dash_replacer(text):

    if text.find('--'):
        return text.replace('--', '—')


text = str(input())
print(hyphen_to_dash_replacer(text))

