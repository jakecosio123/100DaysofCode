#Write your code below this row 👇

#loop through all numbers in range
for number in range(1,101):
    #if a number is divisible by 3 and 5 print FizzBuzz
    if number %3 == 0 and number %5 == 0:
        print("FizzBuzz")
    #if a number is divisible by 3 print Fizz
    elif number %3 == 0:
        print("Fizz")
    #if a number is divisible by 5 print Buzz
    elif number %5 == 0:
        print("Buzz")
    #for all other numbers, print the number
    else:
        print(number)