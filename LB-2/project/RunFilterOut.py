import os
import pickle

from project.DownloadManager import DownloadManager
from project.PathConstants import PathConstants
from project.Utils import Utils


# clear data received from PDB:
# - remove similar chains
# - remove chains shorter than 50 residues
# - remove trash from sequence headers
# write result in blind_data
def filter_out_blind_data(blind_data):
    new_list = list()
    with open(blind_data, "r") as f:
        lines = f.readlines()
        headers = list()
        delete_next_line = False
        for i in range(0, len(lines)):
            line = lines[i]
            next_line = ""
            if i != (len(lines) - 1):
                next_line = lines[i+1]
            if delete_next_line == True:
                if len(next_line) != 0 and next_line[0] == ">":
                    delete_next_line = False
                continue
            if line[0] == ">":
                line = line[0:7] + "\n"
                if line[0:5] in headers or len(next_line) < 50:
                    delete_next_line = True
                    continue
                headers.append(line[0:5])
            new_list.append(line)
    with open(blind_data, "w") as file:
        for line in new_list:
            file.write(line)


# map first sequences
# from clustered data (clustered_data)
# to new file with blind data set (filtered_blind_data)
def filter_out_clustered_data(clustered_data, filtered_blind_data):
    clustered_list = list()
    blind_data_dict = dict()
    # read the first 150 lines and each first seq Id from each of them
    with open(clustered_data, "r") as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            clustered_list.append(line[0:6])

    blind_data_dict = Utils.get_map_from_fasta_file(PathConstants.blind_data)

    with open(filtered_blind_data, "w") as file:
        for key in clustered_list:
            file.write(">" + key + "\n")
            file.write(blind_data_dict[key] + "\n")


# 1) sort tab output file by similarity and chose 150 sequences with the lowest similarity level
# 2) download each of these sequence to appropriate pdb file
def filter_out_considering_training_set(plastp_tab):
    tab_list = list()
    with open(plastp_tab, "r") as file:
        for line in file:
            inner_list = line.split()
            tab_list.append(inner_list)
    tab_list.sort(key=lambda x: float(x[2]))

    dm = DownloadManager()
    count = 0
    i = 0
    list_of_downloaded_id = list()
    while count < 150:
        splitted_line = tab_list[i]
        key = splitted_line[0]
        key = key[0:4]
        is_download_successful = dm.downloadFileByPdbId(key)
        if is_download_successful:
            count += 1
            list_of_downloaded_id.append(splitted_line[0])
        i += 1

    return list_of_downloaded_id


# write down each of filtered seq to final_blind_data file
def create_final_blind_data_file(final_blind_data, list_of_downloaded_id):
    blind_data_dict = Utils.get_map_from_pdb_files(PathConstants.blind_pdb_dir, list_of_downloaded_id)
    with open(final_blind_data, "w") as file:
        for key in list_of_downloaded_id:
            file.write(">" + key + "\n")
            file.write(blind_data_dict[key] + "\n")


if __name__ == "__main__":
    #filter_out_blind_data(blind_data)
    #filter_out_from_clustered_data(clustered_data, filtered_blind_data)
    if os.path.isfile(PathConstants.dump_list_of_pdb_ids):
        with open(PathConstants.dump_list_of_pdb_ids, 'rb') as file:
            list_of_downloaded_id = pickle.load(file)
    else:
        list_of_downloaded_id = filter_out_considering_training_set(PathConstants.plastp_tab)
        with open(PathConstants.dump_list_of_pdb_ids, 'wb') as file:
            pickle.dump(list_of_downloaded_id, file)
    create_final_blind_data_file(PathConstants.final_blind_data, list_of_downloaded_id)

