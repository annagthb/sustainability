import numpy as np
import pandas as pd
import scipy as sp
from distanceAlgorithm import Distance
import math
from scipy.spatial import distance
import json

class AddressPointService:
    def __init__(self,addressPoint,polygonPoints,algorithm=Distance.Default,):
        self.addressPoint=np.array(addressPoint)
        self.polygonPoints=np.array(polygonPoints)
        self.matchingPolygon=[]
        self.minDistance=0
        self.algorithm=algorithm

    def process(self):
        self.calculateDistance(self.algorithm)
        jsonStr=json.loads(self.to_json())
        return jsonStr#json.loads(jsonStr)

    def calculateDistance(self,algorithm):
        if (algorithm==Distance.Nearest):
            self.applyNearest()
        elif(algorithm==Distance.Haversine):
            self.applyHaversine()
        elif(algorithm==Distance.Spatial):
            self.applySpatialDistance
        else:
            self.applyEuclideanDistance()

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

    def to_json(self):
        return json.dumps({"polygon":np.array2string(self.matchingPolygon),"distance":self.minDistance})

    def getMatchingPolygonStr(self):
        return str(self.matchingPolygon.tolist() is not None and self.matchingPolygon.tolist() or "")

    def __str__(self):
        return "the matching polygon is {polygon} and its distance from the given address is {distance}".format(polygon=self.matchingPolygon,distance=self.minDistance)

