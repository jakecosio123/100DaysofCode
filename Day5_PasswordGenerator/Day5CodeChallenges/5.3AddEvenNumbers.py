#Write your code below this row 👇
#set initial total variable
total = 0

#loop through each number between 2 and 101 with a step of 2 (only even numbers) and add them to the total
for number in range(2,101,2):
    total += number
    
#print the total
print(total)