
"""
จงเขียน ฟังก์ชันคำนวณหาผลลัพธ์
Input:
    กำหนดให้ x คือ list ที่เก็บชุดข้อมูลขนาดของลูกบาศก์ (width, height, length, cube_type) หลาย ๆ ชุด
    กำหนดให้ y คือ dict เก็บค่าคงที่ a และ b ของแต่ละ cube_type

Process:
    1. หา ค่า a และ b ที่ต้องใช้จาก cube_type
    2. หาปริมาตรเฉลี่ย, ปริมาตรที่มากที่สุด, ปริมาตรที่น้อยที่สุด, ผลรวมของปริมาตรทั้งหมด และ จำนวนข้อมูลทั้งหมด ของแต่ละ cube_type
    3. หาปริมาตรเฉลี่ย, ปริมาตรที่มากที่สุด, ปริมาตรที่น้อยที่สุด, ผลรวมของปริมาตรทั้งหมด และ จำนวนข้อมูลทั้งหมด ของชุดข้อมูลทุก cube_type ทั้งหมดใน x 

    วิธีการคำนวณหาปริมาตรของโปรแกรมมีดังนี้
        1. ตรวจสอบ height ด้วยฟังก์ชัน check_height() จะได้ค่า height และ s 
        2. ตรวจสอบ s ด้วยฟังก์ชัน check_s() จะได้ค่า length
        3. คำนวณปริมาตรจาก ฟังก์ชัน calculate_volume()

สามารถเขียนฟังก์ชันเพิ่มเติมได้ (ถ้ามี)
จำนวนข้อมูล ให้แสดงผลลัพธ์เป็น int ที่เหลือให้แสดงทศนิยม 2 ตำแหน่ง 

Output ที่ต้องการ:
Result:
A: average:525.01, max:1250.87, min:232.32, sum:4725.12 count:9
B: average:869.95, max:1875.98, min:63.36, sum:6959.56 count:8
C: average:232.61, max:471.11, min:42.24, sum:1628.3 count:7
S: average:513.82, max:2227.68, min:38.53, sum:3596.71 count:7

Total: average:545.47, max:2227.68, min:38.53, sum:16909.68 count:31
"""

def check_height(height, width):
    """มีการตรวจสอบดังนี้
    ถ้า height เป็นเลขคู่ ให้เรียกใช้ ฟังก์ชัน get_new_height() แล้ว return ค่าที่ได้จาก get_new_height() และ s=2
    ถ้า height เป็นเลขคี่ ให้ return height += 1 และ s=1

    Args:
        height (float): ความสูง
        width (float): ความกว้าง

    Returns:
        float: height ใหม่ที่ได้จากการคำนวณ
        int: ค่า s เป็น 1 หรือ 2
    """
    if height%2 == 0:
        height = get_new_height(height, width)
        return height, 2
    else:
        return height+1, 1

def get_new_height(height, width):
    """คำนวณค่า height ใหม่ โดยใช้สูตร (height*b) + (width*a) + 0.5
    โดยค่า a และ b เป็น global variable แล้ว return ค่า height

    Args:
        height (float): ความสูง
        width (float): ความกว้าง
    Returns:
        float: height ใหม่ที่ได้จากการคำนวณ
    """
    global a, b

    return (height*b) + (width*a) + 0.5

def check_s(s, length):
    """ตรวจสอบค่า s
    ถ้า s = 1 length ใหม่จะมีค่าเพียง 80% ของ (length + b) 
    ถ้า s = 2 length ใหม่จะมีค่าเพียง 95% ของ (length - a) 

    Args:
        s (int): 1 หรือ 2
        length (float): ความยาว
    Returns:
        float: length ใหม่ที่ได้จากการคำนวณ
    """
    global a, b

    if s == 1:
        return 0.8*(length + b)
    else:
        return 0.95*(length - a)

def calculate_volume(height, width, length):
    """คำนวณปริมาตรจาก height * width * length
    แล้ว return ผลลัพธ์

    Args:
        height (float): ความสูง
        width (float): ความกว้าง
        length (float): ความยาว
    Returns:
        float: ปริมาตร
    """
    return height * width * length

# Add function
def get_average(x):
    return sum(x)/len(x)

def calculate_data(x):
    average_v = round(get_average(x=x), 2)
    max_v = round(max(x), 2)
    min_v = round(min(x), 2)
    sum_v = round(sum(x), 2)
    return average_v, max_v, min_v, sum_v

def show_result(average_, max_, min_, sum_, len_, name):
    print(f"{name}: average:{average_}, max:{max_}, min:{min_}, sum:{sum_} count:{len_}")

y = {
    "A": (0.5,  0.3),   # a=0.5, b=0.3
    "B": (0.4,  0.4),   # a=0.4, b=0.4
    "C": (0.3,  0.2),   # a=0.3, b=0.2
    "S": (0.2,  0.1),   # a=0.2, b=0.1
    }

x = [
    [10, 15, 3, "A"],
    [22, 8, 6, "B"],
    [10, 7, 2, "C"],
    [11, 6, 4, "A"],
    [11, 4, 4, "A"],
    [15, 12, 2, "S"],
    [19, 16, 4, "S"],
    [11, 3, 1, "C"],
    [8, 5, 4, "B"],
    [9, 1, 4, "B"],
    [9, 11, 4, "C"],
    [12, 7, 5, "A"],
    [13, 8, 5, "S"],
    [16, 9, 9, "B"],
    [17, 12, 10, "B"],
    [15, 9, 2, "A"],
    [13, 8, 1, "S"],
    [14, 2, 6, "C"],
    [15, 4, 5, "A"],
    [12, 3, 4, "C"],
    [11, 7, 3, "A"],
    [16, 7, 7, "B"],
    [17, 17, 9, "S"],
    [15, 4, 6, "C"],
    [10, 8, 13, "B"],
    [13, 8, 5, "B"],
    [14, 6, 4, "S"],
    [9, 3, 2, "C"],
    [19, 7, 3, "S"],
    [21, 17, 3, "A"],
    [22, 6, 5, "A"],
]

# Code here
d_cube = {}

for item in x:
    width, height, length, cube_type = item
    a, b = y.get(cube_type) 

    # calculate
    height, s = check_height(height, width)
    length = check_s(s, length)
    v = calculate_volume(width, height, length)
    # print(cube_type, a,b, v)

    # put data to dict
    if cube_type not in d_cube:
        d_cube[cube_type] = []
    d_cube[cube_type].append(v)

# show result
print("Result:")
total = []
for cube_type, list_volume in d_cube.items():
    average_v, max_v, min_v, sum_v = calculate_data(x=list_volume)
    show_result(average_v, max_v, min_v, sum_v, len(list_volume), cube_type)
    total += list_volume
average_v, max_v, min_v, sum_v = calculate_data(x=total)
print()
show_result(average_v, max_v, min_v, sum_v, len(total), "Total")
