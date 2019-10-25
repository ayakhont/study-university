import pickle
from typing import List

from project.ConfusionMatrix import ConfusionMatrix
from project.PathConstants import PathConstants
from project.Prediction import Prediction
from project.Svm import Svm


def calculate_sov(c_value: float, gamma_value: float):




def calculate_mcc_and_accuracy(c_value: float, gamma_value: float):
    mcc_h = 0.0
    mcc_e = 0.0
    mcc_c = 0.0
    accuracy = 0.0
    for i in range(0, 5):
        predictions_file = PathConstants.prediction_svm_template.format(i, c_value, gamma_value)
        predictions: List[Prediction]
        with open(predictions_file, 'rb') as file:
            predictions = pickle.load(file)
            confusion_matrix_h = ConfusionMatrix("H")
            confusion_matrix_e = ConfusionMatrix("E")
            confusion_matrix_c = ConfusionMatrix("-")
            for prediction in predictions:
                confusion_matrix_h.increment_by_prediction(prediction)
                confusion_matrix_e.increment_by_prediction(prediction)
                confusion_matrix_c.increment_by_prediction(prediction)
            mcc_h += confusion_matrix_h.calculate_mcc()
            mcc_e += confusion_matrix_e.calculate_mcc()
            mcc_c += confusion_matrix_c.calculate_mcc()
            accuracy += confusion_matrix_c.calculate_accuracy()

    print("For model with c={} and gamma={}:".format(c_value, gamma_value))
    print("H: MCC={}".format(mcc_h / 5))
    print("E: MCC={}".format(mcc_e / 5))
    print("C: MCC={}".format(mcc_c / 5))
    print("accuracy={}".format(accuracy / 5))


if __name__ == "__main__":
    for pair_of_parameters in Svm.c_gamma_parameters:
        calculate_mcc_and_accuracy(pair_of_parameters[0], pair_of_parameters[1])
