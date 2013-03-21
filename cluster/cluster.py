# A data structure to represent cluster
#
# Creator: Anant Bhardwaj

import re, random

class Cluster(object):
  def __init__(self, point):  
    self.points=[]
    self.points.append(point)
  
  def add_point(self, point):
    self.points.append(point)  
    
  def get_points(self):
    return self.points


