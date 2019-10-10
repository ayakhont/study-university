import os
import pickle
from project.CrossValidationSet import CrossValidationSet, CrossValidation
from project.PathConstants import PathConstants
from project.Svm import Svm


def build_svm_instance(crossValidation: CrossValidation, number_of_model: int,
                       c_value: float, gamma_value: float) -> Svm:
    dump_profile = PathConstants.dump_svm_profile_template.format(number_of_model)
    dump_model = PathConstants.dump_svm_model_template.format(number_of_model, c_value, gamma_value)
    if os.path.isfile(dump_profile):
        with open(dump_profile, 'rb') as file:
            profile = pickle.load(file)

            if os.path.isfile(dump_model):
                with open(dump_model, 'rb') as file:
                    model = pickle.load(file)
                    svm = Svm(17, crossValidation, c_value, gamma_value, svm_profile=profile, model=model)
            else:
                svm = Svm(17, crossValidation, c_value, gamma_value, svm_profile=profile)
                with open(dump_model, 'wb') as file:
                    pickle.dump(svm.model, file)
    else:
        if os.path.isfile(dump_model):
            with open(dump_model, 'rb') as file:
                model = pickle.load(file)
                svm = Svm(17, crossValidation, c_value, gamma_value, model=model)
            with open(dump_profile, 'wb') as file:
                pickle.dump(svm.svmProfile, file)
        else:
            svm = Svm(17, crossValidation, c_value, gamma_value)
            with open(dump_profile, 'wb') as file:
                pickle.dump(svm.svmProfile, file)
            with open(dump_model, 'wb') as file:
                pickle.dump(svm.model, file)

    return svm


if __name__ == "__main__":
    cross_validation_set = CrossValidationSet(PathConstants.cross_validation_dir)
    number_of_model = 0
    c_value = 2.0
    gamma_value = 2.0

    svm = build_svm_instance(cross_validation_set.get_cross_validation_set()[number_of_model],
                             number_of_model, c_value, gamma_value)