score=input("Enter your score: ")
try:
    if float(score) > 1.0 or float(score) < 0:
        print("Please enter a valid score")
    elif float(score) >= 0.9:
        print("Your Grade is A")
    elif float(score) >= 0.8:
        print("Your Grade is B")
    elif float(score) >= 0.7:
        print("Your Grade is C")
    elif float(score) >= 0.6:
        print("Your Grade is D")
    elif float(score) < 0.6:
        print("Your Grade is F")
except:
    print("Please enter a valid numerical score")


