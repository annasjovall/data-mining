# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 09:24:46 2018

@author: AnnaPS
"""
from Orange.data import Table
from Orange.distance import Euclidean
from Orange.clustering import hierarchical
from sklearn.cluster import KMeans
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt


print('#####################Task 1###################')
data_tab = Table('iris')
dist_mtrx = Euclidean(data_tab)
hier_cluster = hierarchical.HierarchicalClustering(n_clusters=3, linkage='average')
hier_cluster.fit(dist_mtrx)
print(hier_cluster.labels)

print('####################Task 2#####################')
print('PART-A')
rect_pts_x = np.random.random_integers(1, 15, (150, 1))
rect_pts_y = np.random.random_integers(1, 120, (150, 1))
rect_pts1 = np.concatenate((rect_pts_x, rect_pts_y), axis=1)

rect_pts_x = np.random.random_integers(31, 45, (150, 1))
rect_pts_y = np.random.random_integers(41, 160, (150, 1))
rect_pts2 = np.concatenate((rect_pts_x, rect_pts_y), axis=1)

rect_pts_x = np.random.random_integers(61, 75, (150, 1))
rect_pts_y = np.random.random_integers(1, 120, (150, 1))
rect_pts3 = np.concatenate((rect_pts_x, rect_pts_y), axis=1)

rect_pts_x = np.random.random_integers(91, 105, (150, 1))
rect_pts_y = np.random.random_integers(41, 160, (150, 1))
rect_pts4 = np.concatenate((rect_pts_x, rect_pts_y), axis=1)

sample_pts = np.concatenate((rect_pts1, rect_pts2, rect_pts3, rect_pts4), axis=0)

dist_mtrx2 = Euclidean(sample_pts)
hier_cluster2 = hierarchical.HierarchicalClustering(n_clusters=4, linkage='single')
hier_cluster2.fit(dist_mtrx2)

print("Visualizing sample_pts with clustering: ")
colors = hier_cluster2.labels

plt.figure()
plt.scatter(sample_pts[:,0], sample_pts[:,1], c=colors)
plt.show()

print('PART-B')
rad = np.random.rand(400)
ang = 2 * np.pi * np.random.rand(400)
pt_x = np.multiply(rad, np.cos(ang))
pt_y = np.multiply(rad, np.sin(ang))
disc_pts1 = np.c_[pt_x, pt_y]

rad = np.random.rand(400)
ang = 2 * np.pi * np.random.rand(400)
pt_x = np.multiply(rad, np.cos(ang)) + 1.8
pt_y = np.multiply(rad, np.sin(ang))
disc_pts2 = np.c_[pt_x, pt_y]

disc_pts = np.append(disc_pts1, disc_pts2, axis=0)

plt.figure()
plt.scatter(disc_pts1[:, 0], disc_pts1[:, 1], c='r')
plt.scatter(disc_pts2[:, 0], disc_pts2[:, 1], c='b')
plt.show()

dist_mtrx = Euclidean(disc_pts)
#Average performed much better than single
hier_cluster3 = hierarchical.HierarchicalClustering(n_clusters=2, linkage='average')
hier_cluster3.fit(dist_mtrx)

print("Visualizing disc_pts with hierarchical clustering: ")
colors = hier_cluster3.labels
#Prints number of points in each cluster
print(Counter(colors))
plt.figure()
plt.scatter(disc_pts[:,0], disc_pts[:,1], c=colors)
plt.show()

print("Visualizing disc_pts with k-means clustering: ")
estimator = KMeans(n_clusters=2, random_state=0)
k_clusters = estimator.fit(disc_pts)
colors = k_clusters.labels_

plt.figure()
plt.scatter(disc_pts[:,0], disc_pts[:,1], c=colors)
plt.show()

print("K-means clustering gave the best result.")

print('################Exercise 1##############')
colors = ['r', 'g', 'b']
markers = ['o', 'x', '^']
labels = ["Iris-setosa", "Iris-virginica", "Iris-versicolor"]
plt.figure()
#Iterate over clusters
for i in range(0, 3):
    cluster_tuple_indices = np.where(hier_cluster.labels == i)
    cluster_data = data_tab[list(cluster_tuple_indices)]
    #Iterate over species
    for j in range(0, 3):
        l = str(labels[j]) + ", cluster " + str(i) 
        cluster_set = Table(cluster_data.domain, [d for d in cluster_data if d["iris"] == labels[j]])
        #Only plot if it is not empty
        if cluster_set:
            plt.scatter(cluster_set[:,2], cluster_set[:,3], marker=markers[j], c=colors[i], label = l)

plt.legend(loc='best')
plt.show()
