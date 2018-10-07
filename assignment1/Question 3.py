# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 09:28:24 2018

@author: Anna Palmqvist Sjövall
"""
import pandas as pd

from Orange.data import Table, Domain
from Orange.classification import SklTreeLearner
from Orange.evaluation import CrossValidation, scoring

"""
The values for attribute “Tenants” are missing for some tuples. Write a Python script to
read the input CSV file (assg1_room.csv), replace the missing values with the mean
value for that attribute, and then export the entire dataset to another CSV file. Remember
to keep all other attribute values unchanged 
"""
inx_class_label = 6 #Index to attribute 'Accept', which is the class label

csv_path = 'assg1_room.csv'
csv_path_fixed = 'assg1_room_fixed.csv' 
d = pd.read_csv(csv_path)

mean_tenants = round(d['Tenants'].mean())
d['Tenants'].fillna(mean_tenants, inplace=True)
d.to_csv(csv_path_fixed, index=False)

"""
Using the data exported in part (a), create an Orange3 decision tree learner and perform
a 10-fold cross-validation to evaluate the performance of its decision tree classifier with
this data.
"""
#rm_elem takes input list,l and index, i and returns a tuple (a,b), a is the 
#element at l[i] and b is the list without a.
def rm_elem(l, i):
    (a,b) = ('', [])
    for x in range(len(l)):
        if x==i: a = l[x]
        else: b.append(l[x])
    return (a,b)

data_tab = Table.from_file(csv_path_fixed)
class_label_var, feature_vars = rm_elem(data_tab.domain, inx_class_label)
assg1_domain = Domain(feature_vars, class_label_var)
data_tab = Table.from_table(domain=assg1_domain, source=data_tab)

tree_learner = SklTreeLearner()

eval_results = CrossValidation(data_tab, [tree_learner], k=10)
print("Accuracy of cross validation: {:.3f}".format(scoring.CA(eval_results)[0]))
print("AUC: {:.3f}".format(scoring.AUC(eval_results)[0]))


"""
Setting max_leaf_nodes to 4 instead of allowing it to be unlimited as in previous part.
"""
tree_learner_max = SklTreeLearner(max_leaf_nodes = 4)

eval_results_max = CrossValidation(data_tab, [tree_learner_max], k=10)
print("\n\nResult of a decision tree with the limitation to only use 4 leaf nodes\n ")
print("Accuracy of cross validation: {:.3f}".format(scoring.CA(eval_results_max)[0]))
print("AUC: {:.3f}".format(scoring.AUC(eval_results_max)[0]))
