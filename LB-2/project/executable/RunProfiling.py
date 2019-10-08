import os
import subprocess

from project.PathConstants import PathConstants

cmd = "psiblast -query {} -db {} -evalue 0.01 " \
      "-num_iterations 3 -out_ascii_pssm {} -num_descriptions 10000 " \
      "-num_alignments 10000 -out {}"


def run_psiblast():
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


if __name__ == "__main__":
    # run_psiblast()
    pass
