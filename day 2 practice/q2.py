#import  math untuk euclid distance
import math

#tanya coordinates
xA, yA = input('Enter the coordinates of point A: ').split()
xB, yB = input('Enter the coordinates of point B: ').split()

#ganti jawaban menjadi integer untuk hitungan
xA = int(xA)
xB = int(xB)
yA = int(yA)
yB = int(yB)

#hitung slope dan euclid distance
slope = (yB - yA) / (xB - xA)
euclid = round(math.dist([xA, yA], [xB, yB]), 3)

#kasih hasil
print(
    f"""
slope: {slope}
distance: {euclid}
"""
)