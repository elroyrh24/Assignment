import math

xA, yA = input('Enter the coordinates of point A: ').split(', ', 2)
xB, yB = input('Enter the coordinates of point B: ').split(',', 2)

slope = (int(yB) - int(yA)) / (int(xB) - int(xA))
euclid = math.dist([int(xA), int(yA)], [int(xB), int(yB)])

print(
    f"""
slope: {slope}
distance: {euclid}
"""
)