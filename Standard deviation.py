import math

def a(num1,num2,num3,num4,num5):
    numbers = (num1+num2+num3+num4+num5)/5
    return numbers

def stdev(num1,num2,num3,num4,num5,numbers):
    s = math.sqrt((((num1-numbers)**2)+((num2-numbers)**2)+((num3-numbers)**2)+((num4-numbers)**2)+((num5 - numbers)**2))/5)
    return s

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the forth number: "))
num5 = float(input("Enter the fifth number: "))

numbers = a(num1,num2,num3,num4,num5)
print("mean= ",numbers)
s = stdev(num1,num2,num3,num4,num5,numbers)
print("Standard deviation= ", s)
