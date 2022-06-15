# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Output : 20
def add(list):
    i=0
    sum=0
    while i<len(list):
        sum=sum+list[i]
        i=i+1
    return sum
_list=[8,2,3,0,7]
print(add(_list))
list1=[6,3,8,6,4,0,98]
print(add(list1))