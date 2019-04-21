import numpy as np


class ExercisesFromSampleExam:

    def __init__(self):
        pass

    # Receiving n and creation table by some principe
    @staticmethod
    def times_table(n: 'int')-> 'dict':
        table = dict()
        for i in range(10):
            table.update({i: i*n})
        return table

    # Printing any table
    @staticmethod
    def print_table(t: 'dict'):
        for key, value in t.items():
            print(key, " | ", value)

    # Get any table
    @staticmethod
    def get_table(t: 'dict')-> 'str':
        resultString = ""
        for key, value in t.items():
            resultString = resultString + str(key) + " | " + str(value) + "\n"
        return resultString

    # Getting pointed sequence from pointed file
    @staticmethod
    def get_particular_sequence(file, searchedString)-> 'str':
        outputLine = ""
        with open(file, "r") as inputFile:
            isTargetSequence = False
            for line in inputFile.readlines():
                if (searchedString in line) | isTargetSequence:
                    outputLine += line
                    if not line.isspace():
                        isTargetSequence = True
                    else:
                        isTargetSequence = False

        return outputLine


# Let's initialise table
n = int(input("Input the n value for table: "))

print("Result of printed table: ")

# outputting result table
ExercisesFromSampleExam.print_table(ExercisesFromSampleExam.times_table(n))

# write result table to specified file
with open("text.txt", "w") as tableFile:
    tableFile.write(ExercisesFromSampleExam.get_table(ExercisesFromSampleExam.times_table(n)))

# Let's find particular sequence in our fasta file
print("Sequence of Home Sapience from multi fasta file: ")
outputSequence = ExercisesFromSampleExam.get_particular_sequence("example.fasta", "Homo sapiens")
print(outputSequence)

# write result sequence to particular file
with open("text.txt", 'a') as fastaFile:
    fastaFile.write(outputSequence)

# some matrices manipulations
x = np.matrix(((4, 6), (2, 9)))
y = np.matrix(((12, 4), (-6, 0)))
print(x*y)







