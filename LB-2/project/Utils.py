class Utils:

    # build a map of seq Id ant it's sequence in one string
    @staticmethod
    def get_map_from_fasta_file(fasta_file) -> dict:
        map = dict()
        with open(fasta_file, "r") as f:
            lines = f.readlines()
            current_seq = ""
            for i in range(0, len(lines)):
                line = lines[i]
                if line[0] == ">":
                    map[line[1:7]] = ""
                    current_seq = line[1:7]
                else:
                    current = line.rstrip()
                    seq = map[current_seq] + current
                    map[current_seq] = seq
        return map

    @staticmethod
    # H, G, I -> H
    # B, E -> E
    # T, S, “” -> C
    def get_ss_from_dssp_line(splitted_line: list) -> str:
        if splitted_line[4] == "H" or splitted_line[4] == "G" or splitted_line[4] == "I":
            return "H"
        elif splitted_line[4] == "B" or splitted_line[4] == "E":
            return "E"
        else:
            return "C"
