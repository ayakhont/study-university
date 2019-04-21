from pandas import read_csv
from numpy import loadtxt, ndarray
from matplotlib import pyplot
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA


class CSVHandler:

    fileName: str = "pima-indians-diabetes.data.csv"
    filePath: str = "/home/urfin/Education/MachineLearning/"

    def __init__(self):
        pass

    # numpy handling
    def extract(self):
        with open(self.filePath + self.fileName, "rt") as file:
            data = loadtxt(file, delimiter=",")
            print(data.shape)

    # panda handling
    def extract_with_panda(self):
        names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
        data = read_csv(self.filePath + self.fileName, names=names)
        print(data)
        data.hist()
        pyplot.rcParams["figure.figsize"] = [16,16]
        pyplot.show()

    # data import
    def import_data(self) -> ndarray:
        names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
        data = read_csv(self.filePath + self.fileName, names=names)
        array = data.values
        return array

    def represent(self, array: ndarray):
        # separate array into input and output components
        X = array[:, 0:8]   # features: build an array with each element being a full
                            # row with all columns but the last (values) one
        Y = array[:, 8]  # labels: build an array with only last column, i.e. labels only
        print(X)
        return X, Y

    def scale_data(self, X):
        # Rescale data (between 0 and 1)
        scaler = MinMaxScaler(feature_range=(0, 1))
        rescaledX = scaler.fit_transform(X)

        # summarize original data...
        set_printoptions(precision=3)
        print(X[0:5, :])

    def standardize_data(self, X):
        # Standardize data (0 mean, 1 stdev)
        scaler = StandardScaler().fit(X)
        rescaledX = scaler.transform(X)

        # summarize transformed data
        set_printoptions(precision=3)
        print(rescaledX[0:5, :])

    def normalize(self, X):
        # Normalize data (length of 1)
        scaler = Normalizer().fit(X)
        normalizedX = scaler.transform(X)

        # summarize transformed data
        set_printoptions(precision=3)
        print(normalizedX[0:5, :])

    def fit(self, X, Y):
        # Feature Extraction with Univariate Statistical Tests (Chi-squared for classification)
        test = SelectKBest(score_func=chi2, k=4)
        fit = test.fit(X, Y)
        # summarize scores
        set_printoptions(precision=3)
        print("Scores: ", fit.scores_)

    def apply_RFE(self, X):
        # Feature Extraction with RFE
        model = LogisticRegression()
        rfe = RFE(model, 3)  # my choice: seek for 3 features
        fit = rfe.fit(X, Y)
        print("Num Features: %d" % fit.n_features_)
        print("Selected Features: %s" % fit.support_)
        print("Feature Ranking: %s" % fit.ranking_)

    def apply_PCA(self, X):
        # Feature Extraction with PCA
        pca = PCA(n_components=3)
        fit = pca.fit(X)
        # summarize components
        print("Explained Variance: %s" % fit.explained_variance_ratio_)
        print(fit.components_)


if __name__ == '__main__':
    handler = CSVHandler()
    X, Y = handler.represent(handler.import_data())
    handler.scale_data(X)
    handler.standardize_data(X)
    handler.normalize(X)
    handler.fit(X, Y)
    handler.apply_RFE(X)
    handler.apply_PCA(X)

