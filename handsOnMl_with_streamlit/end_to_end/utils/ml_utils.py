from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV


def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def fine_tune_model(model, X_train, y_train):
    param_grid = {'fit_intercept': [True, False], 'normalize': [
        True, False], 'copy_X': [True, False]}
    grid_search = GridSearchCV(model, param_grid, cv=5)
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_
