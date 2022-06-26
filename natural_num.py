def natural_num(a):
    if a==1:
        print(a,end=",")
    else:
        natural_num(a-1)
        print(a,end=",")
num=int(input("enter number"))
natural_num(num)