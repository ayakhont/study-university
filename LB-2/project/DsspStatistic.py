import os
import matplotlib.pyplot as plt
import numpy as np

dssp_dir = "/home/urfin/Dropbox/EBP 2018/LB2/Castrense/project/dssp/"
fasta_dir = "/home/urfin/Dropbox/EBP 2018/LB2/Castrense/project/fasta/"


class SecondaryStructure:
    e_count: int
    h_count: int
    c_count: int

    def __init__(self):
        self.e_count = 0
        self.h_count = 0
        self.c_count = 0

    def update(self, ss):
        if ss == "E":
            self.e_count += 1
        if ss == "H":
            self.h_count += 1
        if ss == "-":
            self.c_count += 1

    def plot_pie_chart(self):
        labels = 'Strand', 'Helix', 'Coil'
        sizes = [self.e_count, self.h_count, self.c_count]

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        plt.show()


def plot_bar_chart(residue_composition: dict):
    labels = residue_composition.keys()
    e_means = []
    h_means = []
    c_means = []
    total_means = []
    for key in labels:
        obj = residue_composition.get(key)
        e_means.append(obj.e_count)
        h_means.append(obj.h_count)
        c_means.append(obj.c_count)
        total_means.append(obj.e_count + obj.h_count + obj.c_count)

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, e_means, width, label='Strand')
    rects2 = ax.bar(x - width / 4, h_means, width, label='Helix')
    rects3 = ax.bar(x + width / 4, c_means, width, label='Coil')
    rects4 = ax.bar(x + width / 2, total_means, width, label='Total')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Number of residues')
    ax.set_title('Number of residues by group')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 4, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)
    autolabel(rects4)
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    ss_composition = SecondaryStructure()
    residue_composition = dict()

    try:
        # Change the current working Directory
        print("Directory changed to ", dssp_dir)
        for dssp_filename in os.listdir(dssp_dir):
            with open(dssp_dir + dssp_filename, "r") as dssp_file:
                fasta_filename = dssp_filename.replace("dssp", "fasta")
                with open(fasta_dir + fasta_filename, "r") as fasta_file:
                    fasta_line = ''
                    for line in fasta_file:
                        if line[0] != '>':
                            fasta_line = line
                    for dssp_line in dssp_file:
                        if dssp_line[0] != '>':
                            ss_composition.e_count += dssp_line.count("E")
                            ss_composition.h_count += dssp_line.count("H")
                            ss_composition.c_count += dssp_line.count("-")

                            if dssp_line.__len__() == fasta_line.__len__():
                                for i in range(0, dssp_line.__len__()):
                                    residue = fasta_line[i]
                                    ss = dssp_line[i]
                                    if residue in residue_composition.keys():
                                        obj = residue_composition.get(residue)
                                    else:
                                        obj = SecondaryStructure()
                                    obj.update(ss)
                                    residue_composition[residue] = obj
                            else:
                                print("These files contains different length of string in sequences: ",
                                      dssp_file)
    except OSError:
        print("Can't change the Current Working Directory to ", dssp_dir)

    common_character = ss_composition.e_count + ss_composition.h_count + ss_composition.c_count
    print("Strand count: ", ss_composition.e_count)
    print("Helix count: ", ss_composition.h_count)
    print("Coil count: ", ss_composition.c_count)
    print("Common character: ", common_character)

    print("Residue composition: ", residue_composition)

    ss_composition.plot_pie_chart()
    plot_bar_chart(residue_composition)







