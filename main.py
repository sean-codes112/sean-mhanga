def join_data() :
    import math
    x1 = float(input("Enter x1 : "))
    x2 = float(input("Enter x2 : "))
    y1 = float(input("Enter y1 : "))
    y2 = float(input("Enter y2 : "))
    dx = x2-x1
    dy = y2-y1
    dist = dx**2 + dy**2
    distance = math.sqrt(dist)
    an = math.atan(dy/dx)
    angle = math.degrees(an)
    if dx>0 and dy>0:
        print('DIRECTION : '+str(angle))
    elif dx<0 and dy>0:
        print('DIRECTION : '+str(180 - angle))
    elif dx<0 and dy<0:
        print('DIRECTION : '+str(180 + angle))
    else:
        print('DIRECTION : '+str(angle+360))
    print('DISTANCE : '+str(distance))

join_data()