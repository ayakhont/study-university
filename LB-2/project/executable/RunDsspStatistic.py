import os
from pathlib import Path

from project.PathConstants import PathConstants
from project.SecondaryStructure import SecondaryStructure
from project.GraphBuilder import GraphBuilder
from project.Scope import Scope
from project.RestAdapter import RestAdapter
from time import time
from time import sleep


def calculate_dssp_statistics(ss_composition: SecondaryStructure, residue_composition: dict):
    try:
        for dssp_filename in os.listdir(PathConstants.training_dssp_dir):
            with open(PathConstants.training_dssp_dir + dssp_filename, "r") as dssp_file:
                fasta_filename = dssp_filename.replace("dssp", "fasta")
                with open(PathConstants.training_fasta_dir + fasta_filename, "r") as fasta_file:
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
                                    if residue == "X" or residue == "\n":
                                        continue
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
    with open(PathConstants.scope_file_path, "r") as file:
        for line in file:
            if line[0] != "#":
                list = line.split()
                scope = Scope(list[0], list[1])
                scope_list.append(scope)
    return scope_list


def calculate_taxonomy_statistics(scope_data: list) -> dict:
    taxonomies = dict()
    tax_file = Path(PathConstants.tax_file_path)
    if tax_file.exists():
        with open(tax_file, "r") as file:
            for line in file:
                list = line.split("\t")
                taxonomies[list[0]] = int(list[1])
            return taxonomies
    else:
        pdbIds = [obj.pdbId for obj in scope_data]
        offset = 50
        j = offset

        for i in range(0, len(pdbIds), offset):
            start = time()
            taxas = RestAdapter.get_taxonomies_by_protein_ids(pdbIds[i:j], 20)
            print("Time elapsed for bunch of requests from {} to {}: {}"
                  .format(i, j, time() - start))
            j += offset
            print("Received taxas: " + str(len(taxas)))
            sleep(5)
            for taxa in taxas:
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
    graphBuilder = GraphBuilder()

    taxonomy_statistics = calculate_taxonomy_statistics(parse_scope_file())
    graphBuilder.plot_pie_chart(taxonomy_statistics)

    #TODO create heat map
    #TODO change the presentation of Y axis in bar chart

    # calculate_dssp_statistics(ss_composition, residue_composition)
    # print_statistics(ss_composition, residue_composition)
    #
    # graphBuilder.plot_pie_chart(ss_composition)
    # graphBuilder.plot_bar_chart(residue_composition)









