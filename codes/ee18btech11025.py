import control
import scipy
import numpy
import matplotlib.pyplot as plt

#enter the co-efficients of numerator in descending power of s
num = [5]

#enter the co-efficients of denominator in descending power of s
den = [1, 2, 7, 4]

G = control.tf(num, den)
w = numpy.logspace(-3,3, 5000)

#plotting the nyquist diagram
control.nyquist(G,w)
plt.title('Nyquist Diagram')
plt.xlabel('Re(s)')
plt.ylabel('Im(s)')
print(G)

#poles, zeros and gain of the transfer function
zero, pole, gain = scipy.signal.tf2zpk(num, den)
print('poles, zeros and gain of the transfer function are:')
print(zero, pole, gain)

#gain margin, phase margin, frequency for gain margin, frquency for phase margin
gm, pm, wg, wp = control.margin(G)
print('gain margin, phase margin(in degrees) are:')
print(gm, pm)

if (gm > 0 and pm > 0) or (gm < pm):
	print('stable system')
elif (gm == 0 and pm == 0) or (gm == pm):
	print('marginally stable system')
elif (gm < 0 or pm <0) or (gm > pm):
	print('unstable system')
plt.show()
