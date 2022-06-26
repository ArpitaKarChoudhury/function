# Examples: (Input --> Output)
# 13 --> "drink toddy"
# 17 --> "drink coke"
# 18 --> "drink beer"
# 20 --> "drink beer"
# 30 --> "drink whisky".
def drink_age(age):
    if age<13 and 0<age:
        return "drink toddy"
    elif age<17:
        return "drink coke"
    elif age<20:
        return "drink beer"
    elif age>=20:
        return "drink whisky"