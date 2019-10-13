import cmath
import matplotlib.pyplot as plt
import numpy as np

def dft(f):
    F = []
    for k in range(len(f)):
        s = complex(0)  # s=0*j
        for n in range(len(f)):
            power = 2j * cmath.pi * n * k / len(f)
            s += f[n] * cmath.exp(-power)
        F.append(s)
    return F

N = 8
print("Let N=8 and f(n)  where n = 0 ,.., N - 1 \nf(n) = 1 when n is even and f(n) = 0 when n is odd")
f = [1 if n%2 == 0 else 0 for n in range(N)]
Dft = dft(f)
print("DFT of",f," is :",Dft)
print("and F is real")

absl = [ np.absolute(i) for i in Dft]

plt.suptitle("15.5.5")
plt.title("DFT")
plt.stem(absl)
plt.show()