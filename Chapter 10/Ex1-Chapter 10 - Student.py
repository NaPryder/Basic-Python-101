

class Student:

    def __init__(self, name, year, faculty) -> None:
        # n = Student('Krit', 4, 'Engineering')
        pass

    def __str__(self):
        # คืนสตริงของ Student เช่น 'Krit (year 4) Engineering'
        pass    

    def __repr__(self) -> str:
        # คืนสตริงเมื่ออยู่ในการประมวลผลของ Student เช่น 'Krit 4 Eng' 
        # format "{self.name} {self.year} {self.faculty[:3]}"
        pass

    def __lt__(self, other):
        # เรียงลำดับ Student ด้วยคณะตามพจนานุกรม ถ้าอยู่คณะเดียวกัน ให้เรียงลำดับด้วยชั้นปีจากน้อยไปมาก
        # ถ้าอยู่คณะและชั้นปีเดียวกัน ให้เรียงลำดับด้วยชื่อตามพจนานุกรม
        pass

if __name__ == '__main__':
    # ตรวจคำตอบโดยการกด run
    a = Student('A', 4, 'Engineering')
    b = Student('B', 3, 'Science')
    c = Student('C', 2, 'Engineering') 
    d = Student('D', 3, 'Engineering') 
    e = Student('E', 1, 'Science') 

    # Answer
    print(a)    # A (year 4) Engineering
    print(b)    # B (year 3) Science
    print(c)    # C (year 2) Engineering
    print(d)    # D (year 3) Engineering
    print(e)    # E (year 1) Science

    print('----sort----')
    x = [a, b, c, d, e]
    x.sort()

    print(x)    # [C 2 Eng, D 3 Eng, A 4 Eng, E 1 Sci, B 3 Sci]
    