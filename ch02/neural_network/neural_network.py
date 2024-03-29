from sklearn.datasets import load_breast_cancer
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split


def main():
    cancer = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)

    mean_on_train = X_train.mean(axis=0)
    std_on_train = X_train.std(axis=0)

    X_train_scaled = (X_train - mean_on_train) / std_on_train
    X_test_scaled = (X_test - mean_on_train) / std_on_train

    mlp = MLPClassifier(max_iter=1000, alpha=1, random_state=0)
    mlp.fit(X_train_scaled, y_train)

    print("Accuracy on training set: {:.3f}".format(mlp.score(X_train_scaled, y_train)))
    print("Accuracy on test set: {:.3f}".format(mlp.score(X_test_scaled, y_test)))


if __name__ == '__main__':
    main()
