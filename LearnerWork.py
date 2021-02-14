# # from sklearn.datasets import make_classification
# # from sklearn.model_selection import train_test_split
import csv
import numpy as np
from sklearn import datasets
from sklearn import neighbors
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

# ds = datasets.load_iris()
# print(ds)

def load_dataset():
  with open('data/ESEMPI.csv') as csv_file:
      data_file = csv.reader(csv_file, delimiter = ";")
      temp = next(data_file)
      n_samples = int(temp[0])
      n_features = int(temp[1])
      data = np.empty((n_samples, n_features))
      target = np.empty((n_samples,), dtype=int)

      for i, sample in enumerate(data_file):
          data[i] = np.asarray(sample[:-1], dtype=int)
          target[i] = np.asarray(sample[-1], dtype=int)
      return [data, target]
    #   return {"data": data.tolist(), "target": target.tolist()}


def KNearestNeighbourClassifier(dataset):
    knn = neighbors.KNeighborsClassifier()
    return knn.fit(dataset[0], dataset[1])

def GaussianNaiveBayes(dataset):
    gnb = GaussianNB()
    return gnb.fit(dataset[0], dataset[1])

def DecisionTree(dataset, casualita_scelta_dopo_suddivisione = 0, cross_validation_ratio = 10, max_depth = None):
    clf = DecisionTreeClassifier(random_state=casualita_scelta_dopo_suddivisione, max_depth=max_depth)
    # cross_val_score(clf, dataset[0], dataset[1], cv=cross_validation_ratio) // to validate dataset
    return clf.fit(dataset[0], dataset[1])