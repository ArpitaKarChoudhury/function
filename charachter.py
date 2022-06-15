# Write a Python function that accepts a string and calculate the number of 
# upper case letters and lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12
def char(sentence):
    i=0
    upper=0
    lower=0
    while i<len(sentence):
        if sentence[i]>=chr(65) and sentence[i]<=chr(90):
            upper=upper+1
            return upper
        elif sentence[i]>=chr(97) and sentence[i]<=chr(122):
            lower=lower+1
            return lower
        i=i+1
    # print("No. of Uppercase characters:",upper)
    # print("No. of lower case charachters:",lower)
sentence="The quick Brow Fox"
print(char(sentence))