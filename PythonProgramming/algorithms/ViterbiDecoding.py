import numpy as np


class Viterbi:

    emissions: dict = None
    transitions: dict = None
    states: dict = None

    def __init__(self):
        self.emissions = {"Y": {"A": 0.1, "G": 0.4, "C": 0.4, "T": 0.1},
                          "N": {"A": 0.25, "G": 0.25, "C": 0.25, "T": 0.25}}
        self.transitions = {"BEGIN": {"Y": 0.2, "N": 0.8},
                            "Y": {"Y": 0.7, "N": 0.2, "END": 0.1},
                            "N": {"N": 0.8, "Y": 0.1, "END": 0.1}}
        self.states = {0: "BEGIN", 1: "Y", 2: "N", 3: "END"}

    @staticmethod
    def find_max(probs: list, states: list) -> (float, str):
        tup = list(zip(probs, states))
        smax = max(tup)
        return smax

    def viterbi_impl(self, seq: str) -> (float, list):
        # object of our model
        m = self

        row = len(m.states)
        col = len(seq) + 1

        matrix = np.zeros((row, col), float)
        pass_matrix = np.zeros((row, col), str)

        for i in range(1, row-1):
            matrix[i][0] = m.transitions["BEGIN"][m.states[i]] * m.emissions[m.states[i]][seq[0]]
            pass_matrix[i][0] = "BEGIN"

        # iterative state
        for j in range(1, col-1):
            for i in range(1, row-1):
                probs = list()
                pointers = list()
                for h in range(1, row-1):
                    probs.append(matrix[h][j-1] * m.transitions[m.states[h]][m.states[i]] * m.emissions[m.states[i]][seq[j]])
                    pointers.append(m.states[h])
                matrix[i][j], pass_matrix[i][j] = Viterbi.find_max(probs, pointers)

        # termination state
        probs = list()
        pointers = list()
        for h in range(1, row - 1):
            probs.append(matrix[h][col-2] * m.transitions[m.states[h]]["END"])
            pointers.append(m.states[h])
        matrix[row-1][col-1], pass_matrix[row-1][col-1] = Viterbi.find_max(probs, pointers)

        print(matrix)
        print(pass_matrix)

        # traceback
        r_states = {"B": 0, "Y": 1, "N": 2, "E": 3}
        pointer_i = r_states[pass_matrix[row-1][col-1]]
        path = list()
        path.append("END")
        path.append(pass_matrix[row-1][col-1])
        for j in range(col - 2, -1, -1):
            path.append(pass_matrix[pointer_i][j])
            pointer_i = r_states[pass_matrix[pointer_i][j]]

        path.reverse()

        return matrix[row-1][col-1], path


model = Viterbi()
common_prob, path = model.viterbi_impl("ATGCG")
print("Probability of the sequence is ", common_prob)
print("Path of the sequence: ", path)





