from Bio.Seq import Seq
from Bio.Alphabet import generic_rna
from Bio.PDB import *
import nglview as nv


messenger_rna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG", generic_rna)
my_protein = messenger_rna.translate()

parser = PDBParser()
structure = parser.get_structure('PHA-L', '1FAT.pdb')
#view = nv.show_biopython(structure)
