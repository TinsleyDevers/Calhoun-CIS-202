numbers = []
try:
    with open('numbers.txt', 'r') as file:
        for line in file:
            numbers.append(int(line.strip()))
except FileNotFoundError:
    print("the file is not found")
else:
    total = sum(numbers)
    maximum = max(numbers)
    average = total / len(numbers)
    unique_numbers = set(numbers)

    print(f"Total of the numbers is: {total:,.2f}")
    print(f"The maximum number is: {maximum:,.2f}")
    print(f"The number greater than 200 is {maximum:,.2f}")
    print(f"The average of the numbers is: {average:,.2f}")
    print("The unique numbers in file are")
    print(*sorted(unique_numbers))
