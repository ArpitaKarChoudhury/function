# generate_range(2, 10, 2) # should return list of [2,4,6,8,10]
# generate_range(1, 10, 3) # should return list of [1,4,7,10]
# generate_range(2, 10, 2) # should return array of [2, 4, 6, 8, 10]
# generate_range(1, 10, 3) # should return array of [1, 4, 7, 10]
# Note
# min < max
# step > 0
def list():
    a=[]
    min = int(input("enter number"))
    max=int(input("enter max number"))
    step=int(input("enter step number"))
    while min<=max:
        a.append(min)
        min=min+step
    return a
print(list())
print(list())
print(list())