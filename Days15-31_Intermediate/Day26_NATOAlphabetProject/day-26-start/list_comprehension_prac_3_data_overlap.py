with open("file1.txt") as file1:
    list1 = file1.readlines()
    list1_formatted = [int(item.strip()) for item in list1]

with open("file2.txt") as file2:
    list2 = file2.readlines()
    list2_formatted = [int(item.strip()) for item in list2]

result = [num for num in list1_formatted if num in list2_formatted]

print(result)
