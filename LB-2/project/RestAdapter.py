from time import sleep
from xml.dom import minidom
import requests
from concurrent.futures import TimeoutError
from concurrent.futures import CancelledError
from concurrent.futures import as_completed
from requests_futures.sessions import FuturesSession

urlForSequence = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/molecules/'
urlForReport = 'http://www.rcsb.org/pdb/rest/customReport.xml?pdbids={}&customReportColumns=taxonomy'

class RestAdapter:

    def __init__(self):
        return

    @staticmethod
    def get_taxonomies_by_protein_ids(proteinIds: list, number_of_session_retry: int) -> list:
        taxonomies = list()
        try:
            with FuturesSession() as session:
                futures = [session.get(urlForReport.format(proteinId)) for proteinId in proteinIds]
                try:
                    for future in as_completed(futures, timeout=10):
                        result = future.result()
                        if result.status_code == 200:
                            xmldoc = minidom.parseString(result.text)
                            element = xmldoc.getElementsByTagName("dimEntity.taxonomy")
                            if len(element) != 0 and len(element[0].childNodes) != 0:
                                taxonomies.append(element[0].childNodes[0].data)
                except TimeoutError:
                    print("TimeoutError with set of pdb ids: {}".format(proteinIds))
                except CancelledError:
                    print("CancelledError with set of pdb ids: {}".format(proteinIds))
        except Exception as e:
            print("Some exception happened: " + str(e))
            if number_of_session_retry > 0:
                sleep(60)
                number_of_session_retry -= 1
                taxonomies = RestAdapter.get_taxonomies_by_protein_ids(proteinIds, number_of_session_retry)

        return taxonomies

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