def greet():
    print("Hello, welcome to the internship!")
greet()

def add_numbers(a,b):
    return a+b

result = add_numbers(5,3)
print(result)

x=10
def show_value():
    x=5
    print(x)
show_value()
print(x)

import math
import random
print(math.sqrt(16))
print(random.randint(1,10))

print("task 1,area and perimeter")
def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))  

area, perimeter = calc_rectangle(length, width)
print("The area of the rectangle is: ", area)
print("The perimeter of the rectangle is: ", perimeter)


