import numpy as np


class SWAlignment:

    match: int = None
    mismatch: int = None
    gap: int = None
    seq1: str = None
    seq2: str = None
    scores: dict = None
    UP: str = "U"
    LEFT: str = "L"
    DIAG: str = "D"
    STOP: str = "S"
    imax: int = 0
    jmax: int = 0

    def __init__(self, seq1: str, seq2: str):
        self.match = 2
        self.mismatch = -1
        self.gap = -2
        self.seq1 = seq1
        self.seq2 = seq2
        self.scores = {"MATCH": self.match, "MISMATCH": self.mismatch, "GAP": self.gap}

    @staticmethod
    def diagonal(n1: str, n2: str, scores: dict) -> int:
        if n1 == n2:
            return scores["MATCH"]
        else:
            return scores["MISMATCH"]

    def pointer(self, diag: int, left: int, up: int) -> str:
        pointer = max(diag, left, up, 0)

        if pointer == diag:
            return self.DIAG
        elif pointer == left:
            return self.LEFT
        elif pointer == up:
            return self.UP
        else:
            return self.STOP

    def get_pass_matrix(self) -> np.ndarray:
        m = self
        row = len(m.seq1) + 1
        col = len(m.seq2) + 1
        score = 0

        score_matrix = np.zeros((row, col), int)
        pass_matrix = np.zeros((row, col), str)

        for i in range(1, row):
            pass_matrix[i][0] = m.UP
        for j in range(1, col):
            pass_matrix[0][j] = m.LEFT
        pass_matrix[0][0] = m.STOP

        for i in range(1, row):
            for j in range(1, col):
                diag = score_matrix[i-1][j-1] + SWAlignment.diagonal(m.seq1[i-1], m.seq2[j-1], m.scores)
                left = score_matrix[i][j-1] + m.scores["GAP"]
                up = score_matrix[i-1][j] + m.scores["GAP"]
                score_matrix[i][j] = max(diag, left, up, 0)
                pass_matrix[i][j] = SWAlignment.pointer(m, diag, left, up)

                if score_matrix[i][j] >= score:
                    score = score_matrix[i][j]
                    m.imax = i
                    m.jmax = j


        print(score_matrix)

        return pass_matrix

    def pack_pass(self, pass_matrix: np.ndarray) -> (list, list):
        m = self
        i = m.imax
        j = m.jmax

        seq1 = list()
        seq2 = list()

        while pass_matrix[i][j] != m.STOP:
            if pass_matrix[i][j] == m.DIAG:
                seq1.append(m.seq1[i-1])
                seq2.append(m.seq2[j-1])
                i -= 1
                j -= 1
            if pass_matrix[i][j] == m.UP:
                seq1.append(m.seq1[i-1])
                seq2.append('-')
                i -= 1
            if pass_matrix[i][j] == m.LEFT:
                seq1.append('-')
                seq2.append(m.seq2[j-1])
                j -= 1

        seq1.reverse()
        seq2.reverse()

        return seq1, seq2



alignment = SWAlignment("TTTTTCGCTTAGGCGGGGG", "TCCAGCCCC")
pass_matrix = alignment.get_pass_matrix()
print(pass_matrix)
sequences = alignment.pack_pass(pass_matrix)
print(sequences[0])
print(sequences[1])


