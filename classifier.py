from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix


import itertools
import numpy as np
import matplotlib.pyplot as plt


from _data_loader import load_data, class_names


class CommentClassifier(object):
    def __init__(self):
        # load data
        self.data, self.headers = load_data()

        # initialize attributes
        self.pipeline = None
        self.fitted = False

    def build_pipeline(self):
        self.pipeline = Pipeline([('vect', CountVectorizer()),
                             ('tfidf', TfidfTransformer()),
                             ('clf', MultinomialNB())])

    def grid_search(self):
        if not self.pipeline:
            raise Exception('You must run build_pipeline first!')

        parameters = {'vect__ngram_range': [(1, 1), (1, 2)],
                      'tfidf__use_idf': (True, False),
                      'clf__alpha': (1e-2, 1e-3)}
        self.model = GridSearchCV(self.pipeline, parameters, n_jobs=-1)
        self.model.fit(self.data['X_train'][:, 3], self.data['y_train'])
        self.fitted = True


    def predict_test_set(self):
        if not self.fitted:
            raise Exception('You must run grid_search to fit the model first!')
        print '*' * 10
        print 'Results of prediction on unseen data'
        print '*' * 10

        y_pred = self.model.predict(self.data['X_test'][:, 3])

        # Compute confusion matrix
        cnf_matrix = confusion_matrix(self.data['y_test'], y_pred)
        np.set_printoptions(precision=2)

        # Plot normalized confusion matrix
        plt.figure()
        self.plot_confusion_matrix(cnf_matrix, class_names=class_names, normalize=True,
                              title='Normalized confusion matrix (Percentages)')

        plt.show()


    def plot_confusion_matrix(self, cm, class_names,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
        """
        This function prints and plots the confusion matrix.
        Normalization can be applied by setting `normalize=True`.
        """
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(class_names))
        plt.xticks(tick_marks, class_names, rotation=45)
        plt.yticks(tick_marks, class_names)

        if normalize:
            cm = 100 * np.round(cm.astype('float') / np.sum(cm), 3)
            print("Normalized confusion matrix")
        else:
            print('Confusion matrix, without normalization')

        print(cm)

        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, cm[i, j],
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')



    def predict_examples(self):
        if not self.fitted:
            raise Exception('You must run grid_search to fit the model first!')

        print 'Predictions on some unseen examples'

        for i, prediction in enumerate(self.model.predict(self.data['X_test'][0:10, 3])):
            print '*'*10
            print 'Example: {}'.format(self.data['X_test'][i])
            print 'Expected result: {}'.format(class_names[int(self.data['y_test'][i])])
            print 'Prediction: {}'.format(class_names[int(prediction)])


def main():
    clf = CommentClassifier()
    clf.build_pipeline()
    clf.grid_search()
    clf.predict_test_set()
    clf.predict_examples()


if __name__ == '__main__':
    main()
