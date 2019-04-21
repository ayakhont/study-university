Norm_Acc={"A" :106.0,  "B" :160.0, "C" :135.0,  "D" :163.0,  "E" :194.0,"F" :197.0,  "G" : 84.0,  "H" :184.0,"I" :169.0,
          "K" :205.0,  "L" :164.0,"M" :188.0,  "N" :157.0,  "P" :136.0,"Q" :198.0,  "R" :248.0,  "S" :130.0,"T" :142.0,
          "V" :142.0,  "W" :227.0,"X" :180.0,  "Y" :222.0,  "Z" :196.0}


def parse_dssp(dsspfile: str, chain: str):
    dssp = list()
    with open(dsspfile, "r") as file:
        current = False
        for line in file:

            if line.find("#  RESIDUE") == 2:
                current = True
                continue

            if current == True:
                if line[11] == '!':
                    continue
                if line[11] == chain:
                    r = line[13].capitalize()
                    ss = line[16]
                    if ss == ' ':
                        ss = "C"
                    acc = float(line[35:38])
                    phi = float(line[103:109])
                    psi = float(line[109:115])

                    racc = acc/Norm_Acc[r]
                    v = [r, racc, phi, psi]
                    dssp.append(v)

    return dssp


if __name__ == "__main__":
    dssp = parse_dssp("1brl.B.dssp", 'B')
    for element in dssp:
        print(element)
