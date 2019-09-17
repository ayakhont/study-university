from xml.dom import minidom
import requests

urlForSequence = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/molecules/'
urlForReport = 'http://www.rcsb.org/pdb/rest/customReport.xml?pdbids='


class RestAdapter:

    def __init__(self):
        return

    @staticmethod
    def get_taxonomy_by_protein_id(proteinId):
        result = requests.get(urlForReport + proteinId + "&customReportColumns=taxonomy")
        if (result.status_code == 200):
            xmldoc = minidom.parseString(result.text)
            element = xmldoc.getElementsByTagName("dimEntity.taxonomy")
            if len(element) != 0:
                return element[0].childNodes[0].data

        return "None"

    @staticmethod
    def fetchSequenceById(proteinId: str, chain: str) -> str:
        result = requests.get(urlForSequence + proteinId)
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

    @staticmethod
    def getIdBySequenceMap(fastaPath: str) -> dict:
        result = dict()
        with open(fastaPath, "r") as file:
            for line in file:
                proteinId = line[0:4]
                chain = line[5]
                element = {line[0:6]: RestAdapter.fetchSequenceById(proteinId, chain)}
                result.update(element)

        return result

    @staticmethod
    def writeMiltifasta(miltiFastaPath: str, idsWithSequences: dict):
        with open(miltiFastaPath, "w") as file:
            for key in idsWithSequences.keys():
                file.write('>' + key + '\n')
                file.write(idsWithSequences[key] + '\n')