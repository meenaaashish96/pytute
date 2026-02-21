#calculate cercumference of a circle
#Also area of circle
import math
def circle_stats(radius):
    circumference = round(2*math.pi*radius,2)
    area = round(math.pi*(radius**2),2)
    return {'circumference': circumference, 'area': area}

print(circle_stats(6371))