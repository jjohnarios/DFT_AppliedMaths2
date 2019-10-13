import cmath,math
import matplotlib.pyplot as plt
import numpy as np
def f(n,N):
    return math.sin(4*cmath.pi*n/N)

def g(n,N,theta):
	return math.sin(4*cmath.pi*n/N -theta)

def dft(f):
    F = []
    for k in range(len(f)):
        s = complex(0)  # s=0*j
        for n in range(len(f)):
            power = 2j * cmath.pi * n * k / len(f)
            s += f[n] * cmath.exp(-power)
        F.append(s)
    return F

N =5
print("Let N=5 and f(n) = sin(4*pi*n/N) where n = 0 ,..., N - 1")
f = [ f(n,N) for n in range(N)]
print("f : ",f)
Dft1 = dft(f)
print("F(k) :" , Dft1)
abs1 = [ np.absolute(i) for i in Dft1]

print("Let N=5 and theta = pi/2 and g1(n) = sin (4*pi*n/N - theta ) where n = 0 ,..., N - 1")
g1 = [ g(n,N,cmath.pi/2) for n in range(N)]
print("g1 : ",g1)
Dftg1 = dft(g1)
print("G1(k) :" , Dftg1)
abs2 = [ np.absolute(i) for i in Dftg1]

print("Let N=5 and theta = 3*pi/2 and g2(n) = sin (4*pi*n/N - theta ) where n = 0 ,..., N - 1")
g2 = [ g(n,N,3*(cmath.pi/2)) for n in range(N)]
print("g2 : ",g2)
Dftg2 = dft(g2)
print("G2(k) :" , Dftg2)
abs3 = [ np.absolute(i) for i in Dftg2]

plt.figure(1)
plt.suptitle("15.5.4")
plt.subplot(311)
plt.title("DFT of sin(4*pi*n/N)")
plt.stem(abs1)

plt.subplot(312)
plt.subplots_adjust(hspace=0.6)
plt.title("DFT of sin (4*pi*n/N - pi/2 )")
plt.stem(abs2)

plt.subplot(313)
plt.subplots_adjust(hspace=0.6)
plt.title("DFT of sin (4*pi*n/N - 3*pi/2 )")
plt.stem(abs3)
plt.show()