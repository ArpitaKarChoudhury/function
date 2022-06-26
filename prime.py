i=1
a=int(input("enter number"))
b=int(input("enter number"))
sum=0
while i<=a:
    c=2
    while c<=i//2:
        if i%c==0:
            # print(i,"is not prime number")
            break
        c=c+1
    else:
        sum=sum+1
        print(i,"is prime number")
    if sum==b:
        break
    i=i+1
    