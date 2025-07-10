#Lamda In python
# add = lambda x, y: x + y
# print(add(2, 3))
# add = lambda x, y: x + y
# print(add(4,6))

#Map in python
# num1=[1,2,3,4,5]
# add_3=list(map(lambda x:x + 3, num1))
# print(add_3)

#filter in  python 
# l=[1,2,3,4,5,6,7,8,9]
# l2_3=list(filter(lambda Z:Z%3==0, l))
# print(l2_3)

#reduce
# num=[10,20,30]
# from functools import reduce
# sum_num= reduce(lambda x,y:x+y, num)
# 
# from functools import reduce

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# evens = filter(lambda x: x % 2 == 0, numbers)


# sum_of_evens = reduce(lambda a, b: a + b, evens)

# print(sum_of_evens)

#Exceptional Handling in python
# try:
#     pass
# except exception type:
#     pass
# else:

# finally:
#     pass

# try:
#     num1=int(input("Enter first number one.."))
#     num2=int(input("Enter number two.."))
#     d=num1/num2
# except ZeroDivisionError:
#     print("Second number cannot be zero")
# except ValueError:
#     print('The input value is not correct')
# else:
#     print('The result is {d}')
# finally:
#     print('program run sucessfull')

# class NegativeNumberError(Exception):
#     print("Age cannot be negative")

# def negative_age(x):
#     if x>0:
#         raise NegativeNumberError('Age cannot be negative')
#     return 'Age is valid'
# try:
#     negative_age(-1)
# except NegativeNumberError as e:
#     print(e)

#python class
# class Car:
#     def __init__(self, brand, model, year):  
#         self.brand = brand                   
#         self.model = model
#         self.year = year

#     def display_info(self):                
#         print(f'Build year: {self.year}, Brand: {self.brand}, Model: {self.model}')

#     def accelerate(self, speed):
#         print(f"{self.brand} {self.model} is accelerating to {speed} km/h.")

# c1 = Car("Toyato", "Hilux", 2023)
# c1.display_info()
# c1.accelerate(80)

#Overloading operator in python
# class Vector2D:
#     def __init__(self, x, y):              
#         self.x = x
#         self.y = y

#     def __str__(self):                     
#         return f'({self.x}, {self.y})'

#     def __add__(self, other):             
#         return Vector2D(self.x + other.x, self.y + other.y)
#     def __sub__(self, other):
#        return Vector2D(self.x - other.x, self.y - other.y)


# v1 = Vector2D(2, 3)
# v2 = Vector2D(3, 4)

# result = v1 + v2
# result1 = v1 - v2
# print("result of v1 - v2 is:", result1)
# print("Result of v1 + v2:", result)

# class parent:
#     def greet(self):
#         print("Hello from parents")
# class child(parent):
#     def speak(self):
#        print("Hello form child")
# c=child()
# c.greet()
# c.speak()
# class Employee:
#     def __init__(self, name, basesalary):
#         self.name = name
#         self.basesalary = basesalary

#     def get_details(self):
#         return f'Employee Name: {self.name}, Salary: {self.basesalary}'

# class Manager(Employee):
#     def __init__(self, name, basesalary, bonus):
#         super().__init__(name, basesalary)
#         self.bonus = bonus

#     def get_details(self):
#         base = super().get_details()
#         return f"{base}, Bonus: {self.bonus}"
    

# e1 = Employee('Krish', 10000)
# m1 = Manager('Ram', 20000, 5000)

# print(e1.get_details())
# print(m1.get_details())

#Mixing in python programming
# from datetime import datetime

# class LogMixin:
#     def log(self, message):
#         return f"[{datetime.now()}]: {message}"  # Call now()

# class User(LogMixin):  # Inherit from mixin
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#     def greet(self):
#         print(self.log(f"User logged in: {self.username}, Password: {self.password}"))

# # Usage
# u = User("rabin", "mypassword123")
# u.greet()

class DiscountMixin:
    def add_discount(self, percent):
        discount_amount = self.price * (percent / 100)
        discounted_price = self.price - discount_amount
        return f"Original Price: Rs. {self.price}, Price after {percent}% discount: Rs. {discounted_price}"

class Product(DiscountMixin):
    def __init__(self, name, price):
        self.name = name 
        self.price = price

    def final_price(self):
        return self.add_discount(20)

p = Product("Mobile", 20000)
print(p.final_price())











