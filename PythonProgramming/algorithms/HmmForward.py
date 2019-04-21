import numpy as np


class HmmForward:

    emissions: dict = None      # emission probabilities
    transitions: dict = None    # transition probabilities
    states: dict = None         # states map
    seq: str = None             # sequence 1 to be estimated

    def __init__(self, seq: str):
        self.emissions = {"Y": {"A": 0.1, "G": 0.4, "C": 0.4, "T": 0.1},
                          "N": {"A": 0.25, "G": 0.25, "C": 0.25, "T": 0.25}}
        self.transitions = {"BEGIN": {"Y": 0.2, "N": 0.8},
                            "Y": {"Y": 0.7, "N": 0.2, "END": 0.1},
                            "N": {"N": 0.8, "Y": 0.1, "END": 0.1}}
        self.states = {0: "BEGIN", 1: "Y", 2: "N", 3: "END"}
        self.seq = seq

    def model_estimation(self) -> float:
        model = self
        # the number of rows in matrix is the number of states
        m = len(model.states)
        # the number of columns in matrix is the length of sequence + 2 (for additional data)
        n = len(model.seq) + 2

        matrix = np.zeros((m, n), float)
        matrix[0][0] = 1.0
        for i in range(1, m-1):
            matrix[i][1] = model.transitions[model.states[0]][model.states[i]] \
                           * model.emissions[model.states[i]][model.seq[0]]
        result: float = 0.0

        for j in range(2, n-1):
            for i in range(1, m-1):
                for h in range(1, m-1):
                    matrix[i][j] += matrix[h][j-1]\
                                    * model.transitions[model.states[h]][model.states[i]]\
                                    * model.emissions[model.states[i]][model.seq[j-1]]

        for i in range (1, m-1):
            result += matrix[i][n-2] * model.transitions[model.states[i]][model.states[m-1]]

        matrix[m-1][n-1] = result
        print(matrix)

        return result


model = HmmForward("ATGCG")
print("Probability of sequence giving this model: ", model.model_estimation())



