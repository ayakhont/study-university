import os
import matplotlib.pyplot as plt
import numpy as np
from SecondaryStructure import SecondaryStructure
from GraphBuilder import GraphBuilder

dssp_dir = "/home/urfin/Dropbox/EBP 2018/LB2/Castrense/project/dssp/"
fasta_dir = "/home/urfin/Dropbox/EBP 2018/LB2/Castrense/project/fasta/"


def calculate_statistics(ss_composition: SecondaryStructure, residue_composition: dict):
    try:
        for dssp_filename in os.listdir(dssp_dir):
            with open(dssp_dir + dssp_filename, "r") as dssp_file:
                fasta_filename = dssp_filename.replace("dssp", "fasta")
                with open(fasta_dir + fasta_filename, "r") as fasta_file:
                    fasta_line = ''
                    for line in fasta_file:
                        if line[0] != '>':
                            fasta_line = line
                    for dssp_line in dssp_file:
                        if dssp_line[0] != '>':
                            ss_composition.e_count += dssp_line.count("E")
                            ss_composition.h_count += dssp_line.count("H")
                            ss_composition.c_count += dssp_line.count("-")

                            if len(dssp_line) == len(fasta_line):
                                for i in range(0, len(dssp_line)):
                                    residue = fasta_line[i]
                                    ss = dssp_line[i]
                                    if residue in residue_composition.keys():
                                        obj = residue_composition.get(residue)
                                    else:
                                        obj = SecondaryStructure()
                                    obj.update_counter(ss)
                                    residue_composition[residue] = obj
                            else:
                                print("These files contains different length of string in sequences: ",
                                      dssp_file)
    except IOError:
        print("IO error!!")


def print_statistics(ss_composition: SecondaryStructure, residue_composition: dict):
    common_character = ss_composition.e_count + ss_composition.h_count + ss_composition.c_count
    print("Strand count: ", ss_composition.e_count)
    print("Helix count: ", ss_composition.h_count)
    print("Coil count: ", ss_composition.c_count)
    print("Common character: ", common_character)

    print("Residue composition: ")
    for key in residue_composition.keys():
        print("{}: {}".format(key, residue_composition.get(key).get_string()))


if __name__ == "__main__":
    ss_composition = SecondaryStructure()
    residue_composition = dict()
    graphBuilder = GraphBuilder

    calculate_statistics(ss_composition, residue_composition)
    print_statistics(ss_composition, residue_composition)

    graphBuilder.plot_pie_chart(ss_composition)
    graphBuilder.plot_bar_chart(graphBuilder, residue_composition)







