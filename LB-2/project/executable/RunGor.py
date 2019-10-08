import os
import pickle

from project.Gor import Gor
from project.GorProfile import GorProfile
from project.PathConstants import PathConstants

if __name__ == "__main__":
    gor_model: Gor
    # if dumped gor profile exists it means that we need only deserialized it
    # (model has already been trained)
    # else create a new one and train the model
    if os.path.isfile(PathConstants.dump_file):
        with open(PathConstants.dump_file, 'rb') as file:
            profile = pickle.load(file)
            gor_model = Gor(profile)
    else:
        gor_profile = GorProfile(17)
        gor_model = Gor(gor_profile)
        gor_model.train_model(PathConstants.training_fasta_dir, PathConstants.training_dssp_dir)
        with open(PathConstants.dump_file, 'wb') as file:
            pickle.dump(gor_profile, file)

    print(gor_model.get_string_profile())
    print(gor_model.predict_secondary_structure_for_seq("NLTLTHFKGPLYIVEDKEYVQENSMVYIGTDGITIIGATWTPETAETLYKEIRKVSPLPINEVINTNYHTDRAGGNAYWKTLGAKIVATQMTYDLQKSQWGSIVNFTRQGNNKYPNLEKSLPDTVFPGDFNLQNGSIRAMYLGEAHTKDGIFVYFPAERVLYGNCILKENLGNMSFANRTEYPKTLEKLKGLIEQGELKVDSIIAGHDTPIHDVGLIDHYLTLLEKAP"))


