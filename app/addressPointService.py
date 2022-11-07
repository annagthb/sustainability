import numpy as np
import pandas as pd
import scipy as sp
from app.distanceAlgorithm import Distance
import math
from scipy.spatial import distance

class AddressPointService:
    def __init__(self,algorithm,addressPoint,polygonPoints):
        self.addressPoint=np.array(addressPoint)
        self.polygonPoints=np.array(polygonPoints)
        self.matchingPolygon=[]
        self.minDistance=0
        self.process(algorithm)

    def process(self,algorithm=Distance.Default):
        self.calculateDistance(algorithm)

    def calculateDistance(self,algorithm):
        if (algorithm==Distance.Nearest):
            self.applyNearest()
        elif(algorithm==Distance.Haversine):
            self.applyHaversine()
        elif(algorithm==Distance.Spatial):
            self.applySpatialDistance
        else:
            self.applyDefaultDistance()

    def applyNearest(self):
        pass

    def applyHaversine(self):
        pass

    def applySpatialDistance(self):
        pass


    def applyEuclideanDistance(self):
        minDistance=math.inf
        polygonId=0
        id=0
        for point in self.polygonPoints:
            distance=math.sqrt((self.addressPoint[0]-point[0])*(self.addressPoint[0]-point[0]) + (self.addressPoint[1]-point[1])*(self.addressPoint[1]-point[1]))
            if (distance<minDistance):
                minDistance=distance
                polygonId=id
            id=id+1
        self.minDistance=minDistance
        self.matchingPolygon=self.polygonPoints[polygonId]

    def printResults(self):
        print("the matching polygon is {polygon} and its distance from the given address is {distance}".format(polygon=self.matchingPolygon,distance=self.minDistance))

