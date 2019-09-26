import os
from SecondaryStructure import SecondaryStructure
from SecondaryStructureWindow import SecondaryStructureWindow


class GorProfile:

    common_counter: SecondaryStructure  # common counter for all residues
    residues_dict: dict                 # dictionary for mapping residue to secondary structure object

    # initialize vector GOR profile in case of pointing out window size
    # otherwise initialize non-vector GOR profile
    def __init__(self, window_size=None):
        self.common_counter = SecondaryStructure()
        if window_size is not None:
            self.residues_dict = {
                "A": SecondaryStructureWindow(window_size), "C": SecondaryStructureWindow(window_size),
                "D": SecondaryStructureWindow(window_size), "E": SecondaryStructureWindow(window_size),
                "F": SecondaryStructureWindow(window_size), "G": SecondaryStructureWindow(window_size),
                "H": SecondaryStructureWindow(window_size), "I": SecondaryStructureWindow(window_size),
                "K": SecondaryStructureWindow(window_size), "L": SecondaryStructureWindow(window_size),
                "M": SecondaryStructureWindow(window_size), "N": SecondaryStructureWindow(window_size),
                "P": SecondaryStructureWindow(window_size), "Q": SecondaryStructureWindow(window_size),
                "R": SecondaryStructureWindow(window_size), "S": SecondaryStructureWindow(window_size),
                "T": SecondaryStructureWindow(window_size), "V": SecondaryStructureWindow(window_size),
                "W": SecondaryStructureWindow(window_size), "Y": SecondaryStructureWindow(window_size)
            }
        else:
            self.residues_dict = {
                "A": SecondaryStructure(), "C": SecondaryStructure(), "D": SecondaryStructure(),
                "E": SecondaryStructure(), "F": SecondaryStructure(), "G": SecondaryStructure(),
                "H": SecondaryStructure(), "I": SecondaryStructure(), "K": SecondaryStructure(),
                "L": SecondaryStructure(), "M": SecondaryStructure(), "N": SecondaryStructure(),
                "P": SecondaryStructure(), "Q": SecondaryStructure(), "R": SecondaryStructure(),
                "S": SecondaryStructure(), "T": SecondaryStructure(), "V": SecondaryStructure(),
                "W": SecondaryStructure(), "Y": SecondaryStructure()
            }

    def get_string(self):
        common_string = "Common counter for all residues: " + self.common_counter.get_string() + "\n"
        for key in self.residues_dict.keys():
             common_string += key + ": " + self.residues_dict[key].get_string() + "\n"
        return common_string

    # normalize non-vector GOR profile
    def normalize(self):
        sum = self.common_counter.common_count
        self.common_counter.e_count = self.common_counter.e_count / sum
        self.common_counter.h_count = self.common_counter.h_count / sum
        self.common_counter.c_count = self.common_counter.c_count / sum
        for key in self.residues_dict:
            ss = self.residues_dict[key]
            ss.e_count = ss.e_count / sum
            ss.h_count = ss.h_count / sum
            ss.c_count = ss.c_count / sum
            ss.common_count = ss.common_count / sum
            self.residues_dict[key] = ss

    # fill in GOR profile from list of dssp and fasta files
    def train_model(self, training_fasta_dir: str, training_dssp_dir: str, window_size=1):
        for dssp_filename in os.listdir(training_dssp_dir):
            with open(training_dssp_dir + dssp_filename, "r") as dssp_file:
                fasta_filename = dssp_filename.replace("dssp", "fasta")
                with open(training_fasta_dir + fasta_filename, "r") as fasta_file:
                    fasta_line = ""
                    dssp_line = ""
                    for line in fasta_file:
                        if line[0] != '>':
                            fasta_line = line
                    for dssp_line_in_file in dssp_file:
                        if dssp_line_in_file[0] != '>':
                            dssp_line = dssp_line_in_file

                    if window_size == 1:
                        self.count_non_vector_profile(dssp_line, fasta_line)
                    else:
                        self.count_vector_profile(dssp_line, fasta_line, window_size)


    def count_non_vector_profile(self, dssp_line, fasta_line):
        if len(dssp_line) == len(fasta_line):
            for i in range(0, len(dssp_line)):
                residue = fasta_line[i]
                ss = dssp_line[i]
                if residue == "X" or residue == "\n":
                    return
                secondary_structure = self.residues_dict.get(residue)
                secondary_structure.update_counter(ss)
                self.residues_dict[residue] = secondary_structure
                self.common_counter.update_counter(ss)
        else:
            print("This sequence is not equal to dssp string: ", fasta_line)


    def count_vector_profile(self, dssp_line, fasta_line, window_size: int):
        if len(dssp_line) == len(fasta_line):
            for i in range(0, len(dssp_line)):
                ss = dssp_line[i]
                for j in range(i - i//window_size, i + 1 + i//window_size):
                    if j < 0 or j >= len(fasta_line):
                        continue
                    residue = fasta_line[j]
                    if residue == "X" or residue == "\n":
                        continue
                    secondary_structure = self.residues_dict.get(residue)
                    secondary_structure.update_counter(ss, )
        else:
            print("This sequence is not equal to dssp string: ", fasta_line)
