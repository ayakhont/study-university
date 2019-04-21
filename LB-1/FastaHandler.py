import re


class FastaHandler:

    pattern = re.compile("^\>sp\|(.*)\|")

    fastaPath: str = None
    buffer = None

    def __init__(self, fastaPath: str):
        self.fastaPath = fastaPath

    def searchSequenceByIds(self, ids: list) -> dict:
        result = dict()
        with open(self.fastaPath, "r") as file:
            is_read = False
            sequence = list()
            for line in file.readlines():

                if self.pattern.match(line):
                    if self.pattern.search(line).group(1) in ids:
                        is_read = True
                        sequence = list()
                        sequence.append(line)
                    elif is_read == True:
                        is_read = False
                        d = {self.pattern.search(sequence[0]).group(1): sequence}
                        result.update(d)

                if is_read == True:
                    sequence.append(line)
                    continue

                if len(result) == len(ids):
                    break

        return result

    def getIdsFromFasta(self) -> list:
        ids = list()
        with open(self.fastaPath, "r") as file:
            for line in file.readlines():
                if self.pattern.match(line):
                    ids.append(self.pattern.search(line).group(1))

        return ids

kunitzHumanFastaPath = "/home/urfin/Education/Rita Casadio/Capriotti/exercies/fasta/KunitzHuman.fasta"
handler1 = FastaHandler(kunitzHumanFastaPath)
ids = handler1.getIdsFromFasta()

notKunitzFastaPath = "/home/urfin/Education/Rita Casadio/Capriotti/exercies/fasta/noneKunitz.fasta"
handler2 = FastaHandler(notKunitzFastaPath)
print("Output:", handler2.searchSequenceByIds(ids))

