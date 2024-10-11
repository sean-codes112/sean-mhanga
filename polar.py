def polar_data() :
    import math
    y = float(input("Enter Y1 coordinate : "))
    x = float(input("Enter x1 coordinate : "))
    dist = float(input("Enter distance : "))
    dirn = float(input("Enter direction : "))
    direction = math.degrees(dirn)
    yy = math.sin(direction)
    xx = math.cos(direction)
    y2 = dist+yy
    x2 = dist+xx
    print('y2 : ' + str(y2))
    print('x2 : ' + str(x2))
polar_data()