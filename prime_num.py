# Write a function to check if a number is prime or not
def prime():
    i=2
    a=int(input("enter number"))
    if a>1:   
        while i<=a//2:
            if a%i==0:
                print(a,"not a prime")
                break
            i=i+1
        else:
            print(a,"is prime")
    else:
        print(a,"is natural number")
prime()