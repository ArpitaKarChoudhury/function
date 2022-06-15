# Q16.Print multiplication table of 12 using function.
def multiple(num):
    i=1
    while i<=10:
        print(num,"*",i,"=",num*i)
        i=i+1
num=int(input("enter number"))
multiple(num)