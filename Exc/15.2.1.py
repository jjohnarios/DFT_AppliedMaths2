import numpy as np
import cmath
import matplotlib.pyplot as plt

def dft(f):
	F4=np.array([[1,1,1,1],
				[1,-1j,-1,1j],
				[1,-1,1,-1],
				[1,1j,-1,-1j]])
	F=np.dot(F4,f)
	return F.tolist() 


f=[1,1,1,1]
Dft=dft(f)
print("DFT of ",f,"using matrix F4 is F=F4*f= ",Dft)
absl = [ np.absolute(i) for i in Dft]

plt.suptitle("15.2.1")
plt.title("DFT")
plt.stem(absl)
plt.show()
