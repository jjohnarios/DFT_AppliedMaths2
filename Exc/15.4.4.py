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


N=6
f = [ 1 if i == 0 else 0 for i in range(N)]
Dft_f = dft(f)
print("Let N=6 and f is f(n) : 1,0,...,0 where n = 0 ,.., N - 1")
print("F(K): ", Dft_f)
absl = [ np.absolute(i) for i in Dft_f]

g = [ 1 if i == 1 else 0 for i in range(N)]
Dft_g = dft(g)
print("Let N=6 and g is g(n) : 0,1,...,0 where n = 0 ,.., N - 1")
print("G(K): ", Dft_g)
abs2 = [ np.absolute(i) for i in Dft_g]


plt.figure(1)
plt.suptitle("15.4.4")
plt.subplot(211)
plt.title("DFT")
plt.stem(absl)

plt.subplot(212)
plt.subplots_adjust(hspace=0.4)
plt.title("IDFT")
plt.stem(abs2)
plt.show()

