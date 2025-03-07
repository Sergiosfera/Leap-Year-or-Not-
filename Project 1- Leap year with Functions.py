def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # Check if the year is divisible by 100
        if year % 100 == 0:
            # Check if the year is divisible by 400
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year_guess=int(input("What year you wanna know if it's a leap year? "))
if is_leap_year(year_guess):
    print(f"{year_guess} is a leap year.")
else:
    print(f"{year_guess} is not a leap year.")