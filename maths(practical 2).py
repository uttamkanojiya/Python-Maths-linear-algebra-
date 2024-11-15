#practical number 2a
import matplotlib.pyplot as plt
x=2+6j
a=[-2+2j,1-1j,2+2j,0+1j,1+4j]
x=[z.real for z in a]
y=[z.imag for z in a]
plt.scatter(x,y,color='red')
plt.show()
