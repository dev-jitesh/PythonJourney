a = float(input("Enter length of side A: "))
b = float(input("Enter length of side B: "))
c = float(input("Enter length of side C: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or c == a:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Error: Those sides cannot form a triangle.")