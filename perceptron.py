#Improting the Perceptron package
from sklearn.linear_model import Perceptron

#We define the criteria of the Perceptron and fit the model
ppn = Perceptron (max_iter=50, eta0 = 0.1, random_state=0)
ppn.fit(X_train_std, y_train)

#We predict the outcome variable using standardized X variables
y_pred=ppn.predict(X_test_std)

#We print Misclassification, Accuracy, Confusion Matrix, Classification Report and RMSE
print ('Misclassified Perceptron samples: %d' % (y_test != y_pred).sum())
from sklearn.metrics import accuracy_score
print ('Perceptron Accuracy: %.2f' % (accuracy_score(y_test, y_pred)))
print ('Coefficients are: ')  
print (ppn.coef_)
from sklearn.metrics import classification_report, confusion_matrix
print('Confusion Matrix')
print(confusion_matrix(y_test, y_pred))
print('Classification Report')
print(classification_report(y_test, y_pred))
from sklearn.metrics import mean_squared_error
from math import sqrt
rms = sqrt(mean_squared_error(y_test, y_pred))
print('RMSE: ')
print(rms)

#We print the ROC curve
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_pred)
roc_auc = auc(false_positive_rate, true_positive_rate)
plt.title('Perceptron Receiver Operating Characteristic')
plt.plot(false_positive_rate, true_positive_rate, 'b',
label='AUC = %0.2f'% roc_auc)
plt.legend(loc='lower right')
plt.plot([0,1],[0,1],'r--')
plt.xlim([-0.1,1.2])
plt.ylim([-0.1,1.2])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()
