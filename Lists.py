random_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
corrected_list = []
user_number = int(input("You can choose number for check how good that program works with that list !"))
for i in random_list:
    if i < user_number :
        corrected_list.append(i)
if not corrected_list:
    print('There\'s no numbers that are lower than your number in this list...')
print(corrected_list)

#one line solutions*
random_list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


print([i for i in random_list1 if i < 5])


print([x for x in random_list1 if x < int(input("Enter a number: "))])