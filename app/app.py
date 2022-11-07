from app.addressPointService import AddressPointService
from app.distanceAlgorithm import Distance

address1=AddressPointService(Distance.Default,[7,8],[[1,2],[4,5],[8,9]])
address1.printResults()
address2=AddressPointService(Distance.Spatial,[7,8],[[1,2],[4,5],[8,9]])
address2.printResults()

