# 🚨 Don't change the code below 👇
#collect input high scores, split input scores into list and save as student_scores, convert each score to an int, then print them
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#set initial high_score variable
high_score = 0

#loop through all of the scores replacing the high_score variable if the current score is higher
for score in student_scores:
    if score > high_score:
        high_score = score

#print the highest score message
print(f"The highest score in the class is: {high_score}")