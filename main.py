myList = [1, 4, 6, 9, 10, 56, 42, 36, 90, 21, 65, 32, 67, 85, 1, 56, 753, 133, 632, 123, 789, 86, 432, 56, 43, 212, 789,
          6313, 3467, 43, 224, 6432, 5774, 21, 3, 68, 0, 6, 42, 1, 2, 4, 57]
found = False
i = 0

num = int(input("Type the number to search for "))

while found is False and i < len(myList):
    if myList[i] == num:
        print(num, 'found at position', i)
        found = True
    else:
        i += 1
if found is False:
    print("Your number is not in the list")