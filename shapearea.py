import math

def sphere(r):
    area = math.pi*(r**2)*(4/3)
    return area

print(sphere(4))

def cylinder(r,h):
    area = math.pi*(r**2)*h
    return area

print (cylinder(4,4))


def cone (r,h):
    area = (1/3) * math.pi * (r**2) * h
    return area


print(cone(2,4))


      
