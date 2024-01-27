# перевод пикселей в негатив

def negative_pic(positive_pixel):

    if positive_pixel not in(range(0,255)):
        return "error"
        
    color = 255 - positive_pixel
    return(color)

positive_pixel = int(input())
print(negative_pic(positive_pixel))