# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 15:36:56 2018

@author: AnnaPS
"""
from Orange.data import Table, Domain
from Orange.classification import SklTreeLearner
from Orange.evaluation import CrossValidation, scoring

data_tab = Table.from_file('mushroom.csv')

#########################TASK 1################################
feature_vars = list(data_tab.domain[1:])
class_label_var = data_tab.domain[0]
mushroom_domain = Domain(feature_vars, class_label_var)

data_tab = Table.from_table(domain=mushroom_domain, source=data_tab)

#print("DOMAIN: %s \nVARIABLES: %s \nATTRIBUTES: %s \nCLASS_VAR: %s" 
#      % (data_tab.domain, data_tab.domain.variables, data_tab.domain.attributes, 
#         data_tab.domain.class_var))

data_tab.shuffle()
indx = int(len(data_tab)*0.8)
train_data_tab = data_tab[:indx]
test_data_tab = data_tab[indx:]

#########################TASK 2################################
def prediction (decision_tree, samples, lables):
    return [lables[int(x)] for x in decision_tree(samples)]

tree_learner = SklTreeLearner()
decision_tree = tree_learner(train_data_tab)
class_labels = data_tab.domain.class_var.values
p = prediction(decision_tree, test_data_tab, class_labels)

matches = 0
for i in range(len(test_data_tab)):
    if test_data_tab[:, 0][i][0] == p[i]:
        matches += 1
        
accuracy = matches/len(test_data_tab)
print("ACCURACY OF DECISION TREE: ")
print(accuracy)

#########################TASK 3################################
eval_results = CrossValidation(data_tab, [tree_learner], k=10)
print("Accuracy of cross validation: {:.3f}".format(scoring.CA(eval_results)[0]))
print("AUC: {:.3f}".format(scoring.AUC(eval_results)[0]))
