import os
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from SecondaryStructure import SecondaryStructure
from GraphBuilder import GraphBuilder
from Scope import Scope
from RestAdapter import RestAdapter

project_dir = "/home/urfin/Dropbox/EBP 2018/LB2/Castrense/project/"
dssp_dir = project_dir + "dssp/"
fasta_dir = project_dir + "fasta/"
scope_file_name = "dir.cla.scope.2.06-stable.txt"
tax_file_name = "./tax_file.txt"


def calculate_dssp_statistics(ss_composition: SecondaryStructure, residue_composition: dict):
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


def parse_scope_file() -> list:
    scope_list = []
    with open(project_dir + scope_file_name, "r") as file:
        for line in file:
            if line[0] != "#":
                list = line.split()
                scope = Scope(list[0], list[1])
                scope_list.append(scope)
    return scope_list


def calculate_taxonomy_statistics(scope_data: list) -> dict:
    taxonomies = dict()
    tax_file = Path(tax_file_name)
    if tax_file.exists():
        with open(tax_file, "r") as file:
            for line in file:
                list = line.split("\t")
                taxonomies[list[0]] = int(list[1])
            return taxonomies
    else:
        restAdapter = RestAdapter
        for scope in scope_data:
            taxa = restAdapter.get_taxonomy_by_protein_id(scope.pdbId)
            print(taxa)
            if taxa in taxonomies.keys():
                current_counter = taxonomies.get(taxa)
                current_counter += 1
                taxonomies[taxa] = current_counter
            else:
                taxonomies[taxa] = 1

        with open(tax_file, "w") as file:
            for key in taxonomies.keys():
                if key != "null" or key != "None":
                    file.write(key + "\t" + str(taxonomies.get(key)) + "\n")

    return taxonomies


if __name__ == "__main__":
    ss_composition = SecondaryStructure()
    residue_composition = dict()
    graphBuilder = GraphBuilder
    #print(calculate_taxonomy_statistics(parse_scope_file()))
    #TODO finish parsing all taxa to the local txt file
    #TODO create pie chart for taxa
    #TODO create heat map
    #TODO change the presentation of Y axis in bar chart

    calculate_dssp_statistics(ss_composition, residue_composition)
    print_statistics(ss_composition, residue_composition)

    graphBuilder.plot_pie_chart(ss_composition)
    graphBuilder.plot_bar_chart(graphBuilder, residue_composition)







