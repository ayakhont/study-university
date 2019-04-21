from typing import Dict

import numpy as np


class NWAlignment:

    match: int = None       # score for matching element
    mismatch: int = None    # score for mismatch element
    gap: int = None         # score for gap element
    seq1: str = None        # sequence 1 to be aligned
    seq2: str = None        # sequence 2 to be aligned
    scores: Dict[str, int] = None   # dictionary for scores

    def __init__(self, m: int, s: int, d: int, seq1: str, seq2: str):
        self.match = m
        self.mismatch = s
        self.gap = d
        self.seq1 = seq1
        self.seq2 = seq2
        self.scores = {'MATCH': self.match, 'MISMATCH': self.mismatch, 'GAP': self.gap}

    @staticmethod
    def diagonal(n1: str, n2: str, score: dict) -> int:
        if n1 == n2:
            return score['MATCH']
        else:
            return score['MISMATCH']

    @staticmethod
    def pointer(diag: int, left: int, up: int) -> str:
        pointer = max(diag, left, up)

        if pointer == diag:
            return "D"
        elif pointer == left:
            return "L"
        else:
            return "U"

    def get_alignment_matrices(self) -> np.ndarray:
        alignment = self
        # dimension for number of columns
        n = len(alignment.seq1) + 1
        # dimension for number of rows
        m = len(alignment.seq2) + 1

        # initialize score matrix for alignment
        score_matrix = np.zeros((m, n), int)
        # initialize pass matrix for alignment
        pass_matrix = np.zeros((m, n), str)

        # initialize first row for alignment matrices
        for j in range(n):
            score_matrix[0][j] = j * alignment.scores['GAP']
            # score_matrix[0][j] = 0 # without end gaps
            pass_matrix[0][j] = "L"

        # initialize first column for alignment matrices
        for i in range(m):
            score_matrix[i][0] = i * alignment.scores['GAP']
            # score_matrix[i][0] = 0 # without end gaps
            pass_matrix[i][0] = "U"
        # restore justice
        pass_matrix[0][0] = '0'

        # let's play
        for i in range(1, m):
            for j in range(1, n):
                diag = score_matrix[i - 1][j - 1] + NWAlignment.diagonal(
                    alignment.seq1[j - 1], alignment.seq2[i - 1], alignment.scores)
                up = score_matrix[i - 1][j] + alignment.scores['GAP']  # vertical from the upper cell
                left = score_matrix[i][j - 1] + alignment.scores['GAP']  # horizontal from the left cell
                score_matrix[i][j] = max(diag, left, up)
                pass_matrix[i][j] = NWAlignment.pointer(diag, left, up)

        print(np.matrix(score_matrix))

        return pass_matrix

    # traceback
    def get_alignment(self, pass_matrix: np.ndarray) -> (list, list):
        alignment = self
        # dimension for number of columns
        jmax = len(alignment.seq1)
        # dimension for number of rows
        imax = len(alignment.seq2)

        align_seq1 = list()
        align_seq2 = list()

        while pass_matrix[imax][jmax] != '0':
            if pass_matrix[imax][jmax] == 'D':
                align_seq1.append(alignment.seq1[jmax - 1])
                align_seq2.append(alignment.seq2[imax - 1])
                jmax -= 1
                imax -= 1
            elif pass_matrix[imax][jmax] == 'L':
                align_seq1.append(alignment.seq1[jmax - 1])
                align_seq2.append("-")
                jmax -= 1
            elif pass_matrix[imax][jmax] == 'U':
                align_seq2.append(alignment.seq2[imax - 1])
                align_seq1.append("-")
                imax -= 1

        return align_seq1, align_seq2


# m = int(input("Please input score when one element match another: "))
# s = int(input("Please input score when one element mismatch another: "))
# d = int(input("Please specify penalty for gap: "))
if __name__ == "__main__":

    our_alignment = NWAlignment(1, -1, -2, "TTTTTCGCAGGCGGGGG", "TCCAGC")
    align_matrix = our_alignment.get_alignment_matrices()
    print(np.matrix(align_matrix))

    alignments = our_alignment.get_alignment(align_matrix)
    alignments[0].reverse()
    alignments[1].reverse()
    print(alignments[0])
    print(alignments[1])
