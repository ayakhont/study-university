import pickle
from typing import List

from project.ConfusionMatrix import ConfusionMatrix
from project.PathConstants import PathConstants
from project.Prediction import Prediction
from project.Sov import Sov
from project.Svm import Svm


def calculate_svm_evaluation(c_value: float, gamma_value: float):
    mcc_h = 0.0
    mcc_e = 0.0
    mcc_c = 0.0
    sov_h = 0.0
    sov_e = 0.0
    sov_c = 0.0
    accuracy = 0.0
    for i in range(0, 5):
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
            sov_h += sov_model_h.get_sov_index()
            sov_e += sov_model_e.get_sov_index()
            sov_c += sov_model_c.get_sov_index()
            accuracy += confusion_matrix_c.calculate_accuracy()

    print("For model with c={} and gamma={}:".format(c_value, gamma_value))
    print("H: MCC={}, SOV={}".format(mcc_h / 5, sov_h / 5))
    print("E: MCC={}, SOV={}".format(mcc_e / 5, sov_e / 5))
    print("C: MCC={}, SOV={}".format(mcc_c / 5, sov_c / 5))
    print("accuracy={}".format(accuracy / 5))


if __name__ == "__main__":
    for pair_of_parameters in Svm.c_gamma_parameters:
        calculate_svm_evaluation(pair_of_parameters[0], pair_of_parameters[1])
