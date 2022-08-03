
""" Excercise 3 - Distance between 2 points

Input: 
กำหนด points เป็นลิสต์ของพิกัดข้อมูลจุด 2 จุด (x1, y1, x2, y2) ตามลำดับ

Process: 
- คำนวณหาระยะห่างระหว่างจุด (x1, y1) กับ (x2, y2) โดยใช้สูตร 
ระยะห่างระหว่างจุด = รากที่สองของ (x1-x2)**2 + (y1-y2)**2 
- คำนวณหาจุดกึ่งกลางระยะห่างระหว่างจุด (x1, y1) กับ (x2, y2) โดยใช้สูตร 
จุดกึ่งกลาง x = (x1 + x2)/2
         y = (y1 + y2)/2

Output: 

distance (0,0) กับ (1,1) = 1.414, half = (0.5, 0.5)
distance (0,0) กับ (-2,2) = 2.828, half = (-1.0, 1.0)
distance (-1,0) กับ (3,1) = 4.123, half = (1.0, 0.5)
distance (-1,-2) กับ (2,5) = 7.616, half = (0.5, 1.5)
distance (0,-2) กับ (1,2) = 4.123, half = (0.5, 0.0)

"""

import math

def distance_between_2_points(x1, y1, x2, y2):
    # คำนวณระยะห่างระหว่างจุด (x1, y1) กับ (x2, y2) และส่งค่ากลับ

    # return round(math.sqrt((x1-x2)**2 + (y1-y2)**2), 3)
    return round(math.dist((x1,y1), (x2,y2)), 3)

def half_between_2_points(x1, y1, x2, y2):
    # คำนวณระยะห่างระหว่างจุด (x1, y1) กับ (x2, y2) และส่งค่ากลับ
    half_x = (x1 + x2)/2
    half_y = (y1 + y2)/2
    return half_x, half_y

points = [
    (0, 0, 1, 1),   # x1=0 ,x2=0, y1=1, y2=1
    (0, 0, -2, 2),  # x1=0 ,x2=0, y1=-2, y2=2
    (-1, 0, 3, 1),  # x1=-1 ,x2=0, y1=3, y2=1
    (-1, -2, 2, 5), # x1=-1 ,x2=-2, y1=2, y2=4
    (0, -2, 1, 2)   # x1=0 ,x2=-2, y1=1, y2=2
]
# Code here

for item in points:
    x1, y1, x2, y2 = item
    d = distance_between_2_points(x1, y1, x2, y2)
    half_x, half_y = half_between_2_points(x1, y1, x2, y2)

    print(f"distance ({x1},{y1}) กับ ({x2},{y2}) = {d}, half = ({half_x}, {half_y})")


