import seaborn as sns
import matplotlib.pyplot as plt


def create_corr_plot(data):
    fig, ax = plt.subplots()
    ax = sns.heatmap(data.corr(), annot=True, fmt=".2f")
    return fig
