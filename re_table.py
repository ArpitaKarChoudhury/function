def table(a,b):
    if a==1:
        print(a,"*",b,"=",a*b)
    else:
        print(a,"*",b,"=",a*b)
        table(a-1,b)
multiplier=int(input("enter multiplier number"))
multiplicand=int(input("enter multiplicand number"))
table(multiplier,multiplicand)