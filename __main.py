from WorkUtils import workDecoder, getLabels
import LearnerWork
import ConfusioMatrix as cm
import matplotlib.pyplot as plt
import ValidationUtils as vu


dataset = LearnerWork.load_dataset()
# print(dataset)

model = LearnerWork.KNearestNeighbourClassifier(dataset)
# model = LearnerWork.GaussianNaiveBayes(dataset)
# model = LearnerWork.DecisionTree(dataset)
# model = LearnerWork.DecisionTree(dataset, max_depth = 3)
# model = LearnerWork.DecisionTree(dataset, max_depth = 8)

risposte = [[2, 2, 2, 5, 4, 2, 2, 5, 2, 4]]
# print(model.decision_path(risposte))
res = workDecoder(model.predict(risposte))

if res[0] != "Errore!":
    print("Secondo me il tuo lavoro e' di tipo '" +
          res[1] + "'... Ti vedo bene come " + res[0])
else:
    print("Si è verificato un errore. Scusa ma sto ancora imparando... '.'")


# # Test
# cm.show_matrix([1, 14, 5, 4, 5, 3, 3, 5, 6, 5], [2, 3, 4, 7, 3, 4, 2, 3, 6, 7], getLabels())
vu.ShowConfusionMatrix(dataset, 5, LearnerWork.DecisionTree)
