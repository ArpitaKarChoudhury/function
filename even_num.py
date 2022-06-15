# Write a function to check if a number is even or not
def even():
    i=int(input("enter number"))
    a=int(input("enter number"))
    while i<=a:
        if i%2==0:
            print(i,end=",")
        i=i+1
even()