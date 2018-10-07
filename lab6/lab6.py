# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 00:11:38 2018

@author: AnnaPS
"""

from Orange.data import Table, Domain
from Orange.classification import NNClassificationLearner
from Orange.evaluation import CrossValidation, scoring

data_tab = Table('iris')
feature_vars = list(data_tab.domain[:-1])
class_label_var = data_tab.domain[len(data_tab.domain) - 1]
iris_domain = Domain(feature_vars, class_label_var)

data_tab = Table.from_table(domain=iris_domain, source=data_tab)

print("DOMAIN: %s \nVARIABLES: %s \nATTRIBUTES: %s \nCLASS_VAR: %s" 
      % (data_tab.domain, data_tab.domain.variables, data_tab.domain.attributes, 
         data_tab.domain.class_var))
print(len(data_tab))


tree_learner = NNClassificationLearner(hidden_layer_sizes=(10,), max_iter = 1750)
#Accuracy of cross validation: 0.953
#AUC: 0.991
eval_results = CrossValidation(data_tab, [tree_learner], k=10)
print("Accuracy of cross validation: {:.3f}".format(scoring.CA(eval_results)[0]))
print("AUC: {:.3f}".format(scoring.AUC(eval_results)[0]))

#####################TASK 3##########################
tree_learner2 = NNClassificationLearner(hidden_layer_sizes=(10,), max_iter = 2000, 
                                        verbose = True, solver = "sgd", 
                                        learning_rate_init = 3, learning_rate = "invscaling",
                                        power_t = 0.3)
#Needs ~1667 iterations. Same accuracy and AUC as before.
#When learning rate init = 0.01 we need 445 iterations. Better Acc and AUC. Accuracy: 0.960, AUC: 0.997 
#When learning rate init = 1 we need 81 iterations. Accuracy: 0.960, AUC: 0.993.
#When learning rate init = 3, we need 4 iterations. Accuracy: 0.587, AUC: 0.729.
#When learning rate dynamically adjusted, we need 7 iterations. Almost back to same accuracy. Definetly better than before. Accuracy: 0.913, AUC: 0.966
eval_results = CrossValidation(data_tab, [tree_learner2], k=10)
print("Accuracy of cross validation (task 3): {:.3f}".format(scoring.CA(eval_results)[0]))
print("AUC: {:.3f}".format(scoring.AUC(eval_results)[0]))