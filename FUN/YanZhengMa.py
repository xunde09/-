# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 17:26:41 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image

#打开图像
im=np.array(Image.open('1534930593(1).jpg'))

#得到图像3个维度
h,w,san=im.shape

X=[(h-x,y) for x in range(h) for y in range (w) if im[x][y][2]<200]

#将X转换成numpy的array类型，方便后续运算操作
X=np.array(X)

n_clusters=4
k_means=KMeans(init='k-means++',n_clusters=n_clusters)
k_means.fit(X)

k_means_labels=k_means.labels_
k_means_cluster_centers=k_means.cluster_centers_
k_means_labels_unique=np.unique(k_means_labels)

colors=['#4EACC5','#FF9C34','#4E9A06','#FF3300']
plt.figure()
plt.hold(True)
for k,col in zip(range(n_clusters),colors):
    my_members=k_means_labels==k
    cluster_center=k_means_cluster_centers[k]
    plt.plot(X[my_members,1],X[my_members,0],'w',markerfacecolor=col,marker='.')
    plt.plot(cluster_center[1],cluster_center[0],'o',markerfacecolor=col,markeredgecolor='k',markersize=6)

plt.title('KMeans')
plt.grid(True)
plt.show()