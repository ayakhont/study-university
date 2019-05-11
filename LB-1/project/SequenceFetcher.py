import requests

# PDB fetching in JSON format
# https://www.rcsb.org/pages/webservices/rest-fetch
# http://www.ebi.ac.uk/pdbe/api/doc/

url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/molecules/'
idsFile = "pdbefold_ids.txt"
multiFastaFile = "pdbefold_multifasta.fasta"

def fetchSequenceById(proteinId: str, chain: str) -> str:
    result = requests.get(url + proteinId)
    data = result.json()
    structureInfo = data[proteinId]
    sequence = ''
    isFound = False
    for element in structureInfo:
        for x in element['in_chains']:
            if x == chain:
                sequence = element['sequence']
                isFound = True
        if isFound:
            break

    return sequence


def getIdBySequenceMap(fastaPath: str) -> dict:
    result = dict()
    with open(fastaPath, "r") as file:
        for line in file:
            proteinId = line[0:4]
            chain = line[5]
            element = {line[0:6]: fetchSequenceById(proteinId, chain)}
            result.update(element)

    return result

def writeMiltifasta(miltiFastaPath: str, idsWithSequences: dict):
    with open(miltiFastaPath, "w") as file:
        for key in idsWithSequences.keys():
            file.write('>' + key + '\n')
            file.write(idsWithSequences[key] + '\n')


if __name__ == '__main__':
    idBySequenceMap = getIdBySequenceMap(idsFile)
    writeMiltifasta(multiFastaFile, idBySequenceMap)