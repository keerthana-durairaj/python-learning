total = 0
count = 0
while True:
    x = input("Enter a number or 'done' to end\n")
    if x == "done":
        break
    try:
       num = float(x)
       total+=num
       count+=1
    except:
        print("Enter valid input")
average = total/count
print("Total is",total,"Count is",count,"Average is",average)


