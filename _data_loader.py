import os
from sklearn.model_selection import train_test_split

import os
import csv
import numpy as np

headers = ['COMMENT_ID', 'AUTHOR', 'DATE', 'CONTENT', 'TAG']


def _get_data():
    data = []

    for filename in os.listdir('data'):
        with open(os.path.join('data', filename), 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            reader.next()  # skip first row
            for row in reader:
                data.append(row)

    return np.array(data)


def _split_x_y(data):
    X = data[:, :-1]
    y = data[:, -1]

    return X, y


def load_data():
    X, y = _split_x_y(_get_data())
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    data = {'X_train': X_train, 'X_test': X_test, 'y_test': y_test, 'y_train': y_train}

    return data, headers
