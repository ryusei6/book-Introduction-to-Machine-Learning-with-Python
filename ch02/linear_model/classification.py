import sys, os
sys.path.append('../../')
import mglearn
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC


def main():
    X, y = mglearn.datasets.make_forge()

    fig, axes = plt.subplots(1, 2, figsize=(10, 3))

    for model, ax in zip([LinearSVC(), LogisticRegression()], axes):
        clf = model.fit(X, y)
        mglearn.plots.plot_2d_separator(clf, X, fill=False, eps=0.5,
                                        ax=ax, alpha=.7)
        mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
        ax.set_title(clf.__class__.__name__)
        ax.set_xlabel("Feature 0")
        ax.set_ylabel("Feature 1")
    axes[0].legend()
    plt.show()

if __name__ == '__main__':
    main()
