import unittest
import json
import os
import sys
import numpy as np

# Set up the path to import from `addrressPoinntService`.
root = os.path.join(os.path.dirname(__file__))
package = os.path.join(root, '..')
sys.path.append(os.path.abspath(package))
from addressPointService import AddressPointService

class AddressPointServiceTest(unittest.TestCase):
  
    def __iter__(self,polygon,distance):
        yield from {
            "polygon": polygon,
            "distance":distance
        }.items()

    def testDefaultAlgorithm(self):
        address1=AddressPointService([7,8],[[1,2],[4,5],[8,9]])
        actualResult=address1.process()
        expectedResultStr=json.dumps({"polygon":str(np.array2string(np.array([8, 9]))),"distance":1.4142135623730951})
        expectedResult=json.loads(expectedResultStr)#returns dictionary
        print(actualResult)
        self.assertEqual(actualResult["polygon"],expectedResult["polygon"])
  
    def testNearestNeighbourAlgorithm(self):        
        pass

    #test result not empty
    def test_isupper(self):
        pass      
        address1=AddressPointService([7,8],[[1,2],[4,5],[8,9]])
        actualResult=address1.process()  
        self.assertTrue(actualResult is not None)

if __name__ == '__main__':
    unittest.main()