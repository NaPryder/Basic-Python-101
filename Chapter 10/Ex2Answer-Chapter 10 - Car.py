
class Car:
    def __init__(self, license, brand, color) -> None:
        # c = Car('AA1234', 'Honda', 'White')
        # มีตัวแปร report สำหรับเก็บข้อมูลประวัติการซ่อมบำรุง โดยกำหนดค่าเริ่มต้นเป็นลิสต์ว่าง
        self.license = license   
        self.brand = brand   
        self.color = color  
        self.report = []
    
    def __str__(self) -> str:
        # คืนสตริงของรถยนต์ เช่น 'AA1234 – White Honda'
        return f"{self.license} - {self.color} {self.brand}"
    
    def __lt__(self, other):
        # เรียงลำดับรถยนต์โดยเปรียบเทียบป้ายทะเบียนรถแบบสตริง
        return self.license < other.license
    
    def __repr__(self) -> str:
        # คืนสตริงเมื่ออยู่ในการประมวลผลของ Car เช่น 'AA1234'
        return self.license

    def add_report(self, new_report):
        # เพิ่มประวัติการซ่อมบำรุง โดยไม่ต้องคืนค่า
        # ตัวแปร new_report เก็บ tuple (วันที่, คำอธิบาย, ราคา)
        # เช่น c.add_report( ('25 May 2017', 'change tires', 1500) )

        self.report.append(new_report)
    
    def total_payment(self):
        # คืนค่าใช้จ่ายทั้งหมดที่ใช้ในการซ่อมบำรุงที่ผ่านมา
        return sum([detail[2] for detail in self.report])

    def max_payment(self):
        # คืนลิสต์ของประวัติการซ่อมบำรุง (วันที่, คำอธิบาย, ราคา) ทุกรายการ ที่มีค่าใช้จ่ายมากที่สุด
        # กรณีที่รถยนต์ไม่มีประวัติการซ่อมบำรุงเลย ให้คืนค่าลิสต์ว่าง
        maxx = 0
        max_payment = []
        for i, detail in enumerate(self.report):
            if i == 0:
                maxx = detail[2]
            if detail[2] >= maxx:
                max_payment.append(detail)

        return max_payment

if __name__ == '__main__':
    # ตรวจคำตอบโดยการกด run
    a = Car('AA1234', 'Honda', 'White')

    b = Car('AA3002', 'Mazda', 'Black')
    c = Car('AX5021', 'Nissan', 'Black')
    d = Car('AA1021', 'Benz', 'Blue')
    e = Car('AB8892', 'Toyota', 'Red')

    a.add_report(('25 May 2017', 'change tires', 1500))
    a.add_report(('15 May 2018', 'checkup', 500))
    a.add_report(('2 Jan 2019', 'check system', 1500))
    a.add_report(('3 Sep 2020', 'check acc', 900))
    
    # Answer
    print(a)    # AA1234 - White Honda
    print(b)    # AA3002 - Black Mazda
    print(c)    # AX5021 - Black Nissan
    print(d)    # AA1021 - Blue Benz
    print(e)    # AB8892 - Red Toyota

    print('---payment---')
    print(f"total payment of {a} = {a.total_payment()}") # total payment of AA1234 - White Honda = 4400
    print(a.max_payment())  # [('25 May 2017', 'change tires', 1500), ('2 Jan 2019', 'check system', 1500)]
    print()
    print(f"total payment of {b} = {b.total_payment()}") # total payment of AA3002 - Black Mazda = 0
    print(b.max_payment())  # []

    print('---sort---')
    x = [a,b,c,d,e]
    x.sort()
    print(x)    # [AA1021, AA1234, AA3002, AB8892, AX5021]