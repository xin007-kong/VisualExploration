from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
import pandas as pd

def load_data():
    boston = load_boston()
    df = pd.DataFrame(boston.data, columns=boston.feature_names)
    df['MEDV'] = boston.target
    return df

def prepare_data(data):
    X = data.drop("MEDV", axis=1)
    y = data["MEDV"]
    return train_test_split(X, y, test_size=0.2, random_state=42)
