# 
# python3 /Users/aaaaaa/pythonscripts/specificfolder/newbatchmeans.py 30 /Users/aaaaaa/pythonscripts/specificfolder/ccc.txt
# python3 /Users/aaaaaa/pythonscripts/specificfolder/newbatchmeans.py 3000 /Users/aaaaaa/pythonscripts/specificfolder/ccc.txt
# '/Users/aaaaaa/Downloads/sample5.txt'

# batchmeans hw3 stuff: 
"""This module computes a value for each batch"""
import sys

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

def retrievedata(line, data):
    """reads file"""
    five_vals = line.split(',')
    batch = five_vals[0]
    if not batch in data:
        data[batch] = []
    data[batch] += [(float(five_vals[1]), float(five_vals[2]), float(five_vals[3]), float(five_vals[4]))] # Collect data from an experiment
    
    
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
        

# part 2: 
class Batch: 
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
        self.datapoints = sample
    def calculate_average(self):
        """uses batchavg function to calculate the averages"""
        return batchavg(self.datapoints)
    def __str__(self):
        """when the object is printed the average and batchid are shown"""
        return 'avg: ' + str(self.calculate_average()) + ', batch id: ' + self.batch_id

    
#filename = '/Users/aaaaaa/Downloads/sample5.txt'    
#filename = '/Users/aaaaaa/Downloads/sample5.txt'        
# batch means stuff simplified: 
#filename = 'allzero.txt'
#filename = 'ten.txt'
#filename = input('Which data file? ')


# main arguments: 
radius = float(sys.argv[1])
filename = str(sys.argv[2])
print('setting radius to: ' + str(radius))




data = dict()               # Or data = {}
with open(filename, 'r') as h:
    for line in h:
        # excludes data with string o:
        if 'O' not in line:
            # excludes data with too many or too few commas:
            if line.count(',') == 4:
                retrievedata(line, data)

for batch, sample in data.items(): 
    if len(sample) > 0 & (Datapoint(batch, sample).is_valid() == True):
        k = Batch(batch, sample)
        print(k)
    else:
        print(batch, "\tNo data")
                        
        
        






