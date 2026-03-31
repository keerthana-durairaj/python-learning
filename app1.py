string = 'X-DSPAM-Confidence: 0.8475'
number1 = string.find(":")
number2 = string.find(" ")
number3 = float(string[number1+1:])
print(number3)