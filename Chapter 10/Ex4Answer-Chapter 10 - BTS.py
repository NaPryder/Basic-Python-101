"""
ข้างล่างนี้แสดงคลาส Station และคลาส BTScard (อ่านคำอธิบายของแต่ละคลาสจาก comment ที่เขียน)
สถานีรถไฟฟ้าเป็นอ็อบเจกต์ของคลาส Station และบัตรโดยสารแบบเติมเงินแต่ละใบเป็นอ็อบเจกต์ของคลาส BTScard
จงเติมคำสั่งในเมท็อด add_value, enter, leave และ __lt__ ของคลาส BTScard ให้ทำงานตาม comment ที่เขียน 
(เมท็อดอื่นที่ได้เขียนคำสั่งไว้ ทำงานถูกต้องแล้ว) ดูตัวอย่างการใช้งานข้างล่างนี้ประกอบ
"""

class Station:  # คลาสของสถานีรถไฟฟ้า
    
    def __init__(self, id, name):    
        # สร้างสถานีที่มีหมายเลข (id) และชื่อสถานี (name) กำหนดให้หมายเลขสถานีเป็นจำนวนเต็ม โดยสถานีที่ติดกัน มีค่าห่างกัน 1
        self.sid = int(id)          
        self.name = name 
    
    def __str__(self) -> str:
        return self.name

    def get_price(self, other): # คืนค่าโดยสารระหว่างสถานี self และ other
        return abs(self.sid - other.sid)*5


class BTScard: # คลาสของบัตรโดยสารแบบเติมเงิน
    def __init__(self, id, value): 
        # สร้างบัตรโดยสารที่มีเลขบัตร (id) และเงินเริ่มต้น (value) 
        # self.station เก็บว่าสถานีต้นทางคือสถานีอะไร 
        # โดยถ้าบัตรไม่ได้อยู่ระหว่างการเดินทาง จะเก็บค่า สถานีต้นทางนี้เป็นสตริงว่าง ๆ

        self.cid = id  
        self.value = value 
        self.station = ''   # Object station

    def __str__(self):
        return f"Card:{self.cid} value:{self.value}"

    def add_value(self, x): 
        # เพิ่มเงินในบัตรโดยสารเท่ากับ x โดยไม่ต้อง return
        self.value += x
    
    def enter(self, station):
        # แตะบัตรเพื่อเข้าสู่สถานีรถไฟฟ้า ให้เช็คว่า บัตรนี้ไม่ได้แตะเข้าที่สถานีอื่นมาก่อน
        # ถ้าไม่มีการแตะเข้ามาก่อน ให้เปลี่ยนค่าสถานีต้นทางเป็น station แล้ว return True
        # แต่ถ้ามีการแตะเข้าสถานีอื่นมาก่อน ให้ return False โดยไม่เปลี่ยนข้อมูลสถานีต้นทางของบัตรโดยสาร

        if self.station :
            return False
        
        else:
            self.station = station
            return True

    def leave(self, station):
        # แตะบัตรเพื่อออกจากสถานีรถไฟฟ้า ให้เช็คว่า บัตรนี้มีข้อมูลสถานีต้นทางอยู่
        # ถ้าไม่มีข้อมูลสถานีต้นทาง ให้return tuple ของเงินในบัตรและ -2
        # ถ้ามีสถานีต้นทาง แต่จำนวนเงินในบัตรไม่พอจ่ายค่าโดยสาร ให้return tuple ของเงินในบัตรและ -1
        # ถ้ามีสถานีต้นทาง และจำนวนเงินในบัตรพอจ่ายค่าโดยสาร ให้ลบค่าโดยสารออกจากจำนวนเงินในบัตร
        # เปลี่ยนสถานีต้นทางเป็นสตริงว่าง แล้ว return tuple ของเงินในบัตรหลังหักค่าโดยสารและ 0
        
        if self.station :
            price = self.station.get_price(station)
            if self.value < price:
                return (self.value, -1)
            else:
                self.value -= price
                self.station = ''
                return (self.value, 0)

        else:
            return (self.value, -2)

    def __lt__(self, other): 
        # บัตรโดยสารที่มีเงินในบัตรน้อยกว่า จะถือว่าน้อยกว่า
        return self.value < other.value


if __name__ == '__main__':
    s1 = Station(1,'Siam')
    s2 = Station(3,'Mo Chit')
    s3 = Station(5,'Asok')
    
    c1 = BTScard(123, 5)    # id = 123, value= 5
    c2 = BTScard(999, 10)   # id = 999, value= 10

    # --------------------------------------------------------------
    print(s1)
    print(s2)
    print(s3)
    print()
    
    # --------------------------------------------------------------
    c1.add_value(100)   # c1 เพิ่มเงิน 100 บาท
    print(c1)           # Card:123 value:105 
    print(c1.enter(s1)) # True
    print(c1.enter(s3)) # False     # (แตะเข้าสถานีหลังจากแตะเข้าไปแล้ว)
    print(c1.leave(s2)) # (95, 0)   # คือ ออกจากสถานีแล้ว เหลือเงิน 95 บาท
    print(c1)           # Card:123 value:95
    
    #------------------------------------------------------------
    print()
    print(c2)           # Card:999 value:10
    print(c2.enter(s3)) # True
    print(c2.leave(s1)) # (10, -1)  # c2 มีเงินในบัตร 10 บาทไม่พอจ่ายค่าโดยสาร
    c2.add_value(50)    # c2 เพิ่มเงิน 50 บาท
    print(c2)           # Card:999 value:60
    print(c2.leave(s1)) # (40, 0)   # c2 เหลือเงินในบัตร 40 บาท
    print(c2.leave(s2)) # (40, -2)  # (ยังไม่ได้แตะเข้าสถานี จึงไม่มีสถานีต้นทาง)
    print(c2.enter(s2)) # True
    print(c1 < c2)      # False