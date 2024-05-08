import matplotlib.pyplot as plt
import numpy as np

# ji = 1000 in ullrich_real

z_0 = 1.0e-2
z_agl = 147.0
z_agl = 10.0
gravity = 9.8
c_d_p = 1005.0
u_lowest_layer = 3.0
u_lowest_layer = 1.0
temp_sfc = 292.0
temp_atmos = 299.0
temp_atmos = 293.0
temp_sfc_extrap = temp_atmos + gravity/c_d_p*z_agl

mo_l_vector = np.linspace(0.01, 200.0, 1000)
f_vector = np.zeros([len(mo_l_vector)])
f_vector_simple = np.zeros([len(mo_l_vector)])

for jl in range(len(mo_l_vector)):
    l = mo_l_vector[jl]
    bulk_richardson = z_agl*gravity*(temp_sfc_extrap - temp_sfc)/(temp_atmos*u_lowest_layer**2)
    s = (np.log(z_agl/z_0) + 4.7*z_agl/l + np.log(7.0))/(np.log(z_agl/z_0) + 4.7*z_agl/l)**2
    f_vector[jl] = z_agl/bulk_richardson*s
    f_vector_simple[jl] = z_agl/bulk_richardson

if temp_sfc > temp_sfc_extrap:
    print("Conditions are unstable.")
elif temp_sfc == temp_sfc_extrap:
    print("Conditions are indifferent.")
elif temp_sfc < temp_sfc_extrap:
    print("Conditions are stable.")

plt.title("Monin-Obukhov length formula (stable conditions)")
plt.plot(mo_l_vector, mo_l_vector)
plt.plot(mo_l_vector, f_vector)
plt.plot(mo_l_vector, f_vector_simple)
plt.xlabel("Monin-Obukhov length / m")
plt.ylabel("Right-hand side / m")
plt.legend(["unity", "RHS", "RHS simple"])
plt.xlim([0, max(mo_l_vector)])
plt.ylim([0, 1.1*max(f_vector_simple)])
plt.grid()
plt.show()



