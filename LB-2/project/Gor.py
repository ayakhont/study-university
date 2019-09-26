from GorProfile import GorProfile
from PathConstants import PathConstants

if __name__ == "__main__":
    # gor_profile = GorProfile()
    # gor_profile.fill_in_profile(PathConstants.training_fasta_dir, PathConstants.training_dssp_dir)
    # print(gor_profile.get_string())
    # gor_profile.normalize()
    # print(gor_profile.get_string())
    gor_profile = GorProfile(5)
    print(gor_profile.get_string())
