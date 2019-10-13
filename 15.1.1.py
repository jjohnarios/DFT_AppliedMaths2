import cmath
import matplotlib.pyplot as plt
import numpy as np

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




f1=[1,1,0,0] #['1','1','0','0']
Dft=dft(f1)
print("DFT of ",f1,"is F(K): ",Dft)
absl = [ np.absolute(i) for i in Dft]

F1=[1,0,1,0]
Idft=idft(F1)
abs2=[ np.absolute(i) for i in Idft]
print("IDFT of ",F1,"is f(n):" ,Idft)

plt.figure(1)
plt.suptitle("15.1.1")
plt.subplot(211)
plt.title("DFT")
plt.stem(absl)

plt.subplot(212)
plt.subplots_adjust(hspace=0.4)
plt.title("IDFT")
plt.stem(abs2)
plt.show()




