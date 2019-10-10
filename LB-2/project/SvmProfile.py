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
        if len(x_vector) != self.window_size * 20:
            raise Exception("The size of vector for X in SVM profile doesn't equal to 20 * window size!")
        self.x_train.append(x_vector)
        self.y_train.append(y)

    def refill_by_seq_profile(self, dssp_line: str, pssm_list: list):
        # verification on zeroes
        is_zero_profile = True
        for seq in pssm_list:
            for number in seq:
                if number != 0.0:
                    is_zero_profile = False
        if is_zero_profile:
            return

        for i in range(0, len(dssp_line)):
            vector = list()
            for j in range(i - self.window_size // 2, i + 1 + self.window_size // 2):
                if j < 0 or j >= len(dssp_line):
                    vector.extend([0.0] * 20)
                    continue
                vector.extend(pssm_list[j])
            self.add_element(vector, SvmProfile.convert_ss_type_to_number(dssp_line[i]))

    def print(self):
        for i in range(0, len(self.y_train)):
            print("{}: [{}] {}".format(self.y_train[i], len(self.x_train[i]), self.x_train[i]))

    @staticmethod
    def convert_ss_type_to_number(ss_type: str):
        if ss_type == "H":
            return 1
        if ss_type == "E":
            return 2
        if ss_type == "-" or ss_type == "C":
            return 3

