import sys, os
sys.path.append('../../')
import mglearn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import LinearSVC
from sklearn.datasets import make_blobs


def main():
    X, y = make_blobs(random_state=42)
    linear_svm = LinearSVC().fit(X, y)
    mglearn.plots.plot_2d_classification(linear_svm, X, fill=True, alpha=.7)
    mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
    line = np.linspace(-15, 15)
    for coef, intercept, color in zip(linear_svm.coef_, linear_svm.intercept_,mglearn.cm3.colors):
        plt.plot(line, -(line * coef[0] + intercept) / coef[1], c=color)
    plt.xlabel("Feature 0")
    plt.ylabel("Feature 1")
    plt.legend(['Class 0', 'Class 1', 'Class 2', 'Line class 0', 'Line class 1','Line class 2'], loc=(1.01, 0.3))
    plt.show()


if __name__ == '__main__':
    main()
