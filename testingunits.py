
# python3 /Users/aaaaaa/pythonscripts/specificfolder/testingunits.py
import random as r 
import unittest
# tests for all functions / classes
# multiplier: 
mult = 1

def gendata(k):
    """function that generates data"""
    ndict = {}
    for k in range(0, k):
        outside_radius = r.randint(0, 1)
        if outside_radius == 1:
        # adjusts multiplier for gendata function
            mult = 100
        else:
            mult = 1
        rlist = r.sample(range(5, 10), 4)
        frlist = [float(v) for v in rlist]
        vfrlist = [c * 0.01 * mult for c in frlist]
        vfrlist[-1] = float(r.randint(1, 110))
        ndict['d' + str(k)] = vfrlist
    return ndict

# initial radius: 
radius = 1

# computes average for each batch using the data: 
def batchavg(sample):
    """computes average for each batch using the data"""
    n = 0
    x_sum = 0
    for (x, y, z, val) in sample:
        if x**2 + y**2 + z**2 <= radius:
            x_sum += val
            n += 1
    if (n == 0):
        return '[outside radius -> invalid measurement]'
        
    average = x_sum/n
    return average


# part 1: 
class Datapoint:
    """a class to represent a datapoint that takes two parameters, batch and sample 
       has a few attributes and the method is_valid()"""
    def __init__(self, batch_id, sample):
        """constructs the object"""
        self.batch_id = batch_id
        x, y, z, val = sample[0]
        self.x = x
        self.y = y
        self.z = z
        self.val = val
    def is_valid(self): 
        """checks validity of data"""
        return (type(self.batch_id) == str) and (type(self.x) == float) and (type(self.y) == float) and (type(self.z) == float) and (type(self.val) == float)
            
    
    
    
#----------------------------------    

class Test_things(unittest.TestCase):
    """performs tests for functions and classes"""
    def test_a_gendata(self):
        print('called first test...')
        self.assertEqual(len(gendata(5)) >= 1, True, \
                                            "Should be nonempty with length more than 1")
        print('testing completed....')

    def test_b_batchavg(self):
        print('called 2nd test...')
        res = batchavg([(0.01, 0.02, 0.03, 5)])
        self.assertEqual(res, 5, \
                                       "should be true with test")
        print('testing completed....')    

    def test_c_datapointclass(self):
        print('called 3rd test...')
        fvar = [(0.23, 0.01, 0.3, 17.0), (0.23, 0.01, 0.3, 17.0), (0.12, 0.15, 0.3, 23.0)]
        someval = Datapoint('2', fvar).is_valid()
        self.assertEqual(someval, True, \
                                       "should be true since the values are float")
        print('testing completed....')        
        
if __name__ == '__main__':
    unittest.main()

