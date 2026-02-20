import calendar


def is_leap_year(year):
    if calendar.isleap(year):
        return True
    else:
        return False


year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    quit
