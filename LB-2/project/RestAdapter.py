from xml.dom import minidom
import requests

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