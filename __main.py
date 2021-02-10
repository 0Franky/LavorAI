from WorkUtils import workDecoder
import LearnerWork


dataset = LearnerWork.load_dataset()
# print(dataset)

# model = LearnerWork.KNearestNeighbourClassifier(dataset)
# model = LearnerWork.GaussianNaiveBayes(dataset)
model = LearnerWork.DecisionTree(dataset)
# model = LearnerWork.DecisionTree(dataset, max_depth = 3)
# model = LearnerWork.DecisionTree(dataset, max_depth = 8)

res = workDecoder(model.predict([[2,2,2,5,4,2,2,5,2,4]]))

if res[0] != "Errore!" :
    print("Secondo me il tuo lavoro è di tipo '" + res[1] + "'... Ti vedo bene come " + res[0])
else:
    print("Si è verificato un errore. Scusa ma sto ancora imparando... '.'")