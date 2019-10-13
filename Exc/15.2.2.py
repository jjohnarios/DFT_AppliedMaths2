import numpy as np
import cmath
import matplotlib.pyplot as plt

def idft(F):
	invF3=np.array([ [ 1,1,1],
		 [ 1,-0.5+(cmath.sqrt(3)/2)*1j,-0.5-(cmath.sqrt(3)/2)*1j],
		 [ 1, -0.5-(cmath.sqrt(3)/2)*1j,-0.5+(cmath.sqrt(3)/2)*1j] ])
	invF3=np.multiply(invF3,1/3)
	f=np.dot(invF3,F)
	return f.tolist()


F=[3,0,6]
Idft = idft(F)
print("IDFT of ",F,"using inverse matrix F3 is f=invF3*F= ",Idft)
absl = [ np.absolute(i) for i in Idft]

plt.suptitle("15.2.2")
plt.title("IDFT")
plt.stem(absl)
plt.show()
