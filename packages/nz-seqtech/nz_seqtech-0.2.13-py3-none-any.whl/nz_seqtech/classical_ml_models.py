import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.gaussian_process.kernels import RBF
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
import warnings
warnings.simplefilter('ignore')

def knn_model(X=None, y=None, suggested_data=False, test_size=0.25, random_state=1, n_neighbors=3):
    """
    Train and evaluate the K Nearest Neighbors classifier.

    Args:
        X (numpy array): Data features.
        y (numpy array): Data labels.
        suggested_data (bool): Whether to use the suggested dataset or not.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.
        n_neighbors (int): Number of neighbors to use.

    Returns:
        str: Classification report containing precision, recall, F1-score, and support metrics.
            The report provides information about the model's performance on the test data.
            If data loading or formatting fails, None is returned.
    """
    if suggested_data:
        X_train, X_test, y_train, y_test = load_dataset(suggested_data=True, test_size=test_size, random_state=random_state)
    else:
        if X is None or y is None:
            print("Data loading failed.")
            return None
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    model = KNeighborsClassifier(n_neighbors=n_neighbors)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = print(classification_report(y_test, y_pred))
    return report

def gaussian_process_model(X=None, y=None, suggested_data=False, test_size=0.25, random_state=1, kernel=None):
    """
    Train and evaluate the Gaussian Process classifier.

    Args:
        X (numpy array): Data features.
        y (numpy array): Data labels.
        suggested_data (bool): Whether to use the suggested dataset or not.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.
        kernel (sklearn.gaussian_process.kernels object): The kernel specifying the covariance function of the GP.

    Returns:
        str: Classification report containing precision, recall, F1-score, and support metrics.
            The report provides information about the model's performance on the test data.
            If data loading or formatting fails, None is returned.
    """
    if suggested_data:
        X_train, X_test, y_train, y_test = load_dataset(suggested_data=True, test_size=test_size, random_state=random_state)
    else:
        if X is None or y is None:
            print("Data loading failed.")
            return None
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    if kernel is None:
        kernel = 1.0 * RBF(1.0)
    model = GaussianProcessClassifier(kernel=kernel)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = print(classification_report(y_test, y_pred))
    return report

def decision_tree_model(X=None, y=None, suggested_data=False, test_size=0.25, random_state=1, max_depth=5):
    """
    Train and evaluate the Decision Tree classifier.

    Args:
        X (numpy array): Data features.
        y (numpy array): Data labels.
        suggested_data (bool): Whether to use the suggested dataset or not.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.
        max_depth (int): The maximum depth of the tree.

    Returns:
        str: Classification report containing precision, recall, F1-score, and support metrics.
            The report provides information about the model's performance on the test data.
            If data loading or formatting fails, None is returned.
    """
    if suggested_data:
        X_train, X_test, y_train, y_test = load_dataset(suggested_data=True, test_size=test_size, random_state=random_state)
    else:
        if X is None or y is None:
            print("Data loading failed.")
            return None
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    model = DecisionTreeClassifier(max_depth=max_depth)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = print(classification_report(y_test, y_pred))
    return report

def random_forest_model(X=None, y=None, suggested_data=False, test_size=0.25, random_state=1, max_depth=5, n_estimators=10, max_features=1):
    """
    Train and evaluate the Random Forest classifier.

    Args:
        X (numpy array): Data features.
        y (numpy array): Data labels.
        suggested_data (bool): Whether to use the suggested dataset or not.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.
        max_depth (int): The maximum depth of the tree.
        n_estimators (int): The number of trees in the forest.
        max_features (int): The number of features to consider when looking for the best split.

    Returns:
        str: Classification report containing precision, recall, F1-score, and support metrics.
            The report provides information about the model's performance on the test data.
            If data loading or formatting fails, None is returned.
    """
    if suggested_data:
        X_train, X_test, y_train, y_test = load_dataset(suggested_data=True, test_size=test_size, random_state=random_state)
    else:
        if X is None or y is None:
            print("Data loading failed.")
            return None
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    model = RandomForestClassifier(max_depth=max_depth, n_estimators=n_estimators, max_features=max_features)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = print(classification_report(y_test, y_pred))
    return report

def neural_net_model(X=None, y=None, suggested_data=False, test_size=0.25, random_state=1, alpha=1.0):
    """
    Train and evaluate the Neural Network classifier.

    Args:
        X (numpy array): Data features.
        y (numpy array): Data labels.
        suggested_data (bool): Whether to use the suggested dataset or not.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.
        alpha (float): L2 penalty (regularization term) parameter.

    Returns:
        str: Classification report containing precision, recall, F1-score, and support metrics.
            The report provides information about the model's performance on the test data.
            If data loading or formatting fails, None is returned.
    """
    if suggested_data:
        X_train, X_test, y_train, y_test = load_dataset(suggested_data=True, test_size=test_size, random_state=random_state)
    else:
        if X is None or y is None:
            print("Data loading failed.")
            return None
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    model = MLPClassifier(alpha=alpha)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = print(classification_report(y_test, y_pred))
    return report

def adaboost_model(X=None, y=None, suggested_data=False, test_size=0.25, random_state=1, n_estimators=50, learning_rate=1.0):
    """
    Train and evaluate the AdaBoost classifier.

    Args:
        X (numpy array): Data features.
        y (numpy array): Data labels.
        suggested_data (bool): Whether to use the suggested dataset or not.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.
        n_estimators (int): The maximum number of estimators at which boosting is terminated.
        learning_rate (float): Weight applied to each classifier at each boosting iteration.

    Returns:
        str: Classification report containing precision, recall, F1-score, and support metrics.
            The report provides information about the model's performance on the test data.
            If data loading or formatting fails, None is returned.
    """
    if suggested_data:
        X_train, X_test, y_train, y_test = load_dataset(suggested_data=True, test_size=test_size, random_state=random_state)
    else:
        if X is None or y is None:
            print("Data loading failed.")
            return None
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    model = AdaBoostClassifier(n_estimators=n_estimators, learning_rate=learning_rate)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = print(classification_report(y_test, y_pred))
    return report

def gaussian_nb_model(X=None, y=None, suggested_data=False, test_size=0.25, random_state=1):
    """
    Train and evaluate the Gaussian Naive Bayes classifier.

    Args:
        X (numpy array): Data features.
        y (numpy array): Data labels.
        suggested_data (bool): Whether to use the suggested dataset or not.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.

    Returns:
        str: Classification report containing precision, recall, F1-score, and support metrics.
            The report provides information about the model's performance on the test data.
            If data loading or formatting fails, None is returned.
    """
    if suggested_data:
        X_train, X_test, y_train, y_test = load_dataset(suggested_data=True, test_size=test_size, random_state=random_state)
    else:
        if X is None or y is None:
            print("Data loading failed.")
            return None
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    model = GaussianNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = print(classification_report(y_test, y_pred))
    return report

def svm_linear_model(X=None, y=None, suggested_data=False, test_size=0.25, random_state=1, C=1.0):
    """
    Train and evaluate the Support Vector Machine (SVM) classifier with a linear kernel.

    Args:
        X (numpy array): Data features.
        y (numpy array): Data labels.
        suggested_data (bool): Whether to use the suggested dataset or not.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.
        C (float): Regularization parameter.

    Returns:
        str: Classification report containing precision, recall, F1-score, and support metrics.
            The report provides information about the model's performance on the test data.
            If data loading or formatting fails, None is returned.
    """
    if suggested_data:
        X_train, X_test, y_train, y_test = load_dataset(suggested_data=True, test_size=test_size, random_state=random_state)
    else:
        if X is None or y is None:
            print("Data loading failed.")
            return None
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    model = svm.SVC(kernel='linear', C=C)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = print(classification_report(y_test, y_pred))
    return report

def svm_rbf_model(X=None, y=None, suggested_data=False, test_size=0.25, random_state=1, C=1.0, gamma='scale'):
    """
    Train and evaluate the Support Vector Machine (SVM) classifier with an RBF kernel.

    Args:
        X (numpy array): Data features.
        y (numpy array): Data labels.
        suggested_data (bool): Whether to use the suggested dataset or not.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.
        C (float): Regularization parameter.
        gamma (str or float): Kernel coefficient.

    Returns:
        str: Classification report containing precision, recall, F1-score, and support metrics.
            The report provides information about the model's performance on the test data.
            If data loading or formatting fails, None is returned.
    """
    if suggested_data:
        X_train, X_test, y_train, y_test = load_dataset(suggested_data=True, test_size=test_size, random_state=random_state)
    else:
        if X is None or y is None:
            print("Data loading failed.")
            return None
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    model = svm.SVC(kernel='rbf', C=C, gamma=gamma)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = print(classification_report(y_test, y_pred))
    return report

def svm_sigmoid_model(X=None, y=None, suggested_data=False, test_size=0.25, random_state=1, C=1.0):
    """
    Train and evaluate the Support Vector Machine (SVM) classifier with a sigmoid kernel.

    Args:
        X (numpy array): Data features.
        y (numpy array): Data labels.
        suggested_data (bool): Whether to use the suggested dataset or not.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.
        C (float): Regularization parameter.

    Returns:
        str: Classification report containing precision, recall, F1-score, and support metrics.
            The report provides information about the model's performance on the test data.
            If data loading or formatting fails, None is returned.
    """
    if suggested_data:
        X_train, X_test, y_train, y_test = load_dataset(suggested_data=True, test_size=test_size, random_state=random_state)
    else:
        if X is None or y is None:
            print("Data loading failed.")
            return None
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    model = svm.SVC(kernel='sigmoid', C=C)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = print(classification_report(y_test, y_pred))
    return report

def load_dataset(X_train=None, X_test=None, y_train=None, y_test=None, suggested_data=False, test_size=0.25, random_state=1):
    """
    Load and preprocess the dataset for classification.

    Args:
        X_train (numpy array): Training data features.
        X_test (numpy array): Testing data features.
        y_train (numpy array): Training data labels.
        y_test (numpy array): Testing data labels.
        suggested_data (bool): Whether to use the suggested dataset or not.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.

    Returns:
        tuple: A tuple containing X_train, X_test, y_train, and y_test data arrays.
            The function loads the dataset and performs preprocessing steps like splitting
            into training and testing sets. If the provided data does not have the appropriate
            format or if data loading fails, None is returned for all arrays.
    """
    if X_train is not None and X_test is not None and y_train is not None and y_test is not None:
        if len(X_train.shape) != 2 or len(X_test.shape) != 2 or len(y_train.shape) != 1 or len(y_test.shape) != 1:
            print("The provided data does not have the appropriate format.")
            return None, None, None, None
        else:
            return X_train, X_test, y_train, y_test

    if suggested_data:
        X_train, X_test, y_train, y_test = suggested_dataset1(test_size, random_state)
    return X_train, X_test, y_train, y_test

def suggested_dataset1(test_size=0.25, random_state=1):
    """
    Load and preprocess a suggested dataset for classification.

    Args:
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.

    Returns:
        tuple: A tuple containing X_train, X_test, y_train, and y_test data arrays.
            The function loads a dataset of promoter gene sequences and performs preprocessing steps,
            including one-hot encoding and train-test splitting. The resulting arrays are returned.
    """
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/molecular-biology/promoter-gene-sequences/promoters.data'
    names = ['Class', 'id', 'Sequence']

    data = pd.read_csv(url, names=names)

    clases = data.loc[:, 'Class']
    sequence = list(data.loc[:, 'Sequence'])
    dic = {}
    for i, seq in enumerate(sequence):
        nucleotides = list(seq)
        nucleotides = [char for char in nucleotides if char != '\t']
        nucleotides.append(clases[i])

        dic[i] = nucleotides

    df = pd.DataFrame(dic)
    df = df.transpose()
    df.rename(columns={57: 'Class'}, inplace=True)

    numerical_df = pd.get_dummies(df)
    numerical_df.drop('Class_-', axis=1, inplace=True)
    numerical_df.rename(columns={'Class_+': 'Class'}, inplace=True)

    X = numerical_df.drop(['Class'], axis=1).values
    y = numerical_df['Class'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    return X_train, X_test, y_train, y_test
