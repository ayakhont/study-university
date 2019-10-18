import os
from Bio.PDB import PDBParser, Selection, PPBuilder


class Utils:

    # build a map of seq Id ant it's sequence in one string
    @staticmethod
    def get_map_from_fasta_file(fasta_file) -> dict:
        map = dict()
        with open(fasta_file, "r") as f:
            lines = f.readlines()
            current_seq = ""
            for i in range(0, len(lines)):
                line = lines[i]
                if line[0] == ">":
                    map[line[1:7]] = ""
                    current_seq = line[1:7]
                else:
                    current = line.rstrip()
                    seq = map[current_seq] + current
                    map[current_seq] = seq
        return map

    @staticmethod
    def get_map_from_pdb_files(pdb_dir: str, list_of_ids: list) -> dict:
        map_id_to_sequence = dict()
        parser = PDBParser()
        for id in list_of_ids:
            with open(pdb_dir + id[0:4] + ".pdb", "r") as file:
                structure = parser.get_structure(id[0:4], file)
                ppb = PPBuilder()
                sequence = ""
                for pp in ppb.build_peptides(structure):
                    if pp[0].parent._id == id[5]:
                        sequence += pp.get_sequence()._data
                map_id_to_sequence[id] = sequence

        return map_id_to_sequence

    @staticmethod
    # H, G, I -> H
    # B, E -> E
    # T, S, “” -> C
    def get_ss_from_dssp_line(splitted_line: list) -> str:
        if splitted_line[4] == "H" or splitted_line[4] == "G" or splitted_line[4] == "I":
            return "H"
        elif splitted_line[4] == "B" or splitted_line[4] == "E":
            return "E"
        else:
            return "C"

    @staticmethod
    def convert_ss_type_to_number(ss_type: str) -> int:
        if ss_type == "H":
            return 1
        if ss_type == "E":
            return 2
        if ss_type == "-" or ss_type == "C":
            return 3

    @staticmethod
    def convert_number_to_ss_type(number: int) -> str:
        if number == 1:
            return "H"
        if number == 2:
            return "E"
        if number == 3:
            return "-"
