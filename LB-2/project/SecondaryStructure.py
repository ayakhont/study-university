import matplotlib.pyplot as plt


class SecondaryStructure:
    e_count: int
    h_count: int
    c_count: int

    def __init__(self):
        self.e_count = 0
        self.h_count = 0
        self.c_count = 0

    def update_counter(self, letter_for_secondary_structure):
        if letter_for_secondary_structure == "E":
            self.e_count += 1
        if letter_for_secondary_structure == "H":
            self.h_count += 1
        if letter_for_secondary_structure == "-":
            self.c_count += 1

    def get_string(self):
        return "Strand: {}, Helix: {}, Coil: {}".format(self.e_count, self.h_count, self.c_count)

    def plot_pie_chart_graph(self):
        labels = 'Strand', 'Helix', 'Coil'
        sizes = [self.e_count, self.h_count, self.c_count]

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        plt.show()