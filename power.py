# Q15.Write a function to calculate power of a number raised to other ( a b ) .
from itertools import product


def calculate(num,power):
    product=num**power
    return product
num=int(input("enter number"))
power=int(input("enter numbber"))
print(calculate(num,power))