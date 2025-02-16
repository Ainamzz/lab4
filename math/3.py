#area of regular polygon
import math
n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
area = int(((n * pow(l, 2))/4) * math.cos(math.pi / n) / math.sin(math.pi / n))
print("the area of the polygon is: ", area)