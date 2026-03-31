min = 0
max = 0
while True:
    x = input("Enter a number (or 'done' to finish): ")

    if x == "done":
        break

    try:
        x = float(x)
        if x < min:
            min = x
        if x > max:
            max = x
    except ValueError:
        print("Enter valid input")
print("Minimum is",min)
print("Maximum is",max)



