#prints the strings and assigns variables to the inputs
print("Welcome to the tip calculator.")
total = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? ")
split = input("How many people to split the bill? ")

#changes the data type
total_as_float = float(total)
tip_as_int = int(tip)
split_as_int = int(split)

#calculates the tip
actual_tip = 1 + tip_as_int / 100

#calcualates ammount each person should pay
pay = (total_as_float * actual_tip)/split_as_int

#rounds the pay to 2 decimal places
pay_rounded = round(pay, 2)

#ensures pay always displays 2 decimal places (1 -> 1.00, 2.4 -> 2.40, etc)
pay_formatted = '{:.2f}'.format(pay_rounded)

#prints f-string which allows variables to be called regardless of data type
print(f"Each person should pay: ${pay_formatted}")