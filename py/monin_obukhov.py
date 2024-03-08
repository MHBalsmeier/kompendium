import matplotlib.pyplot as plt
import numpy as np

# jl = 1000 in ullrich_real

z_0 = 1.0279899463057518E-002
z_agl = 291.50790405273438
gravity = 9.8
c_d_p = 1005.0
u_lowest_layer = 3.0568986604327884
temp_sfc = 292.64180557174751
temp_atmos = 292.58439115255260
temp_sfc_extrap = temp_atmos + gravity/c_d_p*z_agl

mo_l_vector = np.linspace(0, 30, 1000)
f_vector = np.zeros([len(mo_l_vector)])
f_vector_simple = np.zeros([len(mo_l_vector)])

for jl in range(len(mo_l_vector)):
	l = mo_l_vector[jl]
	one_over_a = -temp_atmos*u_lowest_layer**2/(gravity*(temp_sfc - temp_sfc_extrap))
	f_vector[jl] = one_over_a*(np.log(z_agl/z_0) + 4.7*z_agl/l + np.log(7.0))/(np.log(z_agl/z_0) + 4.7*z_agl/l)**2
	f_vector_simple[jl] = one_over_a*(np.log(z_agl/z_0) + np.log(7.0))/np.log(z_agl/z_0)**2

plt.title("Monin-Obukhov length formula (stable conditions)")
plt.plot(mo_l_vector, mo_l_vector)
plt.plot(mo_l_vector, f_vector)
plt.plot(mo_l_vector, f_vector_simple)
plt.xlabel("Monin-Obukhov length / m")
plt.ylabel("Right-hand side / m")
plt.legend(["l = l", "RHS", "RHS simple"])
plt.xlim([0, max(mo_l_vector)])
plt.ylim([0, 1.1*max(f_vector_simple)])
plt.grid()
plt.show()



