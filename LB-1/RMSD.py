from typing import List
from Bio import SVDSuperimposer
import numpy as np


class RMSD:

    ATOM_MARK: str = "ATOM"
    AMINO_DICT = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
                  'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
                  'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
                  'ALA': 'A', 'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M',
                  'ALYS': 'K', 'ASER': 'S'}

    def __init__(self, alignmentFileName, pdb1FileName, pdb2FileName):
        self.alignmentFileName = alignmentFileName
        self.pdb1FileName = pdb1FileName
        self.pdb2FileName = pdb2FileName

    @staticmethod
    def get_atoms(pdbfile: str, chain: str, atm: str = 'CA') -> List[list]:
        result = list()

        with open(pdbfile, "r") as file:
            # counter = 0

            for line in file:
                # colomns = line.split()

                if line[:4] != RMSD.ATOM_MARK:
                    continue
                if line[21] != chain:
                    continue
                if line[12:16].strip() != atm:
                    continue
                x = float(line[30:38])
                y = float(line[38:46])
                z = float(line[46:54])
                coord = [x, y, z]

                result.append(coord)
                # if colomns[0] == RMSD.ATOM_MARK and colomns[2] == atm:
                #     if RMSD.AMINO_DICT[colomns[3]] == chain[counter]:
                #         coordinates = list()
                #         coordinates.append(chain[counter])
                #         coordinates.append(colomns[6])
                #         coordinates.append(colomns[7])
                #         coordinates.append(colomns[8])
                #         result.append(coordinates)
                #     elif int(colomns[5]) != (counter + 1):
                #         raise Exception("Smth with numeration. {0} != {1}".format(colomns[5], counter + 1))
                #     else:
                #         raise Exception("{0}th Sequence in chain doesn't match sequence in PDB!".format(counter))
                #
                #     counter += 1
                #     if counter == len(chain):
                #         break

        return result

    @staticmethod
    def distance(p1, p2):
        np.sqrt(np.sum((p1 - p2)**2))



    def super_prot(self, ca1, ca2):
        sup = SVDSuperimposer()
        sup.set(ca1, ca2)
        sup.run()
        return sup.get_rms()


if __name__ == "__main__":

    seqTarget = "AIGPAASLVVANAPVSPDGFLRDAIVVNGVFPSPLITGKKGDRFQLNVVDTLTNHTMLKSTSIHWHGFFQAGTNWADGPA"
    listOfCoordinates = RMSD.get_atoms("1gyc.pdb", 'A')
    n = len(listOfCoordinates)
    for i in range(n-1):
        d = RMSD.distance(listOfCoordinates[i,], listOfCoordinates[i+1, ])





