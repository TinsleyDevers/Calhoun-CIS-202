def main():

    print("Please enter a time: hours, then minutes.")
    hours = int(input("enter a hour value between 0 and 23: "))
    minutes = int(input("enter a minute value between 0 and 59: "))
    hours, minutes = validate(hours, minutes)
    print(f'You entered {hours} hours and {minutes} minutes')

def validate(hr, mins):
    HOURS = 23
    MINUTES = 59

    while hr > HOURS or hr < 0:
            print("ERROR: Hours out of range, enter valid hours")
            hr = int(input("Enter hours: "))

    while mins > MINUTES or mins < 0:
            print("ERROR: Minutes out of range, enter valid minutes")
            mins = int(input("Enter minutes: "))

    return hr, mins

main()
