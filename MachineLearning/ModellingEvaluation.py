from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

from ML import CSVHandler

"""
Discussed in the lecture, and also in the hands-on.

This algorithm evaluation technique is very fast. It has pros and cons:
* _Pro_. It is ideal for large datasets (millions of records): splitting a large dataset into largish sub-datasets 
    allows that that
 1) each split of the data is **not too tiny**, and 
 2) both are **representative** of the underlying problem. Because of the speed, it is useful to use this approach 
    when the algorithm you are investigating is slow to train.
     
* _Con_. A downside of this technique is that it can have a **high variance**. This means that differences in the
    training and test dataset can result in meaningful differences in the estimate of accuracy.

In the example below we split our dataset into 67%/33% splits for training and test and evaluate the accuracy of a 
    Logistic Regression model.
"""


class ModellingEvaluation:

    def __init__(self):
        return

    def evaluate_with_train_test_sets(self, test_size: float, seed: int):
        # Evaluate using a train and a test set
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
        model = LogisticRegression()  # choose a model
        model.fit(X_train, Y_train)  # train on the training set
        result = model.score(X_test, Y_test)  # get accuracy as measured on the test set
        print("Accuracy: %.3f%%" % (result * 100.0))

    def evaluate_with_shuffle_split_cross_validation(self, n_splits: int, test_size: float, seed:int):
        kfold = ShuffleSplit(n_splits=n_splits, test_size=test_size, random_state=seed)
        model = LogisticRegression()
        results = cross_val_score(model, X, Y, cv=kfold)
        print("Accuracy: %.3f%% (%.3f%%)" % (results.mean() * 100.0, results.std() * 100.0))


if __name__ == '__main__':
    modellingEvaluator = ModellingEvaluation()
    csvHandler = CSVHandler.CSVHandler()
    X, Y = csvHandler.represent(csvHandler.import_data())

    # prepare for the evaluation with a train and test set
    test_size = 0.35
    seed = 7
    n_splits = 10

    #modellingEvaluator.evaluate_with_train_test_sets(test_size, seed)
    modellingEvaluator.evaluate_with_shuffle_split_cross_validation(n_splits, test_size, seed)









