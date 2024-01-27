# bmi

def bmi(weight, height):
    
    i = weight / (height * height)
    return i

weight = int(input())
height = float(input())

print(round(bmi(weight, height), 2))