# Mini-challenge: Largest of 3 numbers multiple times

try:
    sets = int(input("How many sets of numbers do you want to enter? "))
    if sets <= 0:
        print("Enter positive number.")
        quit()
    a_count = 0
    b_count = 0
    c_count = 0
    equal_count = 0
    tie_count = 0
    for i in range(1, sets + 1):
        print(f"\nSet {i}:")

        try:
            a = int(input("Enter number A: "))
            b = int(input("Enter number B: "))
            c = int(input("Enter number C: "))

            if a == b == c:
                print("All numbers are equal")
                equal_count += 1
            elif a==b and a>c:
                print("A and B tie as largest")
                tie_count += 1
            elif a==c and a>b:
                print("A and C tie as largest")
                tie_count += 1
            elif b==c and b>a:
                print("B and C tie as largest")
                tie_count += 1
            elif a > b and a > c:
                print("A is the largest number")
                a_count =+ 1
            elif b > a and b > c:
                print("B is the largest number")
                b_count =+ 1
            elif c > a and c > b:
                print("C is the largest number")
                c_count =+ 1

        except ValueError:
            print("Invalid input. Enter numbers only.")

    print("Summary:\n")
    print(f"A was largest {a_count} times")
    print(f"B was largest {b_count} times")
    print(f"C was largest {c_count} times")
    print(f"All numbers equal {equal_count} times")
    print(f"Ties cases {tie_count} times")
except ValueError:
    print("Invalid input. Enter a valid number of sets.")