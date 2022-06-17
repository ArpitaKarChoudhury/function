# Write a function to tell user if he/she is able to vote or not.( Consider 
# minimum age of voting to be 18. )
def vote_eligibility():
    age=int(input("enter age"))
    if age>=18:
        print("He/She is eligible for vote")
    else:
        print("he/She is not eligible for vote")
vote_eligibility()