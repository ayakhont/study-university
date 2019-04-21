fileName = "sequence_data.py"
genetic_code =  {'GCU':'A','GCC':'A','GCA':'A', 'GCG':'A',
                'CGU':'R','CGC':'R','CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
                'AAU':'N','AAC':'N',
                'GAU':'D','GAC':'D',
                'UGU':'C','UGC':'C',
                'CAA':'Q','CAG':'Q',
                'GAA':'E','GAG':'E',
                'GGU':'G','GGC':'G','GGA':'G', 'GGG':'G',
                'CAU':'H','CAC':'H',
                'AUU':'I','AUC':'I', 'AUA':'I',
                'UUA':'L','UUG':'L','CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
                'AAA':'K','AAG':'K',
                'AUG':'M',
                'UUU':'F','UUC':'F',
                'CCU':'P','CCC':'P','CCA':'P','CCG':'P',
                'UCU':'S','UCC':'S','UCA':'S','UCG':'S','AGU':'S', 'AGC':'S',
                'ACU':'T','ACC':'T','ACA':'T','ACG':'T',
                'UGG':'W',
                'UAU':'Y', 'UAC':'Y',
                'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
                'UAG':'STOP', 'UGA':'STOP', 'UAA':'STOP' }


def dna2rna(DNA: str) -> list:
    RNA = list()
    for letter in DNA:
        if letter == 'T':
            RNA.append('U')
        else:
            RNA.append(letter)
    return RNA

def translate(RNA: str):
    amino = list()
    j = 0

    while j < len(RNA):
        codone = list()
        i = 0
        while len(codone) < 4:
            codone.append(RNA[i + j])
            i += 1
        codone_str = str(codone)
        amino.append(genetic_code[codone_str])
        j += i

    return amino


print(dna2rna("ATGAATGAATGATGAATGAGGGAAAATGAATGA"))
print(translate("AUGAAUGAAUGAUGAAUGAGGGAAAAUGAAUGA"))