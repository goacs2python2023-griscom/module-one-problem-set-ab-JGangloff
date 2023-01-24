distance = int(input("How far did you travel on your road trip? "))
milespergallon = int(input("What is your car's miles per gallon? "))
costofgas = int(input("How much does gas cost per gallon? "))
totalcost = distance * costofgas / milespergallon
print("You spent a total of " + str(totalcost) + " dollars on gas during you road trip")