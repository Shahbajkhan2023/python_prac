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
    
