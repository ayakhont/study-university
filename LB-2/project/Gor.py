from GorProfile import GorProfile
from PathConstants import PathConstants

if __name__ == "__main__":
    # gor_profile = GorProfile()
    # gor_profile.train_model(PathConstants.training_fasta_dir, PathConstants.training_dssp_dir)
    # print(gor_profile.get_string())
    # gor_profile.normalize()
    # print(gor_profile.get_string())
    # gor_profile = GorProfile(5)
    # print(gor_profile.get_string())
    for i in range(0, 10):
        print("i = ", i)
        for j in range(i - i // 3, i + 1 + i // 3):
            print(j)
