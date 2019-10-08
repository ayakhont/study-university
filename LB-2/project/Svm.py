from sklearn import svm

x_train = [[0, 0], [0, 1], [1, 0], [1, 1]]
y_train = [0, 1, 1, 0]
# Create a SVC with RBF kernel with gamma=0.3 and C=8
mySVC = svm.SVC(C=8.0, kernel="rbf", gamma=0.3)
# Train (fit) the model on training data
mySVC.fit(x_train, y_train)