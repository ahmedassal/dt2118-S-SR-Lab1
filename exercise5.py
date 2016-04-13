import numpy as np
import matplotlib.pyplot as plt
import proto 
import tools
reload(proto)
reload(tools)

example = np.load('C:\Users\Linnea\Desktop\dt2118_lab1_2016-04-01\example.npz')['example'].item()
tidigits = np.load('C:\Users\Linnea\Desktop\dt2118_lab1_2016-04-01\etidigits.npz')['tidigits']

for i in range(0,len(tidigits)):
    print 'SAMPLE' , tidigits[i]['samples']
    
