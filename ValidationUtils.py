import ConfusioMatrix as cm
from sklearn import metrics
from sklearn.metrics import classification_report
from WorkUtils import getLabels


def KFoldCrossValidation(dataset, k):
  lista1 = []
  lista2 = []
  temp = []

  n = len(dataset)
  nT = int(n/k)
  a = 0
  b = nT

  lista2.append(dataset[a: b])
  lista2.append(dataset[nT:])
  lista1.append(lista2)
  a = a + nT
  b = b + nT
  temp.extend(dataset[0: a])
  temp.extend(dataset[b:])
  # print(lista1)
  # print("\n\n\n\n")

  for i in range(4):
    lista2 = []
    lista2.append(dataset[a: b])
    lista2.append(temp)
    lista1.append(lista2)
    temp = []
    a = a + nT
    b = b + nT
    temp.extend(dataset[0: a])
    temp.extend(dataset[b:])
    # print(lista1)
    # print("\n\n\n\n")
  # print(lista1)

  return lista1


def ShowConfusionMatrix(dataset, k, trainingModelCB):
  kfoldAnsw = KFoldCrossValidation(dataset[0], k)
  kfoldWork = KFoldCrossValidation(dataset[1], k)
  predictions = []
  rightWorks = []

  for i in range(k):
    model = trainingModelCB([kfoldAnsw[1][1], kfoldWork[1][1]])
    for j in range(len(kfoldAnsw[i][0])):
      predictions.append(model.predict([kfoldAnsw[i][0][j]]))

  for x in kfoldWork:
    for j in range(len(kfoldWork[i][0])):
      rightWorks.append(x[0][j])
  # cm.show_matrix(rightWorks, predictions, getLabels())
  # print(classification_report(rightWorks, predictions, target_names=getLabels()))
  
  # metrics.log_loss(rightWorks, predictions)
  print(classification_report(rightWorks, predictions, target_names=getLabels()))
  cm.show_matrix(rightWorks, predictions, getLabels())
    
