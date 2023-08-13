from sklearn.datasets import load_iris


def load_data():
    iris = load_iris(as_frame=True)
    X = iris.data[["petal length (cm)", "petal width (cm)"]].values
    y = iris.target
    return X, y
