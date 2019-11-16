import os
import pickle

from project.CrossValidationSet import CrossValidationSet
from project.Gor import Gor
from project.GorProfile import GorProfile
from project.PathConstants import PathConstants
from project.Prediction import Prediction

test_seq = "NLTLTHFKGPLYIVEDKEYVQENSMVYIGTDGITIIGATWTPETAETLYKEIRKVSPLPINEVINTNYHTDRAGGNAYWKTLGAKIVATQMT" \
           "YDLQKSQWGSIVNFTRQGNNKYPNLEKSLPDTVFPGDFNLQNGSIRAMYLGEAHTKDGIFVYFPAERVLYGNCILKENLGNMSFANRTEYPK" \
           "TLEKLKGLIEQGELKVDSIIAGHDTPIHDVGLIDHYLTLLEKAP"


def train_models(cross_validation_set: CrossValidationSet):
    for i in range(0, 5):
        gor_profile = GorProfile(17)
        gor_model = Gor(gor_profile)
        cross_validation = cross_validation_set.get_cross_validation_set()[i]
        gor_model.train_model(PathConstants.training_fasta_dir, PathConstants.training_dssp_dir,
                              cross_validation.get_training_seq_ids())
        dump_gor_profile = PathConstants.dump_gor_profile_template.format(i)
        with open(dump_gor_profile, 'wb') as file:
            pickle.dump(gor_profile, file)


def test_prediction(sequence: str):
    # if dumped gor profile exists it means that we need only deserialized it
    # (model has already been trained)
    if os.path.isfile(PathConstants.dump_gor_profile_template.format(0)):
        with open(PathConstants.dump_gor_profile_template.format(0), 'rb') as file:
            profile = pickle.load(file)
            gor_model = Gor(profile)
            print(gor_model.get_string_profile())
            print(gor_model.predict_secondary_structure_for_seq(sequence))
    else:
        raise Exception("Gor profile is not found!")

def predict(cross_validation_set: CrossValidationSet):
    for i in range(0, 5):
        cross_validation = cross_validation_set.get_cross_validation_set()[i]
        with open(PathConstants.dump_gor_profile_template.format(i), 'rb') as file:
            profile = pickle.load(file)
            gor_model = Gor(profile)
            list_of_predictions = list()
            for test_id in cross_validation.get_test_seq_ids():
                prediction = Prediction(test_id, )


if __name__ == "__main__":
    cross_validation_set = CrossValidationSet(PathConstants.cross_validation_dir)
    # train_models(cross_validation_set)
    # test_prediction(test_seq)
    predict(cross_validation_set)


