import math

x1=float(input("point x1 :"))
y1=float(input("point x2 :"))
x2=float(input("point y1 :"))
y2=float(input("point y2 :"))

distance=math.sqrt((x2-x1)**2 +(y2-y1)**2)
print("Distance between of points = ",distance)