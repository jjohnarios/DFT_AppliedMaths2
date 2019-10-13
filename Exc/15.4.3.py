import cmath
import matplotlib.pyplot as plt
import numpy as np
def f(n,k0,N):
    return cmath.exp(2j*cmath.pi*n*k0 / N)

def dft(f,k0):
    F = []
    for k in range(len(f)):
        s = complex(0)  # s=0*j
        for n in range(len(f)):
            power = 2j * cmath.pi * n * k / len(f)
            s += f[n] * cmath.exp(-power)
        F.append(s)
    return F


k0, N = 2,5
f = [ f(n,k0,N) for n in range(N)]
Dft = dft(f,k0)
print("Let k0=2 and N=5 and f(n) = exp(2*pi*j*k0*n/N ) where n = 0 ,.., N - 1 ")
print("f is ",f)
print("DFT of f is F(K): ",Dft)
print("For k!=k0 is 0 and for k=k0 is N=5")
absl = [ np.absolute(i) for i in Dft]

plt.suptitle("15.4.3")
plt.title("DFT")
plt.stem(absl)
plt.show()