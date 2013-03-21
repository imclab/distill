# Hierarchical Clustering
#
# Creator: Anant Bhardwaj

import re, random
from cluster import Cluster

class HierarchicalCluster(object):
  def __init__(self, v):
    self.v = v    
	self.clusters = []
    
    
  def cluster(self):
	  self.clusters = v[0]
	  while(len(self.clusters)!=1){    
		  for c in self.clusters:
			centroid = c.get_centroid()
			print "centroid: " + str(centroid)        
			if(c.reset_centroid() == centroid):
			  break
			
		  for point in self.v:
			c = self.find_nearest_cluster(point)
			c.add_point(point)



