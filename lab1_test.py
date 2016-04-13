import numpy as np
import matplotlib.pyplot as plt
import proto 
from tools import lifter
reload(proto)

example = np.load('C:\Users\Linnea\Desktop\dt2118_lab1_2016-04-01\example.npz')['example'].item()
tidigits = np.load('C:\Users\Linnea\Desktop\dt2118_lab1_2016-04-01\etidigits.npz')['tidigits']


#plt.plot(example['samples'])

# SHOW IMAGE FROM EXAMPLE
#plt.imshow(example['frames'], origin = 'lower', interpolation = 'nearest', aspect = 'auto')


ef = proto.enframe(example['samples'], 400, 200)
preemphas = proto.preemp(example['frames'],0.97)
fourierTrans = proto.powerSpectrum(example['windowed'],512)
cos = proto.cepstrum(example['mspec'],13)
cosLift = lifter(cos,22)
#plt.imshow(ef, origin = 'lower', interpolation = 'nearest', aspect = 'auto')

#plt.show()  