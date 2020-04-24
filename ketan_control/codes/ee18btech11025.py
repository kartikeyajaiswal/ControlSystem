import control
import matplotlib.pyplot as plt
import numpy

num = [100,500]  #numerator of transfer function
den = [1,3,4,12,0]  #denominator of transfer function

#Creating a transfer function G = num/den
G = control.tf(num,den) 
w = numpy.logspace(-3,3,5000)
print(G)

control.nyquist(G,w); # nyquist plot
plt.savefig('nyquist')
pz = control.pzmap(G); #pole-zero plot
print(pz)
#plt.xlim(-100,100)
#plt.ylim(-100,100)
plt.savefig('polezero')