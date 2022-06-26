def fact(num):
    if num==1:
        return num
    else:
        return num*fact(num-1)
z=int(input("enter factorial number"))
print(fact(z))