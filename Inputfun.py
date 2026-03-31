def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        overtime = hours - 40
        pay = (40 * rate) + (overtime * rate * 1.5)
    return round(pay, 2)


try:
    workhours = float(input("Enter hours: "))
    workrate = float(input("Enter rate: "))
except ValueError:
    print("Enter valid input")
    quit()

amount = computepay(workhours, workrate)
print("Your total pay is:", amount)




