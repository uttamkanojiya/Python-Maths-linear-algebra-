#practical numberr 2b
#plotting in 90 degree
import matplotlib.pyplot as plt
x=2+4j
plt.scatter(x.real,x.imag,color='red')
plt.scatter(x.real-1,x.imag,color='blue')#for 90 degree
plt.scatter(x.real-1,x.imag-1,color='yellow')#for 180 degree
plt.scatter(x.real,x.imag-1,color='green')#for 270 degree
plt.scatter(x.real+1,x.imag+1,color='red')#for 360 degree ,it is not correct
plt.show()
