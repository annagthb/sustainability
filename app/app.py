from addressPointService import AddressPointService
from distanceAlgorithm import Distance


address1=AddressPointService([7,8],[[1,2],[4,5],[8,9]],Distance.Default)
address1.process()
print(address1)


address2=AddressPointService([7,8],[[1,2],[4,5],[8,9]],Distance.Default)
address2.process()
print(address2)

