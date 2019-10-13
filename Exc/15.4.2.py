import cmath
import matplotlib.pyplot as plt
import numpy as np
def dft(N):
    F = []
    for k in range(N):
        s = complex(0)  # s=0*j
        for n in range(N):
            power = 2j * cmath.pi * n * k / N
            s += cmath.exp(-power)
        F.append(s)
    return F


N=8
Dft = dft(N)
print("Let N=8 and f(n) = 1 where n = 0 ,.., N - 1")
print("DFT of f is F(K): ", Dft)
absl = [ np.absolute(i) for i in Dft]

plt.suptitle("15.4.2")
plt.title("DFT")
plt.stem(absl)
plt.show()
