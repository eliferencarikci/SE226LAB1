import math
def circle_area(radius):
   if radius <= 0:
      raise ValueError("Radius must be >0")
   return math.pi * (radius**2)

def circle_perieter(radius):
   if radius <=0:
      raise ValueError("Radius must be >0")
   return 2*math.pi*radius

def rectangle_area(width,height):
   return width*height

def rectangle_perimeter(width,height):
   return 2(width+height)

def triangle_area(base,height):
   return (base*height)/2

