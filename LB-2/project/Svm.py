#from thundersvm import SVC
from sklearn import svm
from sklearn.svm import SVC

from project.CrossValidationSet import CrossValidation
from project.PathConstants import PathConstants
from project.SvmProfile import SvmProfile
import os.path


class Svm:

    window_size: int
    crossValidation: CrossValidation
    svmProfile: SvmProfile
    c_value: float
    gamma_value: float
    model: SVC

    def __init__(self, window_size: int, crossValidation: CrossValidation, c_value: float,
                 gamma_value: float, svm_profile=None, model=None):
        self.window_size = window_size
        self.crossValidation = crossValidation
        self.c_value = c_value
        self.gamma_value = gamma_value
        if svm_profile == None:
            self.svmProfile = self.fill_in_svm_profile()
        else:
            self.svmProfile = svm_profile
        if model == None:
            self.train_model()
        else:
            self.model = model

    def fill_in_svm_profile(self):
        svmProfile = SvmProfile(self.window_size)
        for id in self.crossValidation.get_training_seq_ids():
            y_train, x_train = Svm.parse_pssm_by_id(id)
            svmProfile.refill_by_seq_profile(y_train, x_train)
        return svmProfile

    @staticmethod
    def parse_pssm_by_id(id: str) -> (list, list):
        dssp_line = ""
        with open(PathConstants.training_dssp_dir + id + ".dssp", "r") as dssp_file:
            for dssp_line_in_file in dssp_file:
                if dssp_line_in_file[0] != '>':
                    dssp_line = dssp_line_in_file.rstrip()
        pssm_list = list()

        if os.path.isfile(PathConstants.profiling_pssm + id + ".pssm"):
            with open(PathConstants.profiling_pssm + id + ".pssm", "r") as pssm_file:
                is_start = False
                for line in pssm_file:
                    splitted_line = line.split()
                    if splitted_line and splitted_line[0] == "1":
                        is_start = True
                    if is_start and not splitted_line:
                        break
                    if is_start:
                        sub_list = list()
                        for i in range(22, 42):
                            sub_list.append(float(splitted_line[i]) / 100)
                        pssm_list.append(sub_list)

            if len(dssp_line) != len(pssm_list):
                raise Exception("The lengths of pssm profile and dssp are not equal for: ", id)

        return dssp_line, pssm_list

    def train_model(self):
        x_train = self.svmProfile.x_train
        y_train = self.svmProfile.y_train
        self.model = svm.SVC(C=self.c_value, kernel="rbf", gamma=self.gamma_value)
        self.model.fit(x_train, y_train)


