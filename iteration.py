min = 0
count = 0

while True:
    x = input("Enter a number (or 'done' to finish): ")

    if x == "done":
        break

    try:
        x = float(x)
        min = x+min
        count = count+1
    except ValueError:
        print("Enter valid input")
    if count > 0:
            avg = min / count
            print("average is", avg)
    else:
            print("no numbers entered")




