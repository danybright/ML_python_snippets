import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix


def plt_confusion_mtx(y_test, y_pred):
    """ 

    Plot Confusion Matrix Heatmap for the Actual vs Predicted

    Parameters
    ----------
    y_test : pandas DataFrame or Series
    The test values of the project

    y_pred : pandas DataFrame or Series
    The predicted values of the project

    """
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(15, 15))
    sns.heatmap(cm, annot=True, fmt='.3f', linewidths=.5,
                square=True, cmap='Blues_r')
    plt.ylabel('Actual Label')
    plt.xlabel('Predicted Label')
    all_sample_title = 'Accuracy Score: {0}'.format(
        accuracy_score(y_test, y_pred))
    plt.title(all_sample_title, size=20)
