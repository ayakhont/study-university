import pickle
from project.GorProfile import GorProfile
from project.PathConstants import PathConstants

if __name__ == "__main__":
    # below non-vector GOR
    # gor_profile = GorProfile()
    # gor_profile.train_model(PathConstants.training_fasta_dir, PathConstants.training_dssp_dir)
    # print(gor_profile.get_string())
    # gor_profile.normalize()
    # print(gor_profile.get_string())

    # below vector GOR
    # gor_profile = GorProfile(17)
    # gor_profile.train_model(PathConstants.training_fasta_dir, PathConstants.training_dssp_dir, 17)
    # print(gor_profile.get_string())
    # gor_profile.normalize()
    # with open(PathConstants.dump_file, 'wb') as file:
    #     pickle.dump(gor_profile, file)
    with open(PathConstants.dump_file, 'rb') as file:
        deserialized_profile = pickle.load(file)
    print(deserialized_profile.get_string())