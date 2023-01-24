bill = int(input("How much is the bill? "))
tip = int(input("What percent tip would you like to leave? "))
totalprice = bill * tip / 100 + bill
print("The total price is " + str(totalprice))