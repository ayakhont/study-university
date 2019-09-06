import os
import sys
import matplotlib.pyplot as plt

current_dir = "/home/urfin/Dropbox/EBP 2018/LB2/Castrense/project/dssp"

if __name__ == "__main__":
    e_count = 0
    h_count = 0
    c_count = 0

    try:
        # Change the current working Directory
        os.chdir(current_dir)
        print("Directory changed to ", current_dir)
        for filename in os.listdir(os.getcwd()):
            with open(filename, "r") as file:
                for line in file:
                    if line[0] != '>':
                        e_count += line.count("E")
                        h_count += line.count("H")
                        c_count += line.count("-")
    except OSError:
        print("Can't change the Current Working Directory to ", current_dir)

    common_character = e_count + h_count + c_count
    print("Strand count: ", e_count)
    print("Helix count: ", h_count)
    print("Coil count: ", c_count)
    print("Common character ", common_character)

    labels = 'Strand', 'Helix', 'Coil'
    sizes = [e_count, h_count, c_count]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    plt.show()




