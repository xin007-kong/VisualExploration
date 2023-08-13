from sklearn.tree import DecisionTreeClassifier


def train_model(X, y):
    clf = DecisionTreeClassifier()
    clf.fit(X, y)
    return clf


def predict(clf, X_new):
    y_pred = clf.predict(X_new)
    return y_pred
