import os
import pickle
from typing import List

from thundersvm import SVC

from project.CrossValidationSet import CrossValidationSet, CrossValidation
from project.PathConstants import PathConstants
from project.Prediction import Prediction
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


def predict(c_value: float, gamma_value: float, cross_validation_set: CrossValidationSet):
    for i in range(0, 5):
        cross_validation = cross_validation_set.get_cross_validation_set()[i]
        svm = build_svm_instance(cross_validation, i, c_value, gamma_value, True)
        list_of_predictions = list()
        for test_id in cross_validation.get_test_seq_ids():
            y_train, x_train = Svm.parse_pssm_by_id(test_id)
            if len(x_train) == 0:
                continue
            svmProfile = SvmProfile(window_size)
            svmProfile.refill_by_seq_profile(y_train, x_train)
            if len(svmProfile.x_train) == 0:
                continue

            array = svm.model.predict(svmProfile.x_train)

            ss = ""
            for letter in array:
                ss += Utils.convert_number_to_ss_type(int(letter))
            prediction = Prediction(test_id, "".join(y_train), ss)
            list_of_predictions.append(prediction)
        predictions_file = PathConstants.prediction_svm_template.format(i, c_value, gamma_value)
        with open(predictions_file, 'wb') as file:
            pickle.dump(list_of_predictions, file)


def train_models(c_value, gamma_value, cross_validation_set):
    for i in range(0, 5):
        build_svm_instance(cross_validation_set.get_cross_validation_set()[i], i, c_value, gamma_value)


if __name__ == "__main__":
    cross_validation_set = CrossValidationSet(PathConstants.cross_validation_dir)
    #train_models(4.0, 2.0, cross_validation_set)
    #train_models(4.0, 0.5, cross_validation_set)
    #test_prediction()
    predict(4.0, 2.0, cross_validation_set)


