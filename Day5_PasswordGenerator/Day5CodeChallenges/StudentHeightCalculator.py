# 🚨 Don't change the code below 👇

#ask for user to input hieghts, split them into list, convert each string to an int
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#set initial variables
total_height = 0
num_of_students = 0

#increment the variables for each height input
for student in student_heights:
    total_height += student
    num_of_students += 1

#prints a rounded average of the input heights
print(round(total_height/num_of_students))