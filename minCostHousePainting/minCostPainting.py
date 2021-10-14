def colourHouse(n, red, green, blue, latest_colour = None, count = 0):
    if count == n:
        return 0
    
    if latest_colour == None:
        return min(
            red[count] + colourHouse(n, red, green, blue, 'r', count+1),
            green[count] + colourHouse(n, red ,green, blue, 'g', count+1),
            blue[count] + colourHouse(n, red, green, blue, 'b', count+1)
        )
    elif latest_colour == 'r':
        return min(
            green[count] + colourHouse(n, red, green, blue, 'g', count+1),
            blue[count] + colourHouse(n, red, green, blue,'b', count+1)
        )
    elif latest_colour == 'g':
        return min(
            red[count] + colourHouse(n, red, green, blue, 'r', count+1),
            blue[count] + colourHouse(n, red, green, blue,'b', count+1)
        )
    else:
        return min(
            red[count] + colourHouse(n, red, blue, green, 'r', count+1),
            green[count] + colourHouse(n, red, blue, green, 'g', count+1)
        )

if __name__ == '__main__':
    n = 3
    red = [6,5,3]
    green = [3,1,6]
    blue = [9,4,2]
    print(colourHouse(n,red,green,blue))
