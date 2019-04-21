import math
# first exercise
firstList = list()
secondList = list()
with open("neuron_data-2.txt", "r") as file:
    for line in file:
        splitResult = line.split("\t")
        if int(splitResult[0]) == 1:
            firstList.append(float(splitResult[1].rstrip()))
        else:
            secondList.append(float(splitResult[1].rstrip()))

print("First list: ", firstList)
print("Second list: ", secondList)


# average value of lists in exercise1
def get_average_value(vector: list)-> float:
    return sum(vector) / len(vector)


print("First average value: ", get_average_value(firstList))
print("Second average value: ", get_average_value(secondList))


#standart deviation
stdeviation = math.sqrt(lambda firstList: )

