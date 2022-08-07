class Book:

    def __init__(self, title, price, keywords):
        self.title = title
        self.price = price
        self.keywords = set(keywords)   

    def __lt__(self, other):
        if self.price != other.price:
             return self.price < other.price
        else: 
            return self.title < other.title

    def __str__(self):
        return self.title + ' ($' + str(self.price) + ')'
    
    def __repr__(self) -> str:
        return self.__str__()   # return ค่าของฟังก์ชัน __str__

    def update_price(self, new_price):
        self.price = new_price

    def get_common_keywords(self, other):
        return self.keywords & other.keywords   # intersection

def main():
    b1 = Book('Python', 99, ['code','computer'])    # using __init__
    b2 = Book('Calculus', 199, ['maths'])
    b3 = Book('Physics', 99, ['science','maths'])

    b1.update_price(199) 
    print(Book.get_common_keywords(b2,b3))          # {'maths'}
    if b3 < b2: print(b1)                           # using __lt__ & __str__

    # --- sort ---
    books = [b1,b2,b3]
    books.sort()                                    # using __lt__

    print(books)                                    # [Physics ($99), Calculus ($199), Python ($199)]

if __name__ == '__main__':
    
    main()