import numpy as np
import cmath
import matplotlib.pyplot as plt

def dftConv(f):
	F4=np.array([[1,1,1,1],
				[1,-1j,-1,1j],
				[1,-1,1,-1],
				[1,1j,-1,-1j]])
	F=np.dot(F4,f)
	g1=F.tolist()
	g=[ g1[i]*g1[i] for i in range(len(g1)) ]
	return g




f=[1,1,0,0]
Dft = dftConv(f)
print("DFT of g(n)=(f*f)(n) ,where f is",f," , is G(k)=F(k)F(k): ",Dft)
absl = [ np.absolute(i) for i in Dft]

plt.suptitle("15.4.1")
plt.title("DFT")
plt.stem(absl)
plt.show()