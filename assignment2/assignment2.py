# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 16:24:14 2018

@author: Anna Palmqvist Sjövall
StudentID: 19832192
"""
import pandas as pd
import numpy as np

from Orange.data import Table, Domain
from Orange.classification import NNClassificationLearner
from Orange.evaluation import CrossValidation, scoring
from Orange.preprocess import Discretize, discretize
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.cluster import KMeans


csv_path = 'white_wine.csv'

print("\n\n---------------- Q1 --------------------")

"""
Remove minority classes takes a pandas dataframe, removes the minority classes 
with the number of tuples < the cutoff and returns a Table.
(Filter rows, for Q1, c))
"""
def remove_minority_classes(dataframe, cutoff):
    temp_path = 'temp.csv'
    u, c = np.unique(dataframe.quality, return_counts = True)
    #Remove rows
    for (elem, count) in zip(u,c):
        if count < cutoff:
            index = dataframe[dataframe.quality == elem].index
            dataframe = dataframe.drop(index)
    #Turn back into Table
    dataframe.to_csv(temp_path, index=False)
    return Table.from_file(temp_path)

"""
Takes a table (Orange.data.Table) of white_wines and prints the accuracy and 
AUC of applying a NNClassificationLearner for the class label 'quality'. Also 
discretizes the features with number of bins, n.
"""
def predict_wine_quality(table, n):
    #Make the continous varibles discrete
    disc = Discretize()
    disc.method = discretize.EqualWidth(n = n)
    table = disc(table)
    #Define domain    
    feature_vars = list(table.domain[1:])
    class_label_var = table.domain[0]        
    wine_domain = Domain(feature_vars, class_label_var)
    table = Table.from_table(domain=wine_domain, source=table)
    #Construct learner and print results
    tree_learner = NNClassificationLearner(hidden_layer_sizes=(10,), max_iter = 4000)
    eval_results = CrossValidation(table, [tree_learner], k=10)
    print("Accuracy of cross validation: {:.3f}".format(scoring.CA(eval_results)[0]))
    print("AUC: {:.3f}".format(scoring.AUC(eval_results)[0]))


table = Table.from_file(csv_path)
dataframe = pd.read_csv(csv_path)

table_c = remove_minority_classes(dataframe, 10)

#Accuracy of cross validation: 0.766
#AUC: 0.752
#[<3] [3-5] [5-7] [>=7]
print("\nWine quality prediction for the table white_wine:")
predict_wine_quality(table, 4)

#Accuracy of cross validation: 0.522
#AUC: 0.697
#[<=4] [4-6] [6-7] [>=7]
print("\nWine quality prediction with minority classes removed:")
predict_wine_quality(table_c, 4)
 


print("\n\n---------------- Q2 --------------------")
layers = 3
neurons = 10

data = pd.read_csv(csv_path)

class_label_var = data.columns[0]

X = data.drop(class_label_var, axis = 1)
Y = data[class_label_var]

#Splits into random train and test subsets
X_train,X_test,Y_train,Y_test= train_test_split(X,Y)
#Normalize data.
scaler = StandardScaler()
scaler.fit(X_train)
scaler.transform(X_train, X_test)

hls = tuple([neurons]*layers)
mlp = MLPClassifier(hidden_layer_sizes=hls, max_iter=6000)
mlp.fit(X_train, Y_train)
predictions = mlp.predict(X_test)

print("\nConfusion Matrix: \n%s" % confusion_matrix(Y_test.values, predictions))
print("\n\nClassification report: \n%s" % classification_report(Y_test.values, predictions))



print("\n\n---------------- Q3 --------------------")
k=2

data_tab = Table('ionosphere')

estimator = KMeans(n_clusters=k, random_state=0)
k_clusters = estimator.fit(data_tab)

class_labels = data_tab[:,len(data_tab[0]) - 1]

#Arranged as [b0, b1, g0, g1].
combinations = ['00', '01', '10', '11']
#Returns a list where the elements represents the original class and 
#which cluster the elements have ended up in. 
#E.g. '00' means the element was in class b and in cluster 0
results = [list(filter(lambda c: int(c[0]) in cl and int(c[1])==kcl, combinations)) 
           for (cl,kcl) in zip(class_labels, k_clusters.labels_)]

_, c = np.unique(results, return_counts = True)

print("\t\t y='g' \t\t y='b'\n Cluster 0 \t%d \t\t %d \n Cluster 1 \t%d \t\t %d"
      % (c[2], c[0], c[3], c[1]))
