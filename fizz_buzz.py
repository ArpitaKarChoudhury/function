# Q26. Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.
def divisible():
    num=int(input("enter number"))
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%5==0:
        print("Buzz")
    elif num%3==0:
        print("Fizz")
divisible()