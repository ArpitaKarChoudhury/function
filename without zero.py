# Numbers ending with zeros are boring. They might be fun in your world,
#  but not here. Get rid of them. Only the ending ones.
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
# def remove_zero():
def fun_num():
    num=input("enter number")
    i=-1
    str="1"
    while 0==int(num[i]):
        str=str+"0"
        i=i-1
    num1=int(num)//int(str)
    return num1
print(fun_num())