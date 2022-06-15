# Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Output : "dcba4321".
from tokenize import String


def reverse(String):
    i=-1
    a=0-len(String)
    while i>=a:
        print(String[i],end="")
        i=i-1
    print()
String="1234abcd"
reverse(String)
srtng="arpita"
reverse(srtng)