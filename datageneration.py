# directory: 
# /Users/aaaaaa/pythonscripts/specificfolder/
# python3 /Users/aaaaaa/pythonscripts/specificfolder/datageneration.py 30 10 /Users/aaaaaa/pythonscripts/specificfolder/ccc.txt



# unittest stuff: 
import sys 
import random as r 


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
    
    
# start of code: 
print('generating data....')

# three main arguments: 
columns = int(sys.argv[1])
numbofbatchid = int(sys.argv[2])
namefile = str(sys.argv[3])

#namefile = str('/Users/aaaaaa/pythonscripts/specificfolder/aaavvv.txt')

#----------------
# variables that interfere with generated data: 
#randbatchcol = 1
randbatchcol = r.randint(0, 1)

if randbatchcol == 1:
    numbofbatchid = r.randint(5, 10)
    columns = r.randint(7, 20)

#outside_radius = 1
outside_radius = r.randint(0, 1)
if outside_radius == 1:
    # adjusts multiplier for gendata function
    mult = 100
    
    
# generate data: 
fulldata = gendata(columns)

# create list of the data: 
clist = []
for s in range(0, len(fulldata)):
    few = 'd' + str(s)
    rand = 'd' + str(r.randint(0, (numbofbatchid - 1)))
    oletter_switch = r.randint(0, 3)
    if (oletter_switch == 3):
        fulldata[few][r.randint(0, 3)] = 'O'
    lmn = rand + ', ' + str(fulldata[few][0]) + ', ' + str(fulldata[few][1]) + ', ' + str(fulldata[few][2]) + ', ' + str(fulldata[few][3])
    extra_comma = r.randint(0, 2)
    if (extra_comma == 2):
        lmn = lmn + ','
        
    clist.append(lmn)

# add data to the named file: 

dfile = open(namefile, 'w')

dfile.writelines("\n".join(clist))

dfile.close()

print('file generated with data')





    
