from pypdb import get_entity_info
from math import inf

multiFastaFile = "clustered_ids.txt"

def getResolution(pdb_id):
    metadata = get_entity_info(pdb_id)
    resolution = float(metadata.get('resolution', inf))
    return resolution

def clusterSort(clusteredIdsFile):
    f = open(clusteredIdsFile)
    for cluster in f:
        resolutions = []
        ids = cluster.rstrip().split()
        for id_chain in ids:
            pdb_id = id_chain.split(':')[0]
            pdb_res = getResolution(pdb_id)
            resolutions.append(pdb_res)
        sorted_ids = list(zip(resolutions, ids))
        sorted_ids = sorted(sorted_ids)
        print(sorted_ids)
    f.close()

if __name__ == '__main__':
    clusterSort(multiFastaFile)
