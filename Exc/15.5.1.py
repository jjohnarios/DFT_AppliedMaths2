import cmath
import numpy as np
import matplotlib.pyplot as plt
def dft(f):
	F=[]
	for k in range(len(f)):
		s=complex(0) # s=0*j
		for n in range(len(f)):
			power=2j*cmath.pi*n* k/len(f)
			s+=f[n]*cmath.exp(-power)
		F.append(s)
	return F


def idft(F):
	f=[]
	for n in range(len(F)):
		s=complex(0)
		for k in range(len(F)):
			power=2j*cmath.pi*n*k/len(F)
			s+=F[k]*cmath.exp(power)
		f.append((1/len(F))*s )
	return f


f=[2,3,-1,1]
Dft = dft(f)
print("DFT of ",f," : ",Dft)
absl = [ np.absolute(i) for i in Dft]

F=[5,3-2j,-3,3+2j]
Idft = idft(F)
print("IDFT of ",F," : ",Idft)
abs2=[ np.absolute(i) for i in Idft]




plt.figure(1)
plt.suptitle("15.5.1")
plt.subplot(211)
plt.title("DFT")
plt.stem(absl)

plt.subplot(212)
plt.subplots_adjust(hspace=0.4)
plt.title("IDFT")
plt.stem(abs2)
plt.show()