# width of surface
# height
# consumption
# value
# percent

def surface(width, height, consumption, value, percent):

    square = width * height
    count_litres = width * height * consumption * (1 + percent / 100)
    count_of_jars = (count_litres // value) + 1
    count_of_useless = (round(float(count_of_jars * value - count_litres),2))

    return square, count_litres, count_of_jars, count_of_useless


width = float(input())
height = float(input())
consumption = float(input())
value = int(input())
percent = int(input())

print(surface(width, height, consumption, value, percent))