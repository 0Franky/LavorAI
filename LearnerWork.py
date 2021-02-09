# # from sklearn.datasets import make_classification
# # from sklearn.model_selection import train_test_split
import csv
import numpy as np
from sklearn.datasets.base import Bunch

def load_dataset():
  with open('data/ESEMPI.csv') as csv_file:
      data_file = csv.reader(csv_file, delimiter = ";")
      temp = next(data_file)
      n_samples = int(temp[0])
      n_features = int(temp[1])
      data = np.empty((n_samples, n_features))
      target = np.empty((n_samples,), dtype=int)

      for i, sample in enumerate(data_file):
          data[i] = np.asarray(sample[:-1], dtype=np.float64)
          target[i] = np.asarray(sample[-1], dtype=int)
      # return [data, target]
      return Bunch(data=data, target=target)


dataset = load_dataset()

X = dataset.data
y = dataset.target

out = dataset.predict([2,2,2,5,4,2,2,5,2,4])
print(out)