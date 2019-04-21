import numpy as np


class NW:

    match = 1
    mismatch = -1
    gap = -2
    scores: dict = None

    def __init__(self):
        self.scores = {'MATCH': self.match, 'MISMATCH': self.mismatch, 'GAP': self.gap}

    @staticmethod
    def diag(n1: str, n2: str, scores: dict) -> int:
        if n1 == n2:
            return scores['MATCH']
        else:
            return scores['MISMATCH']

    @staticmethod
    def pointer(diag: int, left: int, up: int) -> str:
        maxs = max(diag, left, up)

        if maxs == diag:
            return "D"
        elif maxs == left:
            return "L"
        else:
            return "U"

    # calculate traceback and score matrices
    def get_pass_s_m(self, seq1: str, seq2: str) -> (np.ndarray, np.ndarray):
        m = self
        row = len(seq1) + 1
        col = len(seq2) + 1
        # score matrix
        score_m = np.zeros((row, col), int)
        # matrix with directions
        pass_m = np.zeros((row, col), str)

        # init step
        for i in range(1, row):
            score_m[i][0] = i * m.scores['GAP']
            pass_m[i][0] = "U"
        for j in range(1, col):
            score_m[0][j] = j * m.scores['GAP']
            pass_m[0][j] = "L"
        pass_m[0][0] = 'S'

        # iteration step
        for j in range(1, col):
            for i in range(1, row):
                diag = score_m[i - 1][j - 1] + NW.diag(seq1[i - 1], seq2[j - 1], m.scores)
                up = score_m[i - 1][j] + m.scores['GAP']
                left = score_m[i][j - 1] + m.scores['GAP']
                score_m[i][j] = max(diag, left, up)
                pass_m[i][j] = NW.pointer(diag, left, up)

        return pass_m, score_m

    # traceback
    def get_alignment(self, seq1: str, seq2: str, pass_m: np.ndarray) -> (list, list):

        i = len(seq1)
        j = len(seq2)
        s1 = list()
        s2 = list()

        while pass_m[i][j] != 'S':
            if pass_m[i][j] == 'D':
                s1.append(seq1[i - 1])
                s2.append(seq2[j - 1])
                i -= 1
                j -= 1
            elif pass_m[i][j] == 'L':
                s2.append(seq2[j - 1])
                s1.append("-")
                j -= 1
            elif pass_m[i][j] == 'U':
                s1.append(seq1[i - 1])
                s2.append("-")
                i -= 1
        s1.reverse()
        s2.reverse()

        return s1, s2


seq1 = "TCCAGC"
seq2 = "TTTTTCGCAGGCGGGGG"
our_alignment = NW()
matrices = our_alignment.get_pass_s_m(seq1, seq2)
print(matrices[0])
print(matrices[1])
sequences = our_alignment.get_alignment(seq1, seq2, matrices[0])
print(sequences[0])
print(sequences[1])
