blind_data = "/home/urfin/Education/LB-2/project/data_preparation/blind_data.txt"


def filter_out_blind_data():
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


if __name__ == "__main__":
    filter_out_blind_data()