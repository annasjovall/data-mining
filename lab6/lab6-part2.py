# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 10:23:48 2018

@author: AnnaPS
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix

#################TASK 1, READING THE DATASET#################
csv_path = 'iris.csv'
d = pd.read_csv(csv_path)
print(d.shape)

feature_vars = d.columns[:-1]
class_label_var = d.columns[-1]

X = d.drop(class_label_var, axis = 1)
Y = d[class_label_var]

#############TASK 2, SPLITTING TRAINING AND TESTING##########
X_train,X_test,Y_train,Y_test= train_test_split(X,Y)

#############TASK 3, DATA PREPROCESSING######################
scaler = StandardScaler()
scaler.fit(X_train)
scaler.transform(X_train, X_test)

#############TASK 4, TRAINING THE MODEL######################
layers = 3
hls = tuple([len(d.columns)]*layers)
mlp = MLPClassifier(hidden_layer_sizes=hls, max_iter=1000)
mlp.fit(X_train, Y_train)

#############TASK 5, PREDICTION AND EVALUATION###############
predictions = mlp.predict(X_test)
print(confusion_matrix(Y_test.values, predictions))
print(classification_report(Y_test.values, predictions))