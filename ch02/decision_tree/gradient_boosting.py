import sys, os
sys.path.append('../../')
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier

def main():
    cancer = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(
        cancer.data, cancer.target, stratify=cancer.target, random_state=42)

    gbrt = GradientBoostingClassifier(random_state=0, max_depth=1)
    gbrt.fit(X_train, y_train)

    print("Accuracy on training set: {:.3f}".format(gbrt.score(X_train, y_train)))
    print("Accuracy on test set: {:.3f}".format(gbrt.score(X_test, y_test)))


if __name__ == '__main__':
    main()
