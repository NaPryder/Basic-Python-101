
"""
จงเขียน 4 ฟังก์ชัน ให้ทำงานตามที่เขียนอธิบายกำกับแต่ละฟังก์ชัน ในโครงของโปรแกรมนี้
"""

def make_int_list(x):
    # รับสตริง x มาแยกและแปลงเป็น int เก็บไว้ใน list แล้ว return ผลลัพธ์
    # เช่น x = '12 34 5' ได้ผลเป็น [12, 34, 5]
    return [int(e) for e in x.strip().split(' ')]

def is_odd(e):
    # คืนค่าจริงเมื่อ e เป็นจำนวนคี่ ถ้าไม่ใช่ คืนค่าเท็จ
    return e%2 != 0

def odd_list(alist):
    # คืน list ที่มีค่าเหมือน alist แต่มีเฉพาะตัวที่เป็นจำนวนคี่
    # เช่น alist = [10, 11, 13, 24, 25] จะได้ [11, 13, 25]
    return [e for e in alist if is_odd(e)]

def sum_square(alist):
    # คืนผลรวมของกำลังสองของแต่ละค่าใน alist
    # เช่น alist = [1,3,4] ได้ผลเป็น (1*1 + 3*3 + 4*4) = 26
    return sum([e*e for e in alist])


print(make_int_list('1 2 3 4 5'))   # ต้องได้ [1, 2, 3, 4, 5]
print(is_odd(2222))                 # ต้องได้ False
print(odd_list([1,2,3,4,5,6,7]))    # #ต้องได้ [1, 3, 5, 7]
print(sum_square([1,1,2,3]))        # #ต้องได้ 15
