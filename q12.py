list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [10, 11, 12, 13, 14, 15]

# new list to store result
new_list = []

# add odd numbers from list1
for num in list1:
    if num % 2 != 0:
        new_list.append(num)

# add even numbers from list2
for num in list2:
    if num % 2 == 0:
        new_list.append(num)

print("New list:", new_list)