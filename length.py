# .Write a Python program to count the number of strings where the string length
#  is 2 the first and last characters are the same from a given list of strings.
# ist=['abc', 'xyz', 'aba', '1221']
# result= 2.
def length(_list):
    i=0
    sum=0
    while i<len(_list):
        if 1<len(_list[i]):
            if _list[i][0]==_list[i][-1]:
                sum=sum+1
        i=i+1
    return sum
list=['abc','sbs','xyz','12221','a']
print(length(list))
list1=["arpita","sulagna","srestha","anindita"]
print(length(list1))