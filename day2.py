#    for loops and while loops
#for i in range(1,10):
 #   print("good morning too all frds")
#i = 1
#while i <=10:
        #print("good morning too all frds")
        #i = i + 1
#   using def function

# def greet():
#     print("hello students ")
#     print("welcome to python class ")
# greet()

# def add(a,b):
#     result = a + b
#     print(result)
# add(10,20)
# add(100,200)
#   lists
# students = ["krishna","sai","kiran","suresh"]
# students.append("sai krishna")
# students.insert(1," Rai krishna")
# students.remove("suresh")
# print(students[0:5])

#   Tupels
# students = ("krishna","sai","kiran","suresh")
# print(students[0:5])

#   Dictionaries
# students = {"name":"krishna","usn":"1GD24CI022","Department":"AIML","cgpa":7.3 }
# print(students["name"],students["usn"],students["Department"],students["cgpa"],sep="\n")


############# Class and objects  ##################

# class Student:
#     def display(self):
#         print("hello students ")
#         print("welcome to python class ")

# s1 = Student()
# s1.display()


############## constructor ##############

# class Student:
#     def __init__(self,name,usn,Department,cgpa):
#         self.name = name
#         self.usn = usn
#         self.Department = Department
#         self.cgpa = cgpa

#     def display(self):
#         print("Name : ",self.name)
#         print("USN : ",self.usn)
#         print("Department : ",self.Department)
#         print("CGPA : ",self.cgpa)

# s1 = Student("krishna","1GD24CI022","AIML",7.3)
# s2 = Student("sai","1GD24CI023","AIML",7.5)
# s1.display()
# s2.display()

############### encapsulation #################

# class student:
#     def __init__(self):
#         self.__marks = 0

#     def set_marks(self,marks):
#      self.__marks = marks

#     def show_marks(self):
#         print("Student marks:",self.__marks)


# s1 =student()
# s1.set_marks(85.5)
# s1.show_marks()


########## inheritance ##########
#      single inheritane
# class father:
#     def house(seld):
#         print("father has a house")

# class son(father):
#     def car(self):
#         print("son has a car")

# s = son()
# s.house()
# s.car()

        #   multiple inheritance

# class grandfather:
#     def land(self):
#         print("grandfather has land")

# class father(grandfather):
#     def house(self):
#         print("father has a house")

# class son(father):
#     def car(self):
#         print("son has a car")

# s = son()
# s.land()
# s.house()
# s.car()

# #        hirarical inheritance

# class grandfather:
#     def land(self):
#         print("Grandfather has land")


# class father(grandfather):
#     def house(self):
#         print("Father has a house")


# class uncle(grandfather):
#     def car(self):
#         print("Uncle has a car")


# f = father()
# f.land()
# f.house()

# print("----------------------")

# u = uncle()
# u.land()
# u.car()


#        polymorpism

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")

# animals = [Dog(),Cat(),Animal()]
# for animal in animals:
#     animal.sound()
    
#        Abstracation

# from abc import ABC, abstractmethod

# class payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass

# class UPI(payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using UPI")

# class Card(payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using Card")

# p1 = UPI()
# p2 = Card()
# p1.pay(1000)
# p2.pay(2000)
