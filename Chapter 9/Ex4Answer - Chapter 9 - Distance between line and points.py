
""" Excercise 4 - Distance between line and points

Input: 
กำหนด 
- เส้นตรง L = 3x + 4y + 8 = 0 โดย A=3, B=4, C=8 ตามสมการเส้นตรง Ax+By+C = 0
- points เป็นลิสต์ของพิกัดจุด (x, y) ตามลำดับ

Process: 
- คำนวณหาระยะห่างระหว่างจุด (x, y) กับ เส้นตรง L โดยใช้สูตร 
ระยะห่างระหว่างจุดกับเส้น = absolute ของ ((A*x)+(B*y)+C) หารด้วย รากที่สองของ (A**2 + B**2)

Output: 

distance:(0,0) = 1.6
distance:(3,1) = 4.2
distance:(0,-1) = 0.8
distance:(-2,1) = 1.2
distance:(2,-2) = 1.2
distance:(-1,-2) = 0.6
distance:(-2,-3) = 2.0
distance:(3,4) = 6.6

"""

import math

def distance_between_line_and_point(x, y):
    # คำนวณระยะห่างระหว่างจุด (x, y) กับ เส้นตรง L และส่งค่ากลับ
    global A, B, C

    d = (abs((A*x)+(B*y)+C)) / math.sqrt(A**2 + B**2)
    return d

A = 3
B = 4
C = 8

points = [
    (0, 0),  # x=0, y=0
    (3, 1),  # x=3, y=1
    (0, -1),  # x=0, y=-1
    (-2, 1),  # x=-2, y=0
    (2, -2),  # x=2, y=-2
    (-1, -2),  # x=-1, y=-2
    (-2, -3),  # x=-2, y=-3
    (3, 4),  # x=3, y=4
]

# Code here
for item in points:
    x, y = item
    d = distance_between_line_and_point(x, y)
    print(f"distance:({x},{y}) = {d}")

