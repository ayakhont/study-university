# Exercise 1
# Create a list L of numbers from 21 to 39
# print the numbers of the list that are even
# print the numbers of the list that are multiples of 3
L = list()
for i in range(21, 40):
    L.append(i)

for number in L:
    if number % 2 == 0:
        print("Even number of the list: ", number)
    if number % 3 == 0:
        print("the numbers of the list that are multiples of 3: ", number)

# Exercise 2
# Print the last two elements of L
print("The last two elements: ", L[len(L) -2], " ", L[len(L) -1])

# Exercise 3
# What's wrong with the following piece of code? Fix it and
# modify the code in order to have it work AND to have "<i> is in the list"
# printed at least once

l = ['1', '2', '3']
for i in range(10):
    if str(i) in l:
        print("%d is in the list" %i)
    else:
        print("%d not found" %i)

# Exercise 4
# Read the first line from the sprot_prot.fasta file
# Split the line using 'OS=' as delimiter and print the second element
# of the resulting list

fastaFileName = "sprot_prot.fasta"


def get_second_part_of_first_line(fastaFileName)-> 'list':
    with open(fastaFileName, "r") as file:
        firstLine = file.readline()
        splitedLine = firstLine.split('OS=')
        return splitedLine


splitedLine = get_second_part_of_first_line(fastaFileName)
print(splitedLine[1])


# Exercise 5
# Split the second element of the list of Exercise 4 using blanks
# as separators, concatenate the first and the second elements and print
# the resulting string

secondPart = splitedLine[1]
splittedPart = secondPart.split(' ')
print(splittedPart[0] + splittedPart[1])


# Exercise 6
# reverse the string 'asor rosa'
print('asor rosa'[::-1])

# Exercise 7
# Sort the following list: L = [1, 7, 3, 9]
someList = [1, 7, 3, 9]
someList.sort()
print(someList)

# Exercise 8
# Create a new sorted list from L = [1, 7, 3, 9] without modifying L

someList = [1, 7, 3, 9]
newList = list(someList)
newList.sort()
print("Old list: ", someList)
print("New list: ", newList)

# Exercise 9
# Write to a file the following 2 x 2 table:
# 2 4
# 3 6
fileName = "fileWithTable.txt"
with open(fileName, "w") as file:
    file.write("2 4\n3 6")
