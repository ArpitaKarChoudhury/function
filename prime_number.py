# Write a function that prints all the prime numbers between 0 and limit where
#  limit is a parameter.
def prime(a):
    b=2
    while b<=a:
        i=2
        while i<=b//2:
            if b%i==0:
                break
            i=i+1
        else:
            print(b,"is a prime number")
            
        b=b+1
c=int(input("enter number"))
prime(c)