import matplotlib.pyplot as plt
import numpy as np

z_0 = 0.1
z_agl = 50.0
gravity = 9.8
temp_sfc = 280.0
u_lowest_layer = 5.0
karman = 0.4
temp_atmos = 280.0
temp_sfc_extrap = temp_atmos + 0.01*z_agl

mo_l_vector = np.linspace(1, 100, 1000)
f_vector = np.zeros([len(mo_l_vector)])

for jl in range(len(mo_l_vector)):
	l = mo_l_vector[jl]
	a = -gravity*(temp_sfc - temp_sfc_extrap)/(temp_atmos*u_lowest_layer**2*karman)
	h = np.log(z_agl/z_0) + 4.7*z_agl/l
	f_vector[jl] = a*l*h**2 - h - np.log(7.0)

plt.title("Monin-Obukhov length minimization function")
plt.plot(mo_l_vector, f_vector)
plt.xlabel("Monin-Obukhov length / m")
plt.xlabel("Minimization function")
plt.grid()
plt.show()

