from project.GorProfile import GorProfile


class Gor:

    gor_profile: GorProfile

    def __init__(self, gor_profile: GorProfile):
        self.gor_profile = gor_profile

    def train_model(self, training_fasta_dir: str, training_dssp_dir: str, window_size=1):
        self.gor_profile.fill_in_profile(training_fasta_dir, training_dssp_dir, window_size)
        self.gor_profile.normalize()

    def get_string_profile(self):
        return self.gor_profile.get_string()



