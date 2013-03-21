# K-Means Clustering
#
# Creator: Anant Bhardwaj


'''
TODOs:
	- convergance test
'''

import re, random
import util
from cluster import Cluster

class KMeansCluster(object):
  def __init__(self, k, v):
    self.k = k
    self.v = v    
    self.clusters = []
  
  def set_initial_k(self):
    random_numbers = []
    while(len(random_numbers) < self.k):
      num = random.randint(0, len(self.v)-1)
      if num not in random_numbers:
        random_numbers.append(num)
        self.clusters.append(Cluster(num))
    
    
  def return_clusters(self):
    return self.clusters
  
    
  def find_nearest_cluster(self, p):
    min = self.clusters[0]
    cluster = self.clusters[0]
    for c in self.clusters:
      d = self.func_distance(self.func_magnitude(p), c.get_centroid())
      if(min > d):
        cluster = c
        min = d
    return cluster
    
    
  def cluster(self):
    for i in range(100):       
      for point in self.v:
        c = self.find_nearest_cluster(point)
        c.add_point(point)
      
  
  



