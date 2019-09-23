import os
import subprocess
from Utils import Utils

pdb_dir = "/home/urfin/Education/LB-2/project/data_preparation/pdb_files/"
dssp_dir = "/home/urfin/Education/LB-2/project/data_preparation/dssp_files/"
dssp_short_dir = "/home/urfin/Education/LB-2/project/data_preparation/dssp_short/"
final_blind_data = "/home/urfin/Education/LB-2/project/data_preparation/final_blind_data.txt"

def prepare_full_dssp_files():
    list_of_pdb_files = list()
    for pdb_filename in os.listdir(pdb_dir):
        list_of_pdb_files.append(pdb_filename)

    for filename in list_of_pdb_files:
        command = "mkdssp -i " + pdb_dir + filename + " -o " + dssp_dir + filename[0:4] + ".dssp"
        print("Running the command: " + command)
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        process.wait()
        print(process.returncode)

# parse each full dssp file with consistency corespondent fasta file
# and generate for each id short secondary structure dssp file
def prepare_short_dssp_files():
    map_id_seq = Utils.get_map_from_fasta_file(final_blind_data)
    map_id_ss = dict()
    for key in map_id_seq.keys():
        with open(dssp_dir + key[0:4] + ".dssp", "r") as file:
            is_start_block = False
            ss = ""
            for line in file:
                splitted_line = line.split()
                if splitted_line[0] == "#" and splitted_line[1] == "RESIDUE":
                    is_start_block = True
                if is_start_block == True and splitted_line[2] == key[5]:
                    ss_character = Utils.get_ss_from_dssp_line(splitted_line)
                    ss += ss_character
            map_id_ss[key] = ss

        with open(dssp_short_dir + key[0:4] + ".dssp", "w") as file:
            file.write(">" + key + "\n")
            file.write(map_id_ss[key] + "\n")


if __name__ == "__main__":
    #prepare_full_dssp_files()
    prepare_short_dssp_files()