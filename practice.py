def count(numbers):
    total_even = 0
    total_odd = 0
    for n in numbers:
        if n%2 == 0:
            total_even += 1
        else:
            total_odd += 1

    return total_even, total_odd

my_numbers = [1, 2, 3, 4, 5]
evens,odds=(count(my_numbers))
print(f"Even numbers:{evens}, odd numbers:{odds}")
