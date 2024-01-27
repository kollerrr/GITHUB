
def reduction(text):

    if text.find('ический'):
        return text.replace('ический', '.')
    elif text.find('ическая'):
        return text.replace('ическая', '.')


text = str(input())
print(reduction(text))

