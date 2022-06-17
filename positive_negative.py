# Given a list of numbers, write a Python program to count positive and
# negative numbers in a List using function.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3
def pos_neg():
    i=0
    pos=0
    neg=0
    while i<len(list):
        if int(list[i])>0:
            pos=pos+1
        else:
            neg=neg+1
        i=i+1
    return pos, neg
list=[2,-7,5,-64,-14,8]
print(pos_neg())