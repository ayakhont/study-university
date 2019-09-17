import os
from urllib.error import HTTPError
from urllib.request import urlopen

urlForPdb = "https://files.rcsb.org/download/"


class DownloadManager:

    def __init__(self):
        return

    def downloadFileByPdbId(self, pdb_id,
                            path="/home/urfin/Education/LB-2/project/data_preparation/pdb_files/"):

        if os.path.exists(path + pdb_id + ".pdb"):
            return False

        try:
            filedata = urlopen(urlForPdb + pdb_id + ".pdb")
            datatowrite = filedata.read()

            with open(path + pdb_id + ".pdb", 'wb') as f:
                if datatowrite != None:
                    f.write(datatowrite)
                    return True

        except HTTPError:
            print("PDB file was not found by pdb ID: ", pdb_id)

        return False
