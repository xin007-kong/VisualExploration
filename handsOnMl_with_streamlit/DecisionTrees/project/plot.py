import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap


def plot_decision_boundary(clf, X, y):
    custom_cmap = ListedColormap(['#fafab0', '#9898ff', '#a0faa0'])

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

    fig, ax = plt.subplots()
    cntr = ax.contourf(xx, yy, Z, alpha=0.3, cmap=custom_cmap)

    ax.set_xlabel('Petal Length')
    ax.set_ylabel('Petal Width')
    ax.set_title('Decision Boundary')

    return fig
