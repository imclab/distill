# Python DW Clustering Utils
#
# Creator: Anant Bhardwaj

import re, random
from util import *
import scipy
import scipy.spatial
import scipy.cluster


def get_magnitude(p):
	tokens = re.split('\W+', p)
	tokens = filter(lambda x: x!='', tokens)
	return float(len(tokens))

def get_distance(p1, p2):
	return levenshtein(p1, p2);


data = open("../data/crime.csv", 'rU').read()
#data = open("../data/cut.csv", 'rU').read()
#data = open("../data/labor.csv", 'rU').read()
#data = open("../data/tomcat.log", 'rU').read()
#data = open("../data/multicolumn_cut.csv", 'rU').read()
#data = open("../data/hadoop.log", 'rU').read()
lines = re.split('\n',data);
lines = filter(lambda x: x!='\n' and x!='', lines)

"""
kmc = KMeansCluster(5, lines, get_magnitude, get_distance)
kmc.set_initial_k()
kmc.cluster()
kmc.print_clusters()
"""
print(len(lines))
weight = []
i=0

for line1 in lines:
	j = 0
	weight.append([])
	for line2 in lines:
		weight[i].append(get_distance(get_signature(line1), get_signature(line2)))
		j = j + 1
	i = i + 1

#signatures = get_signatures('crime.csv');
dist_vec = scipy.spatial.distance.squareform(weight)
clusters = scipy.cluster.hierarchy.single(dist_vec)
print clusters

data ={}
cluster_index ={}
i = 0
n= len(lines)
for line in lines:
	data[i] = line;
	i= i+1
j = 0

for cluster in clusters:
	cluster_index[n+j] = [];
	data[n +j] = data[int(cluster[0])] + "\n" + data[int(cluster[1])]
	cluster_index[n+j].append(int(cluster[0]))
	cluster_index[n+j].append(int(cluster[1]))
	j =  j+1


#print data[n+j-1]

print data[cluster_index[n+j-1][0]]
print "\n===============================\n"
print data[cluster_index[n+j-1][1]]
#print "\n===============================\n"
#print data[cluster_index[cluster_index[n+j-1][1]][1]]


