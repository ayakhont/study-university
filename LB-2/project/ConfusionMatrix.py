from math import sqrt
from project.Prediction import Prediction


class ConfusionMatrix:
    true_positive: int
    false_positive: int
    false_negative: int
    true_negative: int
    negative_consistency: int
    ss_type: str  # "H" or "E" or "-"

    def __init__(self, ss_type: str):
        self.true_positive = 0
        self.false_positive = 0
        self.false_negative = 0
        self.true_negative = 0
        self.negative_consistency = 0
        self.ss_type = ss_type

    def increment_by_prediction(self, prediction: Prediction):
        for i in range(0, len(prediction.ss_checked)):
            if prediction.ss_predicted[i] == self.ss_type:
                if prediction.ss_predicted[i] == prediction.ss_checked[i]:
                    self.true_positive += 1
                else:
                    self.false_positive += 1
            else:
                if prediction.ss_checked == self.ss_type:
                    self.false_negative += 1
                else:
                    self.true_negative += 1
                    if prediction.ss_predicted[i] == prediction.ss_checked[i]:
                        self.negative_consistency += 1

    def get_sum(self) -> int:
        return self.true_positive + self.false_positive + self.false_negative + self.true_negative

    def calculate_mcc(self) -> float:
        return float(self.true_positive * self.true_negative - self.false_positive * self.false_negative) \
               / sqrt((self.true_positive + self.false_positive) * (self.true_positive + self.false_negative)
                      * (self.true_negative + self.false_positive) * (self.true_negative + self.false_negative))

    def calculate_accuracy(self) -> float:
        return float(self.true_positive + self.negative_consistency) / float(self.get_sum())
