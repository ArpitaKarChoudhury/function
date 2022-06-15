# def max(a,b,c):
#     if a<b and c<b:
#         print("max number is",b)
#     elif a<c and b<c:
#         print("max number is",c)
#     elif b<a and c<a:
#         print("max number is",a)
# x=int(input("enter number"))
# y=int(input("enter number"))
# z=int(input("enter number"))
# max(x,y,z)

def _max1(a,b,c):
    # a=int(input("enter number"))
    # b=int(input("enter number"))
    # c=int(input("enter number"))
    if a<b and c<b:
        # print("max number is",b)
        return b
    elif a<c and b<c:
        # print("max number is",c)
        return c
    elif b<a and c<a:
        # print("max number is",a)
        return a
print(_max1(2,3,4))

