import os
import pickle
from thundersvm import SVC

from project.CrossValidationSet import CrossValidationSet, CrossValidation
from project.PathConstants import PathConstants
from project.Svm import Svm
from project.SvmProfile import SvmProfile
from project.Utils import Utils

window_size = 17


def build_svm_instance(crossValidation: CrossValidation, number_of_model: int,
                       c_value: float, gamma_value: float, is_for_prediction=False):
    dump_profile = PathConstants.dump_svm_profile_template.format(number_of_model)
    dump_model = PathConstants.dump_svm_model_template.format(number_of_model, c_value, gamma_value)
    if os.path.isfile(dump_profile):
        with open(dump_profile, 'rb') as file:
            if is_for_prediction:
                profile = SvmProfile(window_size)
            else:
                profile = pickle.load(file)

            if os.path.isfile(dump_model):
                svc = SVC(C=c_value, kernel="rbf", gamma=gamma_value)
                svc.load_from_file(dump_model)
                svm = Svm(window_size, crossValidation, c_value, gamma_value, svm_profile=profile, model=svc)
            else:
                svm = Svm(window_size, crossValidation, c_value, gamma_value, svm_profile=profile)
                svm.model.save_to_file(dump_model)
    else:
        if os.path.isfile(dump_model):
            svc = SVC(C=c_value, kernel="rbf", gamma=gamma_value)
            model = svc.load_from_file(dump_model)
            svm = Svm(window_size, crossValidation, c_value, gamma_value, model=model)
            with open(dump_profile, 'wb') as file:
                pickle.dump(svm.svmProfile, file)
        else:
            svm = Svm(window_size, crossValidation, c_value, gamma_value)
            svm.model.save_to_file(dump_model)
            with open(dump_profile, 'wb') as file:
                pickle.dump(svm.svmProfile, file)

    return svm


def test_prediction():
    cross_validation_set = CrossValidationSet(PathConstants.cross_validation_dir)
    c_value = 2.0
    gamma_value = 0.5
    svm = build_svm_instance(cross_validation_set.get_cross_validation_set()[0], 0,
                           c_value, gamma_value, True)
    svmProfile = SvmProfile(window_size)
    y_train, x_train = Svm.parse_pssm_by_id("d1a9xa1")
    svmProfile.refill_by_seq_profile(y_train, x_train)
    array = svm.model.predict(svmProfile.x_train)
    ss = ""
    for letter in array:
        ss += Utils.convert_number_to_ss_type(int(letter))
    print(ss)


def train_models(c_value, gamma_value):
    cross_validation_set = CrossValidationSet(PathConstants.cross_validation_dir)
    for i in range(0, 5):
        build_svm_instance(cross_validation_set.get_cross_validation_set()[i], i, c_value, gamma_value)

if __name__ == "__main__":
    #train_models(2.0, 0.5)
    test_prediction()


