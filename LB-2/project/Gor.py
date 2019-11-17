from project.GorProfile import GorProfile
from project.Utils import Utils


class Gor:

    gor_profile: GorProfile

    def __init__(self, gor_profile: GorProfile):
        self.gor_profile = gor_profile

    def train_model(self, training_fasta_dir: str, training_dssp_dir: str, ids: list):
        self.gor_profile.fill_in_profile(training_fasta_dir, training_dssp_dir, ids)
        self.gor_profile.normalize()

    def get_string_profile(self):
        return self.gor_profile.get_string()

    def predict_secondary_structure_for_seq(self, sequence: str):
        ss_string = ""
        for i in range(0, len(sequence)):
            score_map = {"E": 0.0, "H": 0.0, "-": 0.0}
            vector_counter = -1
            for j in range(i - self.gor_profile.window_size // 2,
                           i + 1 + self.gor_profile.window_size // 2):
                vector_counter += 1
                if j < 0 or j >= len(sequence):
                    continue
                residue = sequence[j]
                if residue == "X" or residue == "\n":
                    continue
                for ss_type in score_map.keys():
                    score_map[ss_type] += self.gor_profile.calculate_score(residue, ss_type,
                                                                           vector_counter)
            ss = max(score_map.keys(), key=(lambda key: score_map[key]))
            ss_string += ss

        return ss_string

    def predict_secondary_structure_by_id(self, seq_id: str, fasta_dir_path: str) -> (str, str):
        fasta_file_path = fasta_dir_path + seq_id + ".fasta"
        sequence = Utils.get_seq_from_fasta_file(fasta_file_path)
        ss_predicted = self.predict_secondary_structure_for_seq(sequence)

        return ss_predicted









