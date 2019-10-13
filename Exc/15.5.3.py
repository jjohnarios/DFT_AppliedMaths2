import cmath,math
import matplotlib.pyplot as plt
import numpy as np
def f(n,N):
    return math.cos(4*math.pi*n/N)

def g(n,N):
	return math.cos(4*math.pi*n/N -math.pi/4)

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
print("Let N=5 and f(n) = cos(4*pi*n/N) where n = 0 ,..., N - 1")
f = [ f(n,N) for n in range(N)]
print("f : ",f)
Dft_f = dft(f)
print("F(k) :" , Dft_f)
absl = [ np.absolute(i) for i in Dft_f]

print("Let N=5 and g(n) = cos(4*pi*n/N -pi/4) where n = 0 ,..., N - 1")
g = [ g(n,N) for n in range(N)]
print("g : ",g)
Dft_g = dft(g)
print("G(k) :" , Dft_g)
abs2 = [ np.absolute(i) for i in Dft_g]


plt.figure(1)
plt.suptitle("15.5.3")
plt.subplot(211)
plt.title("DFT  of cos(4*pi*n/N) ")
plt.stem(absl)

plt.subplot(212)
plt.subplots_adjust(hspace=0.4)
plt.title("DFT of cos(4*pi*n/N -pi/4)")
plt.stem(abs2)
plt.show()
