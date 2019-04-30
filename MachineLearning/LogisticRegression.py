from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

from sklearn.linear_model import LogisticRegression           # <---
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis           # <---
from sklearn.neighbors import KNeighborsClassifier                           # <---
from sklearn.naive_bayes import GaussianNB                           # <---
from sklearn.tree import DecisionTreeClassifier                           # <---
from sklearn.svm import SVC                           # <---


# load dataset
filename = '/home/urfin/Education/MachineLearning/pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]

# Logistic Regression Classification
kfold = KFold(n_splits=10, random_state=7)
model = LogisticRegression()  # specify a solver if you do not want a warning..
results = cross_val_score(model, X, Y, cv=kfold)
print("Logistic Regression Classification: ", results.mean())

# LDA Classification
kfold = KFold(n_splits=10, random_state=7)
model = LinearDiscriminantAnalysis()                           # <---
results = cross_val_score(model, X, Y, cv=kfold)
print("LDA Classification: ", results.mean())

# KNN Classification
kfold = KFold(n_splits=10, random_state=7)
model = KNeighborsClassifier()                           # <---
results = cross_val_score(model, X, Y, cv=kfold)
print("KNN Classification: ", results.mean())

# Gaussian Naive Bayes Classification
kfold = KFold(n_splits=10, random_state=7)
model = GaussianNB()                           # <---
results = cross_val_score(model, X, Y, cv=kfold)
print("Gaussian Naive Bayes Classification: ", results.mean())

# Classification and Regression Trees
kfold = KFold(n_splits=10, random_state=7)
model = DecisionTreeClassifier()                           # <---
results = cross_val_score(model, X, Y, cv=kfold)
print("Classification and Regression Trees: ", results.mean())

# Support Vector Machines (SVM)
kfold = KFold(n_splits=10, random_state=7)
model = SVC()                           # <---
                                        ### be explicit with gamma to e.g. auto if you want to avoid warnings
results = cross_val_score(model, X, Y, cv=kfold)
print("Support Vector Machines (SVM): ", results.mean())

