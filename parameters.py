def Compute_Grade(tmp_score):     #defining function

    if 0.0 <= tmp_score <= 1.0:
        if tmp_score >= 0.9:
            return 'A'
        if tmp_score >= 0.8:
            return 'B'
        if tmp_score >= 0.7:
            return 'C'
        if tmp_score >= 0.6:
            return 'D'
        return 'F'
    # Case 'score' is not on the interval
    return 'Bad score'


input_score = input('Enter score: ') #getting input

try:
    score = float(input_score)             # Only allows input floats and converting input to float
except ValueError:
    print('Bad score')
    quit()

grade = Compute_Grade(score)  # now using the function, passing through the score the user will input.
print(grade)  # printing the value that the function determined