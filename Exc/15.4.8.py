import cmath,math
import numpy as np
import matplotlib.pyplot as plt
def f(n,m,N):
    return math.cos(2*cmath.pi*n*m/N)

def dft(f):
    F = []
    for k in range(len(f)):
        s = complex(0)  # s=0*j
        for n in range(len(f)):
            power = 2j * cmath.pi * n * k / len(f)
            s += f[n] * cmath.exp(-power)
        F.append(s)
    return F
m,N =2,10
print("Let m=2 and N=5 and f(n) = cos(m*n/N) where m < N/2 and n = 0 ,..., N - 1")
f = [ f(n,m,N) for n in range(N)]
print("f : ",f)
Dft = dft(f)
print("F(k) :" , Dft)
absl = [ np.absolute(i) for i in Dft]

plt.figure(1)
plt.suptitle("15.4.8")
plt.subplot(211)
plt.title("f")
plt.stem(f)

plt.subplot(212)
plt.subplots_adjust(hspace=0.4)
plt.title("DFT")
plt.stem(absl)
plt.show()