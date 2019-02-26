# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 09:23:54 2018

@author: AnnaPS
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

print("##########TASK 1####################")
area_pts = np.random.random_integers(0, 100, (30, 2))
print(area_pts.shape)
area_x = area_pts[:,0]
area_y = area_pts[:,1]

plt.figure()
plt.scatter(area_x, area_y)
plt.xlim(-1, 101)
plt.ylim(-1, 101)
plt.show()

print("##########TASK 2####################")
estimator = KMeans(n_clusters=3, random_state=0)
k_clusters = estimator.fit(area_pts)

print("Labels: %s \nCenters: %s \nInertia: %s" 
      % (k_clusters.labels_, k_clusters.cluster_centers_, k_clusters.inertia_))


print("##########Exercise 1################")
k=5
area_pts = np.random.random_integers(0, 100, (500, 2))
estimator = KMeans(n_clusters=k, random_state=0)
k_clusters = estimator.fit(area_pts)

colors = k_clusters.labels_

plt.figure()
plt.scatter(area_pts[:,0], area_pts[:,1], c=colors)
plt.xlim(-1, 101)
plt.ylim(-1, 101)
plt.show()

print("##########TASK 3####################")
print("Visualizing sample_pts1")
rect_pts_x = np.random.random_integers(1, 15, (150, 1))
rect_pts_y = np.random.random_integers(1, 80, (150, 1))
rect_pts1 = np.concatenate((rect_pts_x, rect_pts_y), axis=1)

rect_pts_x = np.random.random_integers(31, 45, (150, 1))
rect_pts_y = np.random.random_integers(81, 160, (150, 1))
rect_pts2 = np.concatenate((rect_pts_x, rect_pts_y), axis=1)

rect_pts_x = np.random.random_integers(61, 75, (150, 1))
rect_pts_y = np.random.random_integers(1, 80, (150, 1))
rect_pts3 = np.concatenate((rect_pts_x, rect_pts_y), axis=1)

rect_pts_x = np.random.random_integers(91, 105, (150, 1))
rect_pts_y = np.random.random_integers(81, 160, (150, 1))
rect_pts4 = np.concatenate((rect_pts_x, rect_pts_y), axis=1)

sample_pts1 = np.concatenate((rect_pts1, rect_pts2, rect_pts3, rect_pts4), axis=0)

plt.figure()

plt.scatter(sample_pts1[:,0], sample_pts1[:,1])
plt.xlim(-1, 107)
plt.ylim(-1, 162)
plt.show()

print("Visualizing sample_pts1 with clustering: ")
k=4
estimator = KMeans(n_clusters=k, random_state=0)
k_clusters = estimator.fit(sample_pts1)

colors = k_clusters.labels_

plt.figure()
plt.scatter(sample_pts1[:,0], sample_pts1[:,1], c=colors)
plt.show()

print("Visualizing sample_pts2. As the 'pilars' are higher, some part of it will be closer to another 'pilars' centroid than its own.")
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

sample_pts2 = np.concatenate((rect_pts1, rect_pts2, rect_pts3, rect_pts4), axis=0)

k=4
estimator = KMeans(n_clusters=k, random_state=0)
k_clusters = estimator.fit(sample_pts2)

colors = k_clusters.labels_
center_x, center_y = k_clusters.cluster_centers_[:,0], k_clusters.cluster_centers_[:,1]

plt.figure()
plt.scatter(sample_pts2[:,0], sample_pts2[:,1], c=colors)
plt.scatter(center_x, center_y, marker="x", c='r')
plt.show()