import os
import subprocess

pdb_dir = "/home/urfin/Education/LB-2/project/data_preparation/pdb_files/"
dssp_dir = "/home/urfin/Education/LB-2/project/data_preparation/dssp_files/"

if __name__ == "__main__":
    list_of_pdb_files = list()
    for pdb_filename in os.listdir(pdb_dir):
        list_of_pdb_files.append(pdb_filename)

    for filename in list_of_pdb_files:
        command = "mkdssp -i " + pdb_dir + filename + " -o " + dssp_dir + filename[0:4] + ".dssp"
        print("Running the command: " + command)
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        process.wait()
        print(process.returncode)