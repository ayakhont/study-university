import numpy as np


def parse_alignment(m_file: str) -> dict:
    d = dict()
    with open(m_file, "r") as file:
        for line in file:
            line = line.rstrip()
            line.split()
            d.update({line[0]: line[1]})
        return d


def get_profile(d_aln: dict, pos: int) -> np.ndarray:
    residues = 'ATCG'
    profile = np.zeros(4)
    keys = d_aln.keys()
    for k in keys:
        res = d_aln[k][pos]
        i = residues.find(res)
        if i > 0:
            profile[i] = profile[i] + 1
    return profile/float(np.sum(profile))


def get_entropy(prof) -> float:
    s = 0.0
    for i in range(len(prof)):
        if prof[i] > 0:
            s = s - prof[i] * np.log(prof[i])
    return s


if __name__ == "__main__":
    l1 = ['-', '-', '-', '-', 'T', 'C', '-', 'C', 'A', '-', 'G', 'C', '-', '-', '-', '-', '-']
    l2 = ['T', 'T', 'T', 'T', 'T', 'A', 'G', 'C', 'A', 'G', 'G', 'C', 'G', 'G', 'G', 'G', 'G']
    l3 = ['-', 'T', 'T', 'T', 'T', 'C', 'G', 'C', 'A', 'G', 'G', 'C', 'G', 'G', 'C', 'G', 'G']
    our_dict = {">s1": l1, ">s2": l2, ">s3": l3}

    for i in range(len(l1)):
        prof = get_profile(our_dict, i)
        print(prof)
        print(get_entropy(prof))





