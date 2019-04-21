class ExperimentalFile:

    # constructor creates initial file with given parameters
    def __init__(self, nameOfTheFile, text):
        with open(nameOfTheFile, "w") as file:
            file.write(text)

    # just printing the lines of given file
    @staticmethod
    def print_file(nameOfTheFile):
        with open(nameOfTheFile, "r") as file:
            for line in file:
                print(line)

nameOfTheFile = "text.txt"
text = "hfaejfhkjw1232123\nwerewerewere\n12329844587346827"
myFile = ExperimentalFile(nameOfTheFile, text)

ExperimentalFile.print_file(nameOfTheFile)

fastaFile = "example.fasta"
ExperimentalFile.print_file(fastaFile)

