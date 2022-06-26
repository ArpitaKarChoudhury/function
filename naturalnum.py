def natural(num):
    if num==1:
        return num
    else:
        return num+natural(num-1)
z=int(input("enter number"))
print(natural(z))