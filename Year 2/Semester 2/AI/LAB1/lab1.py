import numpy as np
import matplotlib.pyplot as plt
import torch

 
theta = np.linspace( 0 , 2 * np.pi , 1000 )
 
radius = 1
 
a = radius * np.cos( theta )
b = radius * np.sin( theta )
 
figure, axes = plt.subplots( 1 )
 
axes.plot( a, b )
axes.set_aspect( 1 )

t = np.array([0, 2*np.pi/3, 4*np.pi / 3,0])
x = np.sin(t)
y = np.cos(t)

axes.plot(x,y)
for i in range(0,1):
    first_chord = 2 * np.pi - np.random.random_sample()
    second_chord = 2 * np.pi - np.random.random_sample()
    e = np.array([np.sin(first_chord),np.cos(first_chord)])
    f = np.array([np.sin(second_chord),np.cos(second_chord)])
    axes.plot(e, f)

plt.show()
