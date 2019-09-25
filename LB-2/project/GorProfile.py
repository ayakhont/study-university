from SecondaryStructure import SecondaryStructure

class GorProfile:

    common_counter: SecondaryStructure
    residues_dict: dict

    def __init__(self):
        self.common_counter: SecondaryStructure()
        self.residues_dict = {
            "A": SecondaryStructure(), "C": SecondaryStructure(), "D": SecondaryStructure(),
            "E": SecondaryStructure(), "F": SecondaryStructure(), "G": SecondaryStructure(),
            "H": SecondaryStructure(), "I": SecondaryStructure(), "K": SecondaryStructure(),
            "L": SecondaryStructure(), "M": SecondaryStructure(), "N": SecondaryStructure(),
            "P": SecondaryStructure(), "Q": SecondaryStructure(), "R": SecondaryStructure(),
            "S": SecondaryStructure(), "T": SecondaryStructure(), "V": SecondaryStructure(),
            "W": SecondaryStructure(), "Y": SecondaryStructure()
        }

    def get_string(self):
        common_string = "Common counter for all residues: " + self.common_counter.get_string() + "\n"
        for key in self.residues_dict.keys():
             common_string += key + ": " + self.residues_dict[key].get_string() + "\n"
        return common_string

