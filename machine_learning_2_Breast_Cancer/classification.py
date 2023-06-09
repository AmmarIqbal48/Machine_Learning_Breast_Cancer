import numpy as np
import pandas as pd
import sklearn as sk
from sklearn import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV 
from sklearn.kernel_approximation import RBFSampler
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
import warnings
import math

warnings.filterwarnings("ignore")

x = pd.read_csv(r'LNIP_super_all.csv')

def sensitivity(tn,fp,fn,tp):
    return round(float(tp/(tp+fn)),2)

def specificity(tn,fp,fn,tp):
    return round(float(tn/(tn+fp)),2)

def precision(tn,fp,fn,tp):
    return round(float(tp/tn+fp),2)

def error_rate(tn,fp,fn,tp):
    return round((fp+fn)/(tp+tn+fp+fn),2)

def quality_index(sensitivity,specificity):
    return round(float(math.sqrt(sensitivity*specificity)),2)

training_set,test_set = train_test_split(x,test_size=0.2,random_state=0)
X_train = training_set.iloc[:,0:512].values
Y_train = training_set.iloc[:,512].values
X_test = test_set.iloc[:,0:512].values
Y_test = test_set.iloc[:,512].values


#################Optimized SVM with RBF Kernel###############
#For getting 98% accuracy feed C=1100 and Gamma = 1000
#         https://scikit-learn.org/0.18/modules/generated/sklearn.svm.NuSVC.html
classifier = SVC(C=1100, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma=1000, kernel='rbf', max_iter=-1,
    probability=False, random_state=None, shrinking=True, tol=0.001,
    verbose=False)
classifier.fit(X_train,Y_train)
SVM_pred = classifier.predict(X_test)
cm = confusion_matrix(Y_test,SVM_pred)
tn = cm[0][0]
fp = cm[0][1]
fn = cm[1][0]
tp = cm[1][1]
sens1 = sensitivity(tn,fp,fn,tp)
spec1 = specificity(tn,fp,fn,tp)
prec  = precision(tn,fp,fn,tp)
err_rate = error_rate(tn,fp,fn,tp)
QI = quality_index(sens1,spec1)
print("################ Details of Optimized RBF kernel ########################")
print("Sensitivity -> "+str(sens1))
print("Specificity -> "+str(spec1))
print("Precision   -> "+str(prec))
print("Error Rate  -> "+str(err_rate))
print("Quality Index-> "+str(QI))
accuracy = float(cm.diagonal().sum())/len(Y_test)
print("Accuracy : ",accuracy*100)
print("\n")
##print(cm)
##accuracy = float(cm.diagonal().sum())/len(Y_test)
##print("\nAccuracy Of Optimized SVM with RBF kernel "+str(accuracy*100))#+" by optimized RBF with 'C'= "+str(1100)+" Gamma value= "+str(1000))

########################Linear SVM Classifier###############
#       https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html
SVM = svm.LinearSVC()
#   Fit the model according to the given training data.
SVM.fit(X_train,Y_train)
#   Predict class labels for samples in X.
SVM_pred = SVM.predict(X_test)
cm = confusion_matrix(Y_test,SVM_pred)
tn = cm[0][0]
fp = cm[0][1]
fn = cm[1][0]
tp = cm[1][1]
sens1 = sensitivity(tn,fp,fn,tp)
spec1 = specificity(tn,fp,fn,tp)
prec  = precision(tn,fp,fn,tp)
err_rate = error_rate(tn,fp,fn,tp)
QI = quality_index(sens1,spec1)
print("################ Details of Linear SVM ########################")
print("Sensitivity -> "+str(sens1))
print("Specificity -> "+str(spec1))
print("Precision   -> "+str(prec))
print("Error Rate  -> "+str(err_rate))
print("Quality Index-> "+str(QI))
accuracy = float(cm.diagonal().sum())/len(Y_test)
print("Accuracy : ",accuracy*100)
print("\n")
##accuracy = float(cm.diagonal().sum())/len(Y_test)
##print("\nAccuracy Of Linear SVM For The Given Dataset: ", accuracy*100)

######################## Random Forest Classifier#################
#       https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
rfc = RandomForestClassifier()
#	 Build a forest of trees from the training set (X, Y).
rfc.fit(X_train,Y_train)
#	 Predict class for X.
rfc_predict = rfc.predict(X_test)
cm = confusion_matrix(Y_test,rfc_predict)
tn = cm[0][0]
fp = cm[0][1]
fn = cm[1][0]
tp = cm[1][1]
sens1 = sensitivity(tn,fp,fn,tp)
spec1 = specificity(tn,fp,fn,tp)
prec  = precision(tn,fp,fn,tp)
err_rate = error_rate(tn,fp,fn,tp)
QI = quality_index(sens1,spec1)
print("################ Details of Random Forest ########################")
print("Sensitivity -> "+str(sens1))
print("Specificity -> "+str(spec1))
print("Precision   -> "+str(prec))
print("Error Rate  -> "+str(err_rate))
print("Quality Index-> "+str(QI))
accuracy = float(cm.diagonal().sum())/len(Y_test)
print("Accuracy : ",accuracy*100)
print("\n")

