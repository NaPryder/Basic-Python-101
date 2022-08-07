# 1. attribute
# 2. method 
    # - action 

# 4 Concepts
# 1. Encapsulate : public, private
# 2. Inheritance : child class can do something more than parent class.
# 3. Abstraction : Build structure from reality.
# 4. Polymorphism : child class can do everything which parent class can.


def main():
    
    book = get_book()
    
    print(f"{book[0]}, price={book[1]}")
    

def get_book():
    title = input('Title:')
    price = input('Price:')
    return title, price


if __name__ == '__main__':
    main()