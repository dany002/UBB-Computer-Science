import numpy as np
import matplotlib.pyplot as plt

 
theta = np.linspace( 0 , 2 * np.pi , 1000 )
 
radius = 1
 
a = radius * np.cos( theta )
b = radius * np.sin( theta )
 
figure, axes = plt.subplots( 1 )
 
axes.plot( a, b)
axes.set_aspect( 1 )

t = np.array([0, 2*np.pi/3, 4*np.pi / 3,0])
x = np.sin(t)
y = np.cos(t)

axes.plot(x,y,linewidth=10)
sum = 0
count = 0
for i in range(0,100):
    first_point = 2 * np.pi * np.random.random_sample()
    second_point = 2 * np.pi * np.random.random_sample()
    e = np.array([np.cos(first_point),np.cos(second_point)])
    f = np.array([np.sin(first_point),np.sin(second_point)])
    #axes.plot(e, f)
    if ((e[0] - e[1]) ** 2 + (f[0] - f[1]) ** 2) ** 0.5 > radius * 3 ** 0.5:
        count += 1
    sum += 1
    


print("Probability for the 1st case is %.4f" % (count / sum))

for i in range(1):
    new_point_for_radius = np.random.random_sample() * 2*np.pi
    x = np.cos(new_point_for_radius)
    y = np.sin(new_point_for_radius)
    v = np.array([-y,x])
    norm_vector = v / radius
    axes.plot([0, x], [0, y])
    axes.plot([0, norm_vector[0]], [0, norm_vector[1]])
    
    
plt.show()

