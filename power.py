# Complete the function that takes a non-negative integer n as input, 
# and returns a list of all the powers of 2 with the exponent ranging 
# from 0 to n (inclusive).
# n=0 == >[1] #[2^0]
# n = 1 ==> [1, 2] # [2^0, 2^1]
# n = 2 ==> [1, 2, 4] # [2^0, 2^1, 2^2].
def power (n):
    a=0
    list=[]
    d=int(input("enter number"))
    while a<=n:
        c=d**a
        list.append(c)
        a=a+1
    return list      
z=int(input("enter the power"))
print(power(z))