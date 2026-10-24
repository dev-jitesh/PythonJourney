x = float(input("x coordinate = "))
y = float(input("y coordinate = "))

if x == 0 and y == 0:
    print("Origin")
elif x == 0:
    print("point on Y axis")
elif y == 0:
    print("point on x axis")
elif x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
else:
    print("Quadrant IV")