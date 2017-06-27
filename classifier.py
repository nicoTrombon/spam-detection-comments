from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

from _data_loader import load_data


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

    def predict_examples(self):
        if not self.fitted:
            raise Exception('You must run grid_search to fit the model first!')

        print 'Predictions for some examples'

        for i, prediction in enumerate(self.model.predict(self.data['X_test'][0:5, 3])):
            print '*'*10
            print 'Example: {}'.format(self.data['X_test'][i])
            print 'Expected result: {}'.format(self.data['y_test'][i])
            print 'Prediction: {}'.format(prediction)


def main():
    clf = CommentClassifier()
    clf.build_pipeline()
    clf.grid_search()
    clf.predict_examples()


if __name__ == '__main__':
    main()