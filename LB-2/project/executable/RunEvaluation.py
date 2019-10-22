import pickle
from typing import List

from project.ConfusionMatrix import ConfusionMatrix
from project.PathConstants import PathConstants
from project.Prediction import Prediction


def calculate_evaluation(i: int, c_value: float, gamma_value: float):
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
        print("For model {} with c={} and gamma={}:".format(i, c_value, gamma_value))
        print("H: MCC={}, accuracy={}".format(confusion_matrix_h.calculate_mcc(),
              confusion_matrix_h.calculate_accuracy()))
        print("E: MCC={}, accuracy={}".format(confusion_matrix_e.calculate_mcc(),
              confusion_matrix_e.calculate_accuracy()))
        print("C: MCC={}, accuracy={}".format(confusion_matrix_c.calculate_mcc(),
              confusion_matrix_c.calculate_accuracy()))


if __name__ == "__main__":
    calculate_evaluation(4, 4.0, 0.5)
