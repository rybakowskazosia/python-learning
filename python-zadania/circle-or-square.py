import math

radius = float(input("Specify the radius of the circle: "))
square_area = float(input("Specify the suare's area: "))

#obliczenia obwodów:

circle_circumference = 2 * math.pi * radius #obl obwodu koła
square_side_length = math.sqrt(square_area) #obl długości boku kwadratu
square_circumference = 4 * square_side_length #obl obwodu kwadratu


if circle_circumference > square_circumference:
    print("Circle circumference is greater than square circumference.", True)
else:
    print("Square circumference is greater than circle circumference.", False)

    