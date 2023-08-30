import math

xA, yA = input('Enter the coordinates of point A: ').split(', ', 2)
xB, yB = input('Enter the coordinates of point B: ').split(',', 2)

xA = int(xA)
xB = int(xB)
yA = int(yA)
yB = int(yB)
slope = (yB - yA) / (xB - xA)
euclid = round(math.dist([xA, yA], [xB, yB]), 3)

print(
    f"""
slope: {slope}
distance: {euclid}
"""
)