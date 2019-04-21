# parsing_fasta.py
# For this exercise the pseudo-code is required (in this same file)
# Write a script that:
# a) Reads sprot_prot.fasta line by line
# b) Copies to a new file ONLY the record(s) that are not from Homo sapiens
# b) And prints their source organism and sequence lenght
# Use separate functions for the input and the output


def get_lines_from_file(nameOfTheFile: str)-> list:
    with open(nameOfTheFile, "r") as file:
        return file.readlines()

# Getting not pointed sequence from pointed file
def get_particular_sequence(file, searchedString) -> 'str':
    outputLine = ""
    with open(file, "r") as inputFile:
        isTargetSequence = False
        for line in inputFile.readlines():
            if (searchedString not in line) and (">sp" in line) or isTargetSequence:
                if (searchedString not in line) and (">sp" in line) or (">sp" not in line):
                    isTargetSequence = True
                    outputLine += line
                else:
                    isTargetSequence = False

    return outputLine

print("a)")
fastaFileName = "sprot_prot.fasta"
print(get_lines_from_file(fastaFileName))

print("b)")
notHomoSapience = get_particular_sequence(fastaFileName, "Homo sapiens")
print(notHomoSapience)

print("c)")
lines = notHomoSapience.split("\n")
print("Length of ", lines[0])
count = 0
for line in lines:
    if ">sp" not in line:
        count = count + len(line)

print(count)


