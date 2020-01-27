import collections
from typing import Dict

import matplotlib.pyplot as plt
import numpy as np
from project.SecondaryStructure import SecondaryStructure
import seaborn as sns
import pandas as pd


class GraphBuilder:

    def convert_to_data_frame(self, residue_composition: dict) -> pd.DataFrame:
        for key, value in residue_composition.items():
            residue_composition[key] = value.convert_to_list()
        data_frame = pd.DataFrame.from_dict(residue_composition)
        return data_frame

    def plot_bar_chart(self, residue_composition: dict):
        labels = residue_composition.keys()
        e_means = []
        h_means = []
        c_means = []
        total_means = []
        total = 0
        total_e = 0
        total_h = 0
        total_c = 0
        for key in labels:
            obj = residue_composition.get(key)
            total += obj.e_count + obj.h_count + obj.c_count
            total_e += obj.e_count
            total_h += obj.h_count
            total_c += obj.c_count
        for key in labels:
            obj = residue_composition.get(key)
            e_means.append(obj.e_count/total_e*100)
            h_means.append(obj.h_count/total_h*100)
            c_means.append(obj.c_count/total_c*100)
            total_means.append((obj.e_count + obj.h_count + obj.c_count)/total*100)

        x = np.arange(len(labels))  # the label locations
        width = 0.6  # the width of the bars

        fig, ax = plt.subplots()
        ax.bar(x - width / 2, e_means, width/4, label='Strand')
        ax.bar(x - width / 4 + 0.05, h_means, width/4, label='Helix')
        ax.bar(x + width / 4 - 0.05, c_means, width/4, label='Coil')
        ax.bar(x + width / 2, total_means, width/4, label='Total')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('% of total amount for each type')
        ax.set_title('Number of residues grouped by symbol')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()

        fig.tight_layout()
        plt.show()

    @staticmethod
    def plot_pie_chart(obj):
        if isinstance(obj, SecondaryStructure):
            obj.plot_pie_chart_graph()
        if isinstance(obj, dict):
            GraphBuilder.plot_pie_chart_graph_for_dict(obj)

    @staticmethod
    def plot_pie_chart_graph_for_dict(taxonomy_statistics: dict):
        sorted_taxonomy_statistics = sorted(taxonomy_statistics.items(), key=lambda kv: kv[1],
                                            reverse=True)
        sorted_dict = collections.OrderedDict(sorted_taxonomy_statistics)
        labels = list()
        sizes = list()
        total = sum(sorted_dict.values())
        others = 0
        showing_number = 8
        for key, value in sorted_dict.items():
            if showing_number > 0:
                labels.append(key)
                sizes.append(value/total*100)
                showing_number -= 1
                continue
            others += value
        labels.append("Others")
        sizes.append(others/total*100)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        plt.show()


    @staticmethod
    def autolabel(ax, rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 4, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

