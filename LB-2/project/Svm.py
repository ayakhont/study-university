from sklearn import svm
from project.PathConstants import PathConstants


class Svm:

    window_size: int

    def __init__(self, window_size: int):
        self.window_size = window_size

    @staticmethod
    def parse_pssm_by_id(id: str) -> (list, list):
        dssp_line = ""
        with open(PathConstants.training_dssp_dir + id + ".dssp", "r") as dssp_file:
            for dssp_line_in_file in dssp_file:
                if dssp_line_in_file[0] != '>':
                    dssp_line = dssp_line_in_file.rstrip()
        pssm_list = list()
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
        x_train = [[0, 0], [0, 1], [1, 0], [1, 1]]
        y_train = [0, 1, 1, 0]
        # Create a SVC with RBF kernel with gamma=0.3 and C=8
        mySVC = svm.SVC(C=8.0, kernel="rbf", gamma=0.3)
        # Train (fit) the model on training data
        mySVC.fit(x_train, y_train)


y_train, x_train = Svm.parse_pssm_by_id("d1a1xa_")