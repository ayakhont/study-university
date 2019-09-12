blind_data = "/home/urfin/Education/LB-2/project/data_preparation/blind_data.txt"
clustered_data = "/home/urfin/Education/LB-2/project/data_preparation/clustered.txt"
filtered_blind_data = "/home/urfin/Education/LB-2/project/data_preparation/filtered_blind_data.txt"


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

# build a map of seq Id ant it's sequence in one string
def get_map_from_fasta_file(file):
    map = dict()
    with open(blind_data, "r") as f:
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

def filter_out_from_clustered_data(clustered_data, filtered_blind_data):
    clustered_list = list()
    blind_data_dict = dict()
    # read the first 150 lines and each first seq Id from each of them
    with open(clustered_data, "r") as f:
        lines = f.readlines()
        for i in range(0, 150):
            line = lines[i]
            clustered_list.append(line[0:7])
    #with open(filtered_blind_data, "w") as file:


if __name__ == "__main__":
    #filter_out_blind_data(blind_data)
    print(get_map_from_fasta_file(blind_data))