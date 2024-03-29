from sklearn.svm import SVC
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

def main():
    cancer = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)
    min_on_training = X_train.min(axis=0)
    range_on_training = (X_train - min_on_training).max(axis=0)

    X_train_scaled = (X_train - min_on_training) / range_on_training
    X_test_scaled = (X_test - min_on_training) / range_on_training

    svc = SVC(C=1000)
    svc.fit(X_train_scaled, y_train)

    print("Accuracy on training set: {:.3f}".format(svc.score(X_train_scaled, y_train)))
    print("Accuracy on test set: {:.3f}".format(svc.score(X_test_scaled, y_test)))


if __name__ == '__main__':
    main()
