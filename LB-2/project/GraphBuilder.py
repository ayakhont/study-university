import matplotlib.pyplot as plt
import numpy as np
from SecondaryStructure import SecondaryStructure


class GraphBuilder:

    def plot_bar_chart(self, residue_composition: dict):
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
        rects1 = ax.bar(x - width / 2, e_means, width/4, label='Strand')
        rects2 = ax.bar(x - width / 4, h_means, width/4, label='Helix')
        rects3 = ax.bar(x + width / 4, c_means, width/4, label='Coil')
        rects4 = ax.bar(x + width / 2, total_means, width/4, label='Total')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Number of residues')
        ax.set_title('Number of residues by group')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()

        self.autolabel(ax, rects1)
        self.autolabel(ax, rects2)
        self.autolabel(ax, rects3)
        self.autolabel(ax, rects4)
        fig.tight_layout()
        plt.show()

    @staticmethod
    def plot_pie_chart(ss: SecondaryStructure):
        ss.plot_pie_chart_graph()

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

