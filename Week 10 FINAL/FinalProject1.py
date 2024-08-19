def validate(number):
    while number < 0:
        number = int(input("Enter a number greater than 0: "))
    return number

def add(num1, num2):
    return num1 + num2

def output_print(total):
    print(f"The sum of the numbers you entered is {total}")
    return total

def main():
    adding = True
    
    while adding:
        num1 = int(input("Enter a number: "))
        num1 = validate(num1)
        num2 = int(input("Enter a number: "))
        num2 = validate(num2)
        total = add(num1, num2)
        
        output_print(total)
    
        while True:
            continuecode = input("Do you want to add two numbers again? (y/n): ")
            if continuecode == 'y':
                adding = True
                break
            elif continuecode == 'n':
                print("Exiting...")
                adding = False
                break
            else:
                print("Error, please enter 'y' or 'n'.")
main()
