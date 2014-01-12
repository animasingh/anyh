# implement k-means algorithm
from numpy import *
import random

class Point: 
    def __init__(self,name,feats):
        self.name = name
        self.feats = arrary(feats)
        
    def getFeats(self):
        return self.feats
    
    def getDimensionality(self):
        return len(self.feats)
    
    def distance(self,other):
        #other is another instance of Point
        res=0.0
        for i in range(self.getDimensionality()):
            res = res + (self.feats[i] - other.feats[i])**2
        return res**0.5
        
    def getName(self):
        return self.name

class Cluster:
    def __init__(self,members):
        self.members=members # list of Points that belong to the cluster
        self.centriod = self.computeCentriod()
        
    def getCentriod(self):
        return self.centriod
        
    def computeCentroid(self):
        dim= self.members[0].getDimensionality()
        sum_features = array([0.0]*dim)
        for point in self.members:
            sum_features = sum_features+point.getFeats()
        
        # mean feature vector
        mean_features = sum_features/len(self.members)
        mean_point = Point('mean',mean_features)
        
        # now find the member that is closest to the mean_features
        closestPoint = self.members[0]
        for point in self.members:
            if point.distance(mean_point)<closestPoint.distance(mean_point):
                closetPoint = point
        
        return closetPoint
        
        
    def update(self, points):
        self.points = points
        oldCentroid = self.centriod
        self.centroid = self.computeCentriod()
        return oldCentroid.distance(self.centriod)
        # returns the distance between new and old centroid
        
        
    def isIn(self,name):
        for point in self.members:
            if point.getName ==name:
                    return True
        return False
        

def kmeans(points,numClusters):
    #select numClusters random centriods
        centroids = random.sample(points,numClusters)
        clusters=[] #list of clusters
        for c in centriods:
            cluster.append(Cluster([c]))
         
        numIter=0   
        while True: #Do multiple iterations
            
            #contains a list of members in each cluster 
            members=[]
            for cluster in clusters:
                members.append([])
            
            for point in points: 
                smallestDist = point.Distance(clusters[0].getCentriod())
                smallestcidx = 0
                
                for cidx in range(1,len(clusters)):
                    dist = point.Distance(clusters[cid].getCentriod())
                    if dist<smallestDist:
                        smallestDist = dist
                        smallestcidx = cidx
                
                # add the point as a member to the closest centriod
                members[cidx].append(point)
            
            numIter=numIter+1
            biggestCentroidChange=0.0
            for cluster,idx in clusters:
                change=cluster.update(members[idx])
                if biggestCentriodChange<change:
                    biggestCentroidChange=change
            
            if biggestCentriodChange< cutoff or numIter >=maxIters:
                break
                
        print 'Number of iterations =', numIters
        return clusters
        





