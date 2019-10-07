import os
from typing import List


class CrossValidation:
    training_seq_ids: list
    test_seq_ids: list

    def __init__(self, training_seq_ids, test_seq_ids):
        self.test_seq_ids = test_seq_ids
        self.training_seq_ids = training_seq_ids

    def get_training_seq_ids(self):
        return self.training_seq_ids

    def get_test_seq_ids(self):
        return self.test_seq_ids


class CrossValidationSet:

    cross_validation_set: List[CrossValidation]

    def __init__(self, cross_validation_dir):
        self.cross_validation_set = list()
        list_of_files = list()
        for filename in os.listdir(cross_validation_dir):
            list_of_files.append(cross_validation_dir + filename)
        for test_file in list_of_files:
            cross_validation = CrossValidation(list(), list())
            for training_file in list_of_files:
                if training_file != test_file:
                    with open(training_file, "r") as file:
                        for line in file:
                            cross_validation.training_seq_ids.append(line.rstrip())
            with open(test_file, "r") as file:
                for line in file:
                    cross_validation.test_seq_ids.append(line.rstrip())
            self.cross_validation_set.append(cross_validation)



