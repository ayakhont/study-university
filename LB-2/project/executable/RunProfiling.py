import os
import subprocess

from project.PathConstants import PathConstants
from project.Utils import Utils

cmd = "psiblast -query {} -db {} -evalue 0.01 " \
      "-num_iterations 3 -out_ascii_pssm {} -num_descriptions 10000 " \
      "-num_alignments 10000 -out {}"


def run_psiblast_for_cross_validation():
    list_of_fasta_files = list()
    for fasta_filename in os.listdir(PathConstants.training_fasta_dir):
        list_of_fasta_files.append(fasta_filename)

    for filename in list_of_fasta_files:
        command = cmd.format(PathConstants.training_fasta_dir + filename,
                             PathConstants.profiling_uniprot_sprot,
                             PathConstants.profiling_pssm + filename.replace("fasta", "pssm"),
                             PathConstants.profiling_alns + filename.replace("fasta", "alns.blast"))
        print("Running the command: " + command)
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        process.wait()
        print(process.returncode)


def create_fasta_file_for_each_seq_of_blind_set():
    map = Utils.get_map_from_fasta_file(PathConstants.final_blind_data)
    for key, value in map.items():
        fasta_file_path = PathConstants.blind_fasta_dir + key + ".fasta"
        with open(fasta_file_path, "w") as file:
            file.write(">" + key + "\n" + value)


def run_psiblast_for_blind_set():
    list_of_fasta_files = list()
    for fasta_filename in os.listdir(PathConstants.blind_fasta_dir):
        list_of_fasta_files.append(fasta_filename)

    for filename in list_of_fasta_files:
        command = cmd.format(PathConstants.blind_fasta_dir + filename,
                             PathConstants.profiling_uniprot_sprot,
                             PathConstants.profiling_pssm_blind + filename.replace("fasta", "pssm"),
                             PathConstants.profiling_alns_blind + filename.replace("fasta", "alns.blast"))
        print("Running the command: " + command)
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        process.wait()
        print(process.returncode)


if __name__ == "__main__":
    # run_psiblast_for_cross_validation()
    # create_fasta_file_for_each_seq_of_blind_set()
    run_psiblast_for_blind_set()

