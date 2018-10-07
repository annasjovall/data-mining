# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 11:38:18 2018

@author: AnnaPS
"""

from Orange.data import Table, Domain
from Orange.classification import LinearSVMLearner, SVMLearner
from Orange.evaluation import CrossValidation, scoring
import matplotlib.pyplot as plt
import numpy as np

print("##########TASK 1####################")
data_tab = Table('iris')
feature_vars = list(data_tab.domain[:-1])
class_label_var = data_tab.domain[len(data_tab.domain) - 1]
iris_domain = Domain(feature_vars, class_label_var)

data_tab = Table.from_table(domain=iris_domain, source=data_tab)

print("DOMAIN: %s \nVARIABLES: %s \nATTRIBUTES: %s \nCLASS_VAR: %s" 
      % (data_tab.domain, data_tab.domain.variables, data_tab.domain.attributes, 
         data_tab.domain.class_var))
print(len(data_tab))


print("###########TASK 2###################")
svm_learner = LinearSVMLearner()
#Accuracy of cross validation: 0.940
#AUC: 0.955
eval_results = CrossValidation(data_tab, [svm_learner], k=10)
print("Accuracy of cross validation: {:.3f}".format(scoring.CA(eval_results)[0]))
print("AUC: {:.3f}".format(scoring.AUC(eval_results)[0]))


print("###########TASK 3###################")
data_tab_2d = data_tab[:50, ['sepal width', 'sepal length', 'iris']]
data_tab_2d.extend(data_tab[100:, ['sepal width', 'sepal length', 'iris']])
learner = LinearSVMLearner()
results = learner(data_tab_2d)
area_x_min = np.min(data_tab_2d[:, 'sepal width']) - 0.2
area_x_max = np.max(data_tab_2d[:, 'sepal width']) + 0.2
area_y_min = np.min(data_tab_2d[:, 'sepal length']) - 0.2
area_y_max = np.max(data_tab_2d[:, 'sepal length']) + 0.2

area_x_range_vals = np.arange(area_x_min, area_x_max, 0.01)
area_y_range_vals = np.arange(area_y_min, area_y_max, 0.01)
area_pts_x, area_pts_y = np.meshgrid(area_x_range_vals, area_y_range_vals)
area_pts = np.c_[area_pts_x.ravel(), area_pts_y.ravel()]

area_pts_class = results(area_pts.tolist())
area_pts_class = area_pts_class.reshape(area_pts_x.shape)

plt.figure()
plt.pcolormesh(area_pts_x, area_pts_y, area_pts_class, cmap=plt.cm.Set3)
plt.scatter(data_tab_2d[:, 'sepal width'], data_tab_2d[:, 'sepal length'],
c=data_tab_2d[:, 'iris'], cmap=plt.cm.Set1, edgecolors='k')
plt.xlim(area_x_min, area_x_max)
plt.ylim(area_y_min, area_y_max)
plt.show()

print("###########TASK 4###################")
def create_disc_pts(num_of_tuples, max_rad, min_rad=0):
    rad = min_rad + (max_rad - min_rad) * np.random.rand(num_of_tuples)
    ang = 2 * np.pi * np.random.rand(num_of_tuples)
    pt_x = np.multiply(rad, np.cos(ang))
    pt_y = np.multiply(rad, np.sin(ang))
    return np.c_[pt_x, pt_y]

train_disc_pts1 = create_disc_pts(75, 2)
train_disc_pts2 = create_disc_pts(75, 3.5, 2)

plt.figure()
plt.scatter(train_disc_pts1[:, 0], train_disc_pts1[:, 1], c='r')
plt.scatter(train_disc_pts2[:, 0], train_disc_pts2[:, 1], c='b')
bound_ang = np.arange(0, 2 * np.pi, 0.01)
plt.plot(2 * np.cos(bound_ang), 2 * np.sin(bound_ang))
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.show()

train_disc_pts = np.append(train_disc_pts1, train_disc_pts2, axis=0)
train_disc_pt_labels = np.append(np.zeros(75), np.ones(75))
train_disc_data_domain = Domain.from_numpy(train_disc_pts, train_disc_pt_labels)
train_disc_data_tab = Table.from_numpy(train_disc_data_domain, train_disc_pts,
train_disc_pt_labels)


print("###########TASK 5###################")
non_linear_learner = SVMLearner()
eval_results = CrossValidation(train_disc_data_tab, [non_linear_learner], k=10)
#Accuracy of cross validation: 0.960
#AUC: 0.959
print("Accuracy of cross validation: {:.3f}".format(scoring.CA(eval_results)[0]))
print("AUC: {:.3f}".format(scoring.AUC(eval_results)[0]))


print("###########EXERCISE 1###############")
non_linear_learner = SVMLearner()
eval_results = non_linear_learner(train_disc_data_tab)

print("DOMAIN: %s \nVARIABLES: %s \nATTRIBUTES: %s \nCLASS_VAR: %s" 
      % (train_disc_data_tab.domain, train_disc_data_tab.domain.variables, train_disc_data_tab.domain.attributes, 
         train_disc_data_tab.domain.class_var))
print(len(train_disc_data_tab))

area_x_min = np.min(train_disc_data_tab[:, 'Feature 1']) - 0.2
area_x_max = np.max(train_disc_data_tab[:, 'Feature 1']) + 0.2
area_y_min = np.min(train_disc_data_tab[:, 'Feature 2']) - 0.2
area_y_max = np.max(train_disc_data_tab[:, 'Feature 2']) + 0.2

area_x_range_vals = np.arange(-3.5, 3.5, 0.01)
area_y_range_vals = np.arange(-3.5, 3.5, 0.01)
area_pts_x, area_pts_y = np.meshgrid(area_x_range_vals, area_y_range_vals)
area_pts = np.c_[area_pts_x.ravel(), area_pts_y.ravel()]

area_pts_class = eval_results(area_pts.tolist())
area_pts_class = area_pts_class.reshape(area_pts_x.shape)

plt.figure()
plt.contour(area_pts_x, area_pts_y, area_pts_class, colors='k',   
            linestyles='dashed')
plt.scatter(train_disc_data_tab[:, 'Feature 1'], train_disc_data_tab[:, 'Feature 2'],
c=train_disc_data_tab[:, 'Class'], cmap=plt.cm.Set1, edgecolors='k')
plt.xlim(area_x_min, area_x_max)
plt.ylim(area_y_min, area_y_max)
plt.show()