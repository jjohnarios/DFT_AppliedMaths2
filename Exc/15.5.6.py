import cmath,math
import matplotlib.pyplot as plt
import numpy as np

def idft(F):
	f=[]
	for n in range(len(F)):
		s=complex(0)
		for k in range(len(F)):
			power=2j*cmath.pi*n*k/len(F)
			s+=F[k]*cmath.exp(power)
		f.append((1/len(F))*s )
	return f

def dft(f):
    F = []
    for k in range(len(f)):
        s = complex(0)  # s=0*j
        for n in range(len(f)):
            power = 2j * cmath.pi * n * k / len(f)
            s += f[n] * cmath.exp(-power)
        F.append(s)
    return F

def g(m,n,N):
	return math.cos(2*cmath.pi *m*n/N)

N = 30
print("F(k) = 1 when k = 4 otherwise F(k) = 0 where k = 0, 1 ,..., 29 ")
F = [1 if k == 3 else 0 for k in range(N)]
Idft = idft(F)
print("IDFT of F is ",Idft,'\n')
absl = [ np.absolute(i) for i in Idft]

N = 3 
print("Let N=3 and g(n) = cos(2*pi*m*n/N) where m,n = 0 ,1,...,N - 1")
g1 = [ g(m,n,N) for m in range(N) for n in range(N)]
Dftg1 = dft(g1)
print("g :",g1,'\n')
print("DFT of g is :",Dftg1)
abs2 = [ np.absolute(i) for i in Dftg1]

plt.figure(1)
plt.suptitle("15.5.6")
plt.subplot(211)
plt.title("IDFT of F")
plt.stem(absl)

plt.subplot(212)
plt.subplots_adjust(hspace=0.4)
plt.title("DFT of cos(2*pi*m*n/N)")
plt.stem(abs2)
plt.show()

