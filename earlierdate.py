day1 = int(input("What is the first date's day? "))
month1 = int(input("What is the first date's month? "))
year1 = int(input("What is the first date's year? "))
day2 = int(input("What is the second date's day? "))
month2 = int(input("What is the second date's month? "))
year2 = int(input("What is the second date's year? "))
if year1 < year2:
    print("The first date comes before the second date.")
if year2 < year1:
    print("The first date comes after the first date.")
if year1 == year2 and month1 < month2:
    print("The first date comes before the second date.")
if year1 == year2 and month1 > month2:
    print("The first date comes after the first date.")
if year1 == year2 and month1 == month2 and day1 < day2:
    print("The first date comes before the first date.")
if year1 == year2 and month1 == month2 and day1 > day2:
    print("The first date comes after the second date date.")
if year1 == year2 and month1 == month2 and day1 == day2:
    print("They are all the same. ")