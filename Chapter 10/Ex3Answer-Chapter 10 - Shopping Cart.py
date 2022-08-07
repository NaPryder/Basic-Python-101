class Book:

    def __init__(self, title, price, keywords):
        self.title = title
        self.price = price
        self.keywords = set(keywords)   

    def __lt__(self, rhs):
        if self.price != rhs.price:
             return self.price < rhs.price
        else: 
            return self.title < rhs.title

    def __str__(self):
        return self.title + ' ($' + str(self.price) + ')'
    
    def __repr__(self) -> str:
        return self.__str__()   # return ค่าของฟังก์ชัน __str__

    def update_price(self, new_price):
        self.price = new_price

    def get_common_keywords(self, other):
        return self.keywords & other.keywords   # intersection

# จาก class Book ให้เติม method ของ class ShoppingCart สำหรับการซื้อหนังสือผ่านเว็บไซต์
class ShoppingCart:
    def __init__(self, id):
        self.id = id
        self.books = []
        # books เก็บลิสต์ของหนังสือในตะกร้าพร้อมจำนวน เช่น [[b1,2],[b3,7]]

    def __repr__(self) -> str:
        # แสดงสตริงของ ShoppingCart ตาม format f"Shopping Cart {self.id} total:{self.get_total()}"
        return f"Shopping Cart {self.id} total:{self.get_total()}"

    def __lt__(self, other):
        # ตะกร้าที่มีราคารวมของหนังสือน้อยกว่า จะเป็นตะกร้าที่น้อยกว่า
        return self.get_total() < other.get_total()

    def add_book(self, book, n):
        # เพิ่มข้อมูลการซื้อหนังสือ book เพิ่มอีก n เล่ม โดยไม่ต้องคืนค่า
        # หากไม่มีหนังสือเล่มนี้ในตะกร้า ให้เพิ่มลิสต์ [book, n] ต่อท้าย books
        # หากเคยมีข้อมูลหนังสือเล่มนี้ในตะกร้าแล้ว ให้เพิ่มจำนวนที่ซื้ออีก n เล่ม
        # เช่น ถ้า books = [[b1,2]] และเราสั่ง add_book(b1,3) จะได้ books = [[b1,5]]

        for i, item in enumerate(self.books):
            if book==item[0]:
                self.books[i][1] += n
                break
        else:
            self.books.append([book, n])

    def delete_book(self, book):
        # ลบข้อมูลการซื้อหนังสือ book ออกจากตะกร้า โดยไม่ต้องคืนค่า
        # ถ้าในตะกร้าไม่มีหนังสือ book ไม่ต้องทำอะไร
        for i, item in enumerate(self.books):
            if book==item[0]:
                self.books.pop(i)
                break

    def get_total(self):
        # คืนค่าราคารวมของหนังสือทั้งหมดในตะกร้า

        # total = 0
        # for item in self.books:
        #     book: Book = item[0]
        #     n = item[1]
        #     total += book.price * n
        # return total
        return sum([item[0].price * item[1] for item in self.books])

    

if __name__ == '__main__':
    s1 = ShoppingCart(id=1)
    s2 = ShoppingCart(id=2)
    s3 = ShoppingCart(id=3)
    
    b1 = Book('B1', 100, ['math', 'science'])
    b2 = Book('B2', 200, ['math', 'science'])
    b3 = Book('B3', 500, ['math', 'science'])

    s1.add_book(b1, 3)  # add b1 to s1
    s1.add_book(b1, 2)  # add b1 to s1
    s1.add_book(b2, 1)  # add b2 to s1
    s1.delete_book(b1)  # delete b1 from s1

    s2.add_book(b3, 4)  # add b3 to s2
    s2.add_book(b1, 4)  # add b1 to s2
    
    # Answer
    print('---s1---')
    print(s1.books)         # [[B2 ($200), 1]]
    print(s1.get_total())   # 200

    print('---s2---')
    print(s2.books)         # [[B3 ($500), 4], [B1 ($100), 4]]
    print(s2.get_total())   # 2400

    print('---s3---')
    print(s3.books)         # [[B3 ($500), 4], [B1 ($100), 4]]
    print(s3.get_total())   # 2400

    print()
    print('---sort---')
    x = [s1, s2, s3]
    x.sort()
    print(x)                # [Shopping Cart 3 total:0, Shopping Cart 1 total:200, Shopping Cart 2 total:2400]
