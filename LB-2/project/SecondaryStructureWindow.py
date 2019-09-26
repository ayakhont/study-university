import matplotlib.pyplot as plt
import numpy as np
from typing import List


class SecondaryStructureWindow:
    e_counts: List[float]
    h_counts: List[float]
    c_counts: List[float]
    common_counts: List[float]

    def __init__(self, window_size: int):
        self.e_counts = list(np.zeros(window_size, float))
        self.h_counts = list(np.zeros(window_size, float))
        self.c_counts = list(np.zeros(window_size, float))
        self.common_counts = list(np.zeros(window_size, float))

    def update_counter(self, letter_for_secondary_structure: str, position: int):
        if letter_for_secondary_structure == "E":
            self.e_counts[position] += 1.0
            self.common_counts[position] += 1.0
        if letter_for_secondary_structure == "H":
            self.h_counts[position] += 1.0
            self.common_counts[position] += 1.0
        if letter_for_secondary_structure == "-" or letter_for_secondary_structure == "C":
            self.c_counts[position] += 1.0
            self.common_counts[position] += 1.0

    def get_string(self):
        return "Strand: {}\n, Helix: {}\n, Coil: {}\n, Common: {}\n"\
            .format(self.e_counts, self.h_counts, self.c_counts, self.common_counts)

    def plot_pie_chart_graph(self):
        labels = 'Strand', 'Helix', 'Coil'
        sizes = [self.e_counts, self.h_counts, self.c_counts]

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        plt.show()