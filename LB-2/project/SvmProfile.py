from typing import List


# 1 = Helix     : H
# 2 = Strand    : E
# 3 = Coil      : C
class SvmProfile:

    x_train: List[List[float]]
    y_train: List[int]
    window_size: int

    def __init__(self, window_size):
        self.x_train = list()
        self.y_train = list()
        self.window_size = window_size

    def add_element(self, x_vector: List[float], y: int):
        if len(x_vector) != self.window_size:
            raise Exception("The size of vector for X in SVM profile doesn't equal to window size!")
        self.x_train.append(x_vector)
        self.y_train.append(y)

    @staticmethod
    def convert_ss_type_to_number(ss_type: str):
        if ss_type == "H":
            return 1
        if ss_type == "E":
            return 2
        if ss_type == "-" or ss_type == "C":
            return 3

