# 1. attribute
# 2. method 
    # - action 

# 4 Concepts
# 1. Encapsulate : public, private, protect
# 2. Inheritance : child class can do something more than parent class.
# 3. Abstraction : Build structure from reality.
# 4. Polymorphism : child class can do everything which parent class can.


class Player:
   
    # constructor
    def __init__(self, ID:int, name:str, nation:str, v:int) -> None:
        self.__id = ID
        self.name = name
        self.nation = nation
        self.v = v  # m/s 
        # print('------construction-------')


    def __str__(self):
        return f"this is object: {self.name}"
    
    def get_id(self):
        return self.__id
    
    def set_id(self, new_id):
        self.__id = new_id

    def running(self, distance:float):

        time = self.calculate_time(v=self.v, s=distance)

        print(f"run {distance} m. for {time} sec.")
    
    def climbing(self,  distance:float):
        # v / 2
        v = self.v/2
        time = self.calculate_time(v=v, s=distance)

        print(f"climb {distance} m. for {time} sec.")
    
    @staticmethod   # decorator
    def calculate_time(v, s):
        return s / v

class BankAccount:
    
    def __init__(self, account:str) -> None:
        self.__account = account
        self.__balance = 0.0
    
    def get_balance(self):
        return self.__balance

    def __set_balance(self, new_balance:float):
        self.__balance = new_balance
    
    def do_deposite(self, deposite:float):

        print('check money', deposite)

        if not self.check_money_not_None(money=deposite):
            return 

        if not self.check_money_not_minus(money=deposite):
            return 

        if deposite > 200_000:
            print('error too many money')
            return 'error too many money'

        new = deposite + self.__balance

        self.__set_balance(new_balance=new)

        print(f"show new balance: {self.get_balance()}")
    
    def do_withdraw(self, withdraw:float):
        
        if not self.check_money_not_None(money=withdraw):
            return 

        if withdraw > self.__balance:
            print(f'ยอดเงินคงเหลือไม่พอ {self.__balance}')
            return 

        if withdraw < 0:
            print(f"cannot withdraw money < 0")
            return 

        self.__set_balance(new_balance=self.__balance - withdraw)     
        print(f"show new balance: {self.get_balance()}")   

    def check_money_not_None(self, money:float):
        if money is None:
            print('error')
            return False
        return True

    def check_money_not_minus(self, money:float):
        if money < 0:
            print(f"cannot process money < 0")
            return False
        return True

# parent class
class Human:

    def __init__(self, sex, name, age) -> None:
        self.sex = sex
        self.name = name
        self._age = age
        self.speed = self.calculate_speed()

    def speak(self, x):
        print('-------call from parent class -----------')
        print(f'Hi, my name is {self.name}.'*x)

    def walk(self):
        print(f'{self.name} {self.sex} walk speed : {self.speed} m/s.')

    def calculate_speed(self):
        if self.sex == "M":
            return 5
        else:
            return 3

class User:

    def __init__(self) -> None:
        self.H = Developer(sex='M', name='A', age=23, skill=31)
    
        
        property(self.H._dev())

# child class
class Developer(Human):

    def __init__(self, sex, name, age, skill) -> None:
        super().__init__(sex, name, age)
        self.skill = skill

    def _dev(self):
        print(f'dev hard play harder. {self.skill}')

    def speak(self, x):
        print('-------call from child class -----------')
        print('Hello dev')

    def debug(self):
        pass

class BA(Human):

    def __init__(self, sex, name, age) -> None:
        super().__init__(sex, name, age)
    
    def get_req(self, es_time):
        print(f'use {es_time} days for 1 requirement.')

class SeniorDev( Developer ):

    def __init__(self, sex, name, age, skill) -> None:
        super().__init__(sex, name, age, skill)

    def speak(self,x):
        print('-------call from child class 2 -----------')
        print(f"I'm senior dev: {self.name} skill:{self.skill}")
        super().speak(x)

    def debug(self):
        a = 10

class Car:

    def engine_elec(self):
        print('electric')
        return 'electric'

    def engine_fuel(self):
        print('fuel')
        return 'fuel'
    
    def system(self):
        pass

class Tesla(Car):

    def __init__(self) -> None:
        super().__init__()
        self.engine = self.engine_elec()

class Toyota(Car):
    def __init__(self) -> None:
        super().__init__()
        self.engine = self.engine_fuel()

if __name__ == '__main__':

    # A = Human(sex='M', name='A', age=15)
    
    B = Developer(sex='M', name='B', age=25, skill=51)
    B.walk()

    # E  = BA(sex='M', name='RRR', age=25)
    # # E.get_req(20)

    # C = SeniorDev(sex='M', name='C', age=25, skill=999)
    # # C.speak(1)
    # print(C.__age)

    # U = User()
    # print(U.H._age)




    # A = BankAccount(account="123456789")
    # print(A.get_balance())
    # A.do_deposite(900)
    # A.do_deposite(5000)
    # A.do_deposite(15000)
    # A.do_deposite(-80000)
    # print(A.get_balance())
    # # A.do_withdraw(-1_500_000)
    # # print(A.get_balance())

    pass

