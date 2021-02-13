from sklearn import metrics
from sklearn.metrics import classification_report
import seaborn as sns
import matplotlib.pyplot as plt

def show_matrix(validations, predictions, labels):
    """
    La matrice di mostra a video la differenza tra predizione e effettiva classificazione dell'immagine.
    :param validations: validazione (ground)
    :param predictions: predizioni effettuate
    :param labels: corrispondenze intero
    :return:
    """
    matrix = metrics.confusion_matrix(validations, predictions)
    plt.figure(figsize=(6, 4))
    sns.heatmap(matrix,
                cmap='coolwarm',
                linecolor='white',
                linewidths=1,
                xticklabels=labels,
                yticklabels=labels,
                annot=True,
                fmt='d')
    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.show()