# x = 10
# print(type(x))

# class student:
#     """this class is defined for doc"""
#     def __init__(self, name, age, date_of_birth):
#         self.name = name
#         self.age = age
#         self.date_of_birth = date_of_birth
    
#     def personality(self):
#         pass

# shahbaj = student('shahbaj khan', 10, '10-03-2000')
# print(student.__doc__)




# class Student:
#     "Developed by Shahbaj for Python demo"

#     def __init__(self):
#         self.name = 'Shahbaj'
#         self.age = 4
#         self.marks = 80

#     def talk(self):
#         print(f"Hello I am : {self.name}.")
#         print(f"My age is : {self.age}")
#         print(f"My marks is : {self.marks}")
    
# shahbaj = Student()
# shahbaj.talk()


# class Student:
    
#     def __init__(self, name , age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

#     def talk(self):
#         print(f"Hello My name is {self.name}")
#         print(f"My age is {self.age}")
#         print(f"My age is {self.marks}")

# obj1 = Student('Akhtar khan', 23, 98)
# obj1.talk()



# class Test:

#     def __init__(self):
#         print("Constructor executions....")

#     def m1(self):
#         print('Method execution...')

# t1 = Test()
# t2 = Test()
# t3 = Test()
# t1.m1()




# class Test:

#     def __init__(self):
#         print('Constructor execution...')
    
#     def m1(self):
#         print('m1 method execution...')


# t1 = Test()
# t2 = Test()
# t3 = Test()
# t1.m1()




# class Student:

#     def __init__(self, name, roll_no , marks):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks

#     def display(self):
#         print(f"Student name {self.name}\nRoll number {self.roll_no}\nmarks {self.marks}")

# s1 = Student('Shahbaj khan', 122, 48)
# s1.display()
# s2 = Student('Akhtar raza', 101, 99)
# s2.display()


# class Employee:

#     def __init__(self):
#         self.eno = 100
#         self.ename = 'vijay'
#         self.esal = 12000
    
# e1 = Employee()
# print(e1.__dict__)



# class Test:

#     def __init__(self):
#         self.a = 10
#         self.b = 20

#     def t1(self):
#         self.c = 30

# t = Test()
# t.t1()
# print(t.__dict__)




# class Test:

#     def __init__(self):
#         self.a = 10
#         self.b = 20

#     def t1(self):
#         self.c = 30
    
# t = Test()
# print(t.__dict__)
# t.t1()
# print(t.__dict__)
# t.d = 40
# print(t.__dict__)



# class Test:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
    
#     def t1(self):
#         self.c = 30
#         print(f"this is from contructor {self.a}, {self.b}")

# t = Test()
# t.t1()
# print(t.a)
# print(t.b)


# class Test:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#         self.c = 30
#         self.d = 40

#     def m1(self):
#         del self.d 
    
# t = Test()
# print(t.__dict__)
# t.m1()
# print(t.__dict__)
# del t.c
# print(t.__dict__)


# class Test:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#         self.c = 30

    
# t = Test()
# t1 = Test()
# del t.a
# print(t.__dict__)
# print(t1.__dict__)


# class Test:

#     def __init__(self):
#         self.a = 10
#         self.b = 20

# t1 = Test()
# t2 = Test()
# t1.a = 420
# t1.b = 419
# print(t1.__dict__)
# print(t2.__dict__)


# class Test:
#     x = 10
#     def __init__(self):
#         self.y = 20

# t1 = Test()
# t2 = Test()
# print(f"t1 {t1.x} , {t1.y}")
# print(f"t2 {t2.x}, {t2.y}")

# Test.x = 222
# t1.y = 100
# print(f"t1 {t1.x}, {t1.y}")
# print(f"t2 {t2.x}, {t2.y}")


# class Test:

#     a = 10
#     def __init__(self):
#         Test.b = 20
    
#     def m1(self):
#         Test.c  = 30
    
#     @classmethod
#     def m2(cls):
#         cls.d1 = 40
#         Test.d2 = 400

#     @staticmethod
#     def m3():
#         Test.e = 50
    
# # print(Test.__dict__)

# t = Test()
# print(Test.__dict__)

# t.m1()
# print(Test.__dict__)

# Test.m2()
# print(Test.__dict__)

# Test.m3()
# print(Test.__dict__)





# class Test:
#     a = 10
#     def __init__(self):
#         print(self.a)
#         print(Test.a)
    
#     def m1(self):
#         print(self.a)
#         print(Test.a)
    
#     @classmethod
#     def m2(cls):
#         print(cls.a)
#         print(Test.a)

#     @staticmethod
#     def m3():
#         print(Test.a)


# t = Test()
# print(Test.a)
# print(t.a)
# t.m1()
# t.m2()
# t.m2()



# class Test:
#     a = 777
#     @classmethod
#     def m1(cls):
#         cls.a = 888
    
#     @staticmethod
#     def m2():
#         Test.a = 999
    
# print(Test.a)
# Test.m1()
# print(Test.a)
# Test.m2()
# print(Test.a)


# class Test:
#     a = 10
#     def m1(self):
#         self.a = 888
    
# t1 = Test()
# t1.m1()
# print(Test.a)
# print(t1.a)

# class Test:
#     x = 10
#     def __init__(self):
#         self.y = 20

# t1 = Test()
# t2 = Test()

# print(f"t1 {t1.x}, {t1.y}")
# print(f"t2 {t2.x}, {t2.y}")


# class Test:
#     a = 10
#     @classmethod
#     def m1(cls):
#         del cls.a
    
# Test.m1()
# print(Test.__dict__)


# class Test:

#     a = 10
#     def __init__(self):
#         Test.b = 20
    



# import sys

# class Customer:

#     bank_name = 'ShahbajBank'
#     def __init__(self, name, balance = 0.0):
#         self.name = name 
#         self.balance = balance

#     def deposit(self, amt):
#         self.balance = self.balance + amt
#         print(f"Balance after deposit: {self.balance}")

#     def withdraw(self, amt):
#         if amt > self.balance:
#             print('Insufficient funds.. cannot perform this operation')
#             sys.exit()
#         self.balance = self.balance - amt
#         print(f"balance after withdraw: {self.balance}")


# print(f"Welcome to {Customer.bank_name}")
# name = input('Enter Your Name: ')
# c = Customer(name)

# while True:
#     print('D-Deposit \nw-Withdraw \nE-Exit')
#     option = input('Choose your option: ')

#     if option == 'd' or option == 'D':
#         amt = float(input('Enter amount: '))
#         c.deposit(amt)

#     elif option == 'w' or option == 'W':
#         amt = float(input('Enter amount: '))
#         c.withdraw(amt)

#     elif option == 'e' or option == 'E':
#         print('thanks for Banking')
#         sys.exit()
#     else:
#         print('Invalid option.. Plz choose valid option')




# class Test:

#     def m1(self):
#         a = 1000
#         print(a)

#     def m2(self):
#         b = 2000
#         print(b)


# t = Test()
# t.m1()
# t.m2()



# class Test:
    
#     def m1(self):
#         a = 1000
#         print(a)

#     def m2(self):
#         b = 2000
#         print(a)
#         print(b)

# t = Test()
# t.m1()
# t.m2()


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def displaY(self):
#         print(f"Hi", {self.name})
#         print(f'Your marks are {self.marks}')

#     def grade(self):
#         if self.marks >= 60:
#             print('You got first Grade')
        
#         elif self.marks >= 50:
#             print('You got a second Grade')

#         elif self.marks >= 35:
#             print('You got third Grade')

#         else:
#             print('you are failed')


# n = int(input('Enter mumber of student: '))
# for i in range(n):
#     name = input('Enter name: ')
#     marks = int(input('Enter marks'))
#     s = Student(name, marks)
#     s.displaY()
#     s.grade()
#     print()




# class Student:

#     def set_name(self, name):
#         self.name = name

#     def get_name(self):
#         return self.name
    
#     def set_marks(self, marks):
#         self.marks = marks

#     def get_marks(self):
#         return self.marks
    

# n = int(input('Enter number of students: '))
# for i in range(n):
#     s = Student()
#     name = input('Enter name: ')
#     s.set_name(name)
#     marks = int(input('Enter marks: '))
#     s.set_marks(marks)

#     print(f"Hi, {s.get_name()}")
#     print(f"Your marks are: {s.get_marks()}")
#     print()




# class Animal:
#     lEgs = 4
#     @classmethod
#     def walk(cls, name):
#         print(f"{name} walks with {cls.lEgs}...")
    
# Animal.walk('Dog')
# Animal.walk('Cat')



# class Animal:
#     legs = 4
#     @classmethod
#     def walk(cls, name):
#         print(f"{name} walks with {cls.legs} legs....")

# Animal.walk('Dog')
# Animal.walk('Cat')

# t = Animal()
# t.walk('Dogs')



# class Test:
#     count = 0
#     def __init__(self):
#         Test.count = Test.count + 1

#     @classmethod
#     def no_of_objects(cls):
#         print(f"The number of objects creted for test class: {cls.count}")

# t1 = Test()
# t2 = Test()
# Test.no_of_objects()
# t3 = Test()
# t4 = Test()
# t5 = Test()
# Test.no_of_objects()


# class Test:
#     count = 0
#     def __init__(self):
#         Test.count = Test.count+1

#     @classmethod
#     def not_of_count(cls):
#         print(f"The number of object created for the test class {cls.count}")
    
# t1 = Test()
# t2 = Test()
# Test.not_of_count()


# class ShahbajInfo:

#     @staticmethod
#     def add(x, y):
#         print('The sum: ', x+y)

#     @staticmethod
#     def product(x, y):
#         print('The product: ', x * y)
    
#     @staticmethod
#     def average(x, y):
#         print('Teh average: ', x+y/2)

    
# ShahbajInfo.add(12, 13)
# ShahbajInfo.product(12, 13)
# ShahbajInfo.average(12, 13)
# t = ShahbajInfo()
# t.add(12, 13)



# class Employee:
#     def __init__(self, eno, ename, esal):
#         self.eno = eno
#         self.ename = ename
#         self.esal = esal

#     def display(self):
#         print(f"Employee number: {self.eno}")
#         print(f"Employee name: {self.ename}")
#         print(f"Employee salary: {self.esal}")


# class Test:
#     def modify(emp):
#         emp.esal = emp.esal + 100000
#         emp.display()


# e = Employee(100, 'shahbaj', 150)
# Test.modify(e)





# class Outer:

#     def __init__(self):
#         print('Outer class object creation')
    
#     class Inner:
#         def __init__(self):
#             print('Inner class object creation')
    
#         def m1(self):
#             print("Inner class method")
    
# # O = Outer()
# # i = O.Inner()
# # i.m1()

# i = Outer().Inner()
# i.m1()



# class Person:

#     def __init__(self):
#         self.name = 'shahbaj'
#         self.db = self.Dob()
#         self.db.display()
    
#     def display(self):
#         print(f"Name: {self.name}")


#     class Dob:
#         def __init__(self):
#             self.dd = 10
#             self.mm = 5
#             self.yy = 1947
        
#         def display(self):
#             print(f"Dob {self.dd}/0{self.mm}/{self.yy}")
        

# p = Person()
# p.display()
# x = p.db
# x.display()




# class Human:

#     def __init__(self):
#         self.name = 'Sam'
#         self.head = self.Head()
#         self.brain = self.Brain()

#     def display(self):
#         print(f"Hello.. {self.name}")
    

#     class Head:
#         def talk(self):
#             print('Talking...')


#     class Brain:
#         def think(self):
#             print('Thinking...')
        

# h = Human()
# h.display()
# x = h.head
# y = h.brain
# x.talk()
# y.think()


# import gc
# print(gc.isenabled())



# import time
# class Test:
    
#     def __init__(self):
#         print('Object Initilizaiton...')
    
#     def __del__(self):
#         print('Fulfiling last wish and permorming clean up activities... ')


# t = Test()
# t = None
# time.sleep(5)
# print('End of application')


# import time
# class Test:

#     def __init__(self):
#         print('constructor Execution')
    
#     def __del__(self):
#         print('Destructor execution')
    
# t1 = Test()
# t2 = t1
# t3 = t2
# del t1
# time.sleep(5)



# class Engine:
#     a = 10
#     def __init__(self):
#         self.b = 20
    
#     def m1(self):
#         print('Engine Specific functionality')
    

# class Car:
#     def __init__(self):
#         self.engine = Engine()
    
#     def m2(self):
#         print('Car using engine class functionality')
#         print(self.engine.a)
#         print(self.engine.b)
#         self.engine.m1()

# c = Car()
# c.m2()




# class Car:
#     def __init__(self, name, model, color):
#         self.name = name
#         self.model = model 
#         self.color = color

#     def getinfo(self):
#         print(f"Car Name: {self.name}, Car Model: {self.model}, Car Color: {self.color}")
    

# class Employee:
#     def __init__(self, ename, eno, car):
#         self.ename = ename
#         self.eno = eno
#         self.car = car

#     def empinfo(self):
#         print(f"Employee Name {self.ename}")
#         print(f"Employee Number {self.eno}")
#         print(f"Employee Car info: ")
#         self.car.getinfo()

# c = Car("Innova", "2.5v", "Grey")
# e = Employee('Durga', 10000, c)
# e.empinfo()




# class P:
#     a = 10
#     def __init__(self):
#         self.b = 10

#     def m1(self):
#         print('parent instance method')
    
#     @classmethod
#     def m2(cls):
#         print('parent class Method')
    
#     @staticmethod
#     def m3():
#         print('parent static method')
    

# class C(P):
#     pass 


# c = C()
# print(c.a)
# print(c.b)
# c.m1()
# c.m2()
# c.m3()



# class P:
#     def m1(self):
#         print('Parent class method')

# class C(P):
#     def m2(self):
#         print('child class method')

# c = C()
# c.m1()
# c.m2()



class P:
    a = 10
    def __init__(self):
        self.b = 20


# class C(P):
#     c = 30
#     def __init__(self):
#         super().__init__()
#         self.d = 30

# c1 = C()
# print(c1.a, c1.b, c1.c, c1.d)




# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def eat_n_drink(self):
#         print('Eat Biryani and Drink beer')
    

# class Employee(Person):
#     def __init__(self, name, age, eno, esal):
#         super().__init__(name, age)
#         self.eno = eno
#         self.esal = esal

#     def work(self):
#         print('Coding Python is very easy just like drinking chilled beer.')
    
#     def empinfo(self):
#         print(f"Employee Name: {self.name}")
#         print(f"Employee Age: {self.age}")
#         print(f"Employee Number: {self.eno}")
#         print(f"Employee Salary: {self.esal}")
    
# e = Employee('shahbaj', 25, 1, 1200)
# e.eat_n_drink()
# e.work()
# e.empinfo()




# class Car:
#     def __init__(self, name, model, color):
#         self.name = name
#         self.model = model
#         self.color = color

#     def getinfo(self):
#         print(f"\tCar Name: {self.name}\n\tModel: {self.model}\n\t{self.model}\n\tColor: {self.color}.")
    

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def eat_n_drink(self):
#         print('Eat biryani and drink Beer')


# class Employee(Person):
#     def __init__(self, name, age, eno, esal, car):
#         super().__init__(name, age)
#         self.eno = eno
#         self.esal = esal 
#         self.car = car

#     def work(self):
#         print('coding python is very easy just like drinking chilled beer')
    
#     def empinfo(self):
#         print(f"Employee Name: {self.name}")
#         print(f"Employee Age: {self.age}")
#         print(f"Employee Esal: {self.esal}")
#         print(f"Employee Car info")
#         self.car.getinfo()

# c = Car('Innova', '2.5v', 'Grey')
# e = Employee('Durga', 48, 1, 10000, c)
# e.eat_n_drink()
# e.work()
# e.empinfo()