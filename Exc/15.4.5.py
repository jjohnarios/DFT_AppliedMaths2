import cmath
import numpy as np
import matplotlib.pyplot as plt

def G_transform(F,H):
    k = len(F) # == len(H)
    G = list()
    for i in range(k):
        G.append(H[i] / F[i])
    return G


def idft(F):
    invF3=np.array([ [ 1,1,1],
         [ 1,-0.5+(cmath.sqrt(3)/2)*1j,-0.5-(cmath.sqrt(3)/2)*1j],
         [ 1, -0.5-(cmath.sqrt(3)/2)*1j,-0.5+(cmath.sqrt(3)/2)*1j] ])
    invF3=np.multiply(invF3,1/3)
    f=np.dot(invF3,F)
    return f.tolist()


print("h = f * g <-> {15 ,-2*j*sqrt(3),2*j*sqrt(3)")
print("f <-> {5,-1-j*sqrt(3) , -1 + j*sqrt(3)}")
print("Finding g using Fourier Transform")

H = [ 15 , -2j*cmath.sqrt(3),2j*cmath.sqrt(3)] # F{h=f*g} = H
F = [ 5,-1-1j*cmath.sqrt(3) , -1 + 1j*cmath.sqrt(3)] # F{f}
G = G_transform(F , H )
print("G :",G)
Idft = idft(G)
print("IDFT of G is g :",Idft)

absl = [ np.absolute(i) for i in Idft]

plt.suptitle("15.4.5")
plt.title("IDFT")
plt.stem(absl)
plt.show()






