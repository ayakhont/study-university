from typing import List

from project.Prediction import Prediction


class Sov:
    intersections: List[list]       # contains lists of intersections with indexes of segments
                                    # in view of [index of observed list, index of predicted list]
    observed: List[list]            # list of segments observed. Example: [[0, 1, 2][7,8,9]]
    predicted: List[list]           # list of segments predicted. Example: [[2, 3, 4][9, 10, 11, 12]]
    ss_type: str                    # "H" or "E" or "-"

    def __init__(self, ss_type):
        self.intersections = list()
        self.observed = list()
        self.predicted = list()
        self.ss_type = ss_type

    def fill_in(self, prediction: Prediction):
        observed_str = prediction.ss_checked
        predicted_str = prediction.ss_predicted
        is_continued_observed = False
        is_continued_predicted = False
        temp_observed_list = list()
        temp_predicted_list = list()
        index_of_last_observed_segment = 0
        index_of_last_predicted_segment = 0
        for i in range(0, len(observed_str)):
            if observed_str[i] == self.ss_type:
                temp_observed_list.append(i)
                is_continued_observed = True
            else:
                if is_continued_observed:
                    self.observed.append(temp_observed_list)
                    temp_observed_list = list()
                    is_continued_observed = False
                    index_of_last_observed_segment += 1

            if predicted_str[i] == self.ss_type:
                temp_predicted_list.append(i)
                is_continued_predicted = True
            else:
                if is_continued_predicted:
                    self.predicted.append(temp_predicted_list)
                    temp_predicted_list = list()
                    is_continued_predicted = False
                    index_of_last_predicted_segment += 1

            if observed_str[i] == self.ss_type and predicted_str[i] == self.ss_type:
                if [index_of_last_observed_segment, index_of_last_predicted_segment] not in self.intersections:
                    self.intersections.append([index_of_last_observed_segment, index_of_last_predicted_segment])

        if temp_observed_list:
            self.observed.append(temp_observed_list)
        if temp_predicted_list:
            self.predicted.append(temp_predicted_list)

    def get_len_of_all_observed(self):
        n = 0
        for segment in self.observed:
            n += len(segment)
        return n

    def get_sov_index(self) -> float:
        summation = 0
        for indexes_set in self.intersections:
            minov = Sov.minov(self.observed[indexes_set[0]], self.predicted[indexes_set[1]])
            maxov = Sov.maxov(self.observed[indexes_set[0]], self.predicted[indexes_set[1]])
            delta = Sov.delta(self.observed[indexes_set[0]], self.predicted[indexes_set[1]])
            summation += (minov + delta)/maxov * len(self.observed[indexes_set[0]])
        return 100 / self.get_len_of_all_observed() * summation

    @staticmethod
    def minov(segment1, segment2) -> int:
        return len(set(segment1).intersection(segment2))

    @staticmethod
    def maxov(segment1, segment2) -> int:
        return len(segment1) + len(segment2) - Sov.minov(segment1, segment2)

    @staticmethod
    def delta(segment1, segment2) -> float:
        return min(float(Sov.maxov(segment1, segment2) - Sov.minov(segment1, segment2)),
                   float(Sov.minov(segment1, segment2)),
                   len(segment1)/2,
                   len(segment2)/2)

    @staticmethod
    def test():
        sov = Sov("H")
        prediction = Prediction("dsad1", "CCCHHHHHCCCCCCCCHHHHHHHHHHCCC", "CCCCCCCCCCCHHHHHHHCCCCCHHHHCC")
        sov.fill_in(prediction)
        print(sov.observed)
        print(sov.predicted)
        print(sov.intersections)
        for indexes_set in sov.intersections:
            print("minov = ", Sov.minov(sov.observed[indexes_set[0]], sov.predicted[indexes_set[1]]))
            print("maxov = ", Sov.maxov(sov.observed[indexes_set[0]], sov.predicted[indexes_set[1]]))
            print("delta = ", Sov.delta(sov.observed[indexes_set[0]], sov.predicted[indexes_set[1]]))
        print(sov.get_len_of_all_observed())
        print(sov.get_sov_index())