import numpy as np
from gbeam import gbeam
import propagateclass as pg
from propagateclass import general_element
from propagateclass import freespace
beam1=gbeam(1.1*10**-3,780*10**-9,0)
abcd=np.array([[1,0],[-1/10**-2,1]])

len1=general_element(abcd,1)
len1.givebeam(beam1)
beam2=len1.propagate(beam1)

fp1=freespace(10*10**-2,1)
fp1.givebeam(beam1)
fp1.propagate(beam1)

beam3=fp1.propagate(len1.propagate(beam1))
print 'waist propagate:',pg.findfocus(beam2).waist
#print 'beam3 waist:',beam3.waist,'beam 3 radiuscur:',1/beam3.R1,
