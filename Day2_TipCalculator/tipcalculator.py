print("Welcome to the tip calculator.")
total = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? ")
split = input("How many people to split the bill? ")

total_as_float = float(total)
tip_as_int = int(tip)
split_as_int = int(split)

actual_tip = 1 + tip_as_int / 100
pay = (total_as_float * actual_tip)/split_as_int
pay_rounded = round(pay, 2)
pay_formatted = '{:.2f}'.format(pay_rounded)
print(f"Each person should pay: ${pay_formatted}")