from WorkUtils import workDecoder, getLabels
from Survey import startSurvey
import LearnerWork
import ConfusioMatrix as cm
import matplotlib.pyplot as plt
import ValidationUtils as vu
import os


dataset = LearnerWork.load_dataset()
# print(dataset)

model = LearnerWork.KNearestNeighbourClassifier(dataset)
# model = LearnerWork.GaussianNaiveBayes(dataset)
# model = LearnerWork.DecisionTree(dataset)
# model = LearnerWork.DecisionTree(dataset, max_depth = 3)
# model = LearnerWork.DecisionTree(dataset, max_depth = 8)

# models = [LearnerWork.KNearestNeighbourClassifier, LearnerWork.GaussianNaiveBayes, LearnerWork.DecisionTree]

risposte = [startSurvey()]
# print(model.decision_path(risposte))
res = workDecoder(model.predict(risposte))

print('\n\n\n')
if res[0] != "Errore!":
  print("Secondo me il tuo lavoro e' di tipo '" +
        res[1] + "'... Ti vedo bene come " + res[0])
else:
  print("Si è verificato un errore. Scusa ma sto ancora imparando... '.'")



print('\n\n\n')

Networkx_idc = os.path.dirname(os.path.realpath(__file__)) + '\\Networkx_idc.py'
os.system('python ' + Networkx_idc)

print('\n\n')

# # Test
# for m in models:
#   # cm.show_matrix([1, 14, 5, 4, 5, 3, 3, 5, 6, 5], [2, 3, 4, 7, 3, 4, 2, 3, 6, 7], getLabels())
#   vu.validateDataset(dataset, 5, m)

# # vu.validateDataset(dataset, 5, LearnerWork.DecisionTree)
