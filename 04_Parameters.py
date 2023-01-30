# Calculates the area of a triangle give its side lengths.

def area_tri(b, h):
    """Calculates the area of a triangle with base of b and height of h"""
    area = 0.5 * b * h
    print("The area of the triangle is " + str(area) + "cm^2")


area_tri(4, 5)
area_tri(3.5, 7.8)