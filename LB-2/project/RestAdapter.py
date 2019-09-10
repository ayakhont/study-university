from xml.dom import minidom
import requests

urlForReport = 'http://www.rcsb.org/pdb/rest/customReport.xml?pdbids='


def get_taxonomy_by_protein_id(proteinId):
    result = requests.get(urlForReport + proteinId + "&customReportColumns=taxonomy")
    xmldoc = minidom.parseString(result.text)
    element = xmldoc.getElementsByTagName("dimEntity.taxonomy")
    return element[0].childNodes[0].data