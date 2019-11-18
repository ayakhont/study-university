import pickle
from typing import List

from project.ConfusionMatrix import ConfusionMatrix
from project.PathConstants import PathConstants
from project.Prediction import Prediction
from project.Sov import Sov
from project.Utils import Utils

c_gamma_parameters = [[4.0, 2.0],
                      [4.0, 0.5],
                      [2.0, 2.0],
                      [2.0, 0.5]]


def calculate_evaluation(is_gor_evaluation: bool, is_blind: bool, c_value=None, gamma_value=None):
    mcc_h = 0.0
    mcc_e = 0.0
    mcc_c = 0.0
    sov_h = list()
    sov_e = list()
    sov_c = list()
    accuracy = 0.0
    for i in range(0, 5):
        if is_gor_evaluation:
            if is_blind:
                predictions_file = PathConstants.prediction_gor_template_blind.format(i)
            else:
                predictions_file = PathConstants.prediction_gor_template.format(i)
        else:
            predictions_file = PathConstants.prediction_svm_template.format(i, c_value, gamma_value)
        predictions: List[Prediction]
        with open(predictions_file, 'rb') as file:
            predictions = pickle.load(file)
            confusion_matrix_h = ConfusionMatrix("H")
            confusion_matrix_e = ConfusionMatrix("E")
            confusion_matrix_c = ConfusionMatrix("-")

            sov_model_h = Sov("H")
            sov_model_e = Sov("E")
            sov_model_c = Sov("-")
            prediction_for_sov = Prediction()

            for prediction in predictions:
                if len(prediction.ss_checked) != len(prediction.ss_predicted):
                    print("Length of verified and predicted are not equal for id: {}"
                          .format(prediction.id))
                    continue
                confusion_matrix_h.increment_by_prediction(prediction)
                confusion_matrix_e.increment_by_prediction(prediction)
                confusion_matrix_c.increment_by_prediction(prediction)
                prediction_for_sov.increment(prediction.ss_checked, prediction.ss_predicted)

            sov_model_h.fill_in(prediction_for_sov)
            sov_model_e.fill_in(prediction_for_sov)
            sov_model_c.fill_in(prediction_for_sov)
            mcc_h += confusion_matrix_h.calculate_mcc()
            mcc_e += confusion_matrix_e.calculate_mcc()
            mcc_c += confusion_matrix_c.calculate_mcc()
            sov_h.append(sov_model_h.get_sov_index())
            sov_e.append(sov_model_e.get_sov_index())
            sov_c.append(sov_model_c.get_sov_index())
            accuracy += confusion_matrix_c.calculate_accuracy()

    if is_gor_evaluation:
        if is_blind:
            print("Gor blind evaluation:")
        else:
            print("Gor cross validation evaluation:")
    else:
        print("For model with c={} and gamma={}:".format(c_value, gamma_value))
    print("H: MCC={}, SOV={}, SD of SOV index = {}".format(mcc_h / 5, sum(sov_h) / 5, Utils.calculate_sd(sov_h)))
    print("E: MCC={}, SOV={}, SD of SOV index = {}".format(mcc_e / 5, sum(sov_e) / 5, Utils.calculate_sd(sov_e)))
    print("C: MCC={}, SOV={}, SD of SOV index = {}".format(mcc_c / 5, sum(sov_c) / 5, Utils.calculate_sd(sov_c)))
    print("accuracy={}".format(accuracy / 5))


if __name__ == "__main__":
    # for pair_of_parameters in c_gamma_parameters:
    #     calculate_evaluation(False, pair_of_parameters[0], pair_of_parameters[1])
    calculate_evaluation(True, False)
    calculate_evaluation(True, True)
