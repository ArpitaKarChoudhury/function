# Write a Python function that takes a list and returns a new list with 
# unique elements of the first list.Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5].
def unique(list):
    i=0
    a=[]
    while i<len(list):
        if list[i] not in a:
            a.append(list[i])
        i=i+1
    print(a)
list1=[1,2,3,3,3,4,4,5,6]
unique(list1)
list=[6,7,5,3,4,3,0,]
unique(list)