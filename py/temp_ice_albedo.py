import numpy as np
import matplotlib.pyplot as plt
import math as mat

T_0 = 260
T_1 = 283
vector_length = 1000

# end of input section

def alpha_p(T, alpha_min, alpha_max):
    result = 0
    if (T < T_0):
        result = alpha_max
    if (T > T_1):
        result = alpha_min
    if (T >= T_0 and T <= T_1):
        result = alpha_max + (T - T_0)*(alpha_min - alpha_max)/(T_1 - T_0)
    return result

S_0 = 1367
sigma = 5.670374419e-8

T_diff = T_1 - T_0
T_mean = 0.5*(T_0 + T_1)
T_rad = 0.9*T_mean

temp_vector = np.linspace(T_0 - T_diff, T_1 + T_diff, vector_length)
out = np.zeros([vector_length])
in0 = np.zeros([vector_length])
in1 = np.zeros([vector_length])
in2 = np.zeros([vector_length])

for i in range(vector_length):
    T = temp_vector[i]
    out[i] = sigma*T_rad**4 + 4*sigma*T_rad**3*(T - T_mean)
    in0[i] = S_0/4*(1 - alpha_p(T, 0.2, 0.6))
    in1[i] = S_0/4*(1 - alpha_p(T, 0.4, 0.6))
    in2[i] = S_0/4*(1 - alpha_p(T, 0.2, 0.4))

fig = plt.figure(figsize = (6, 6))
plt.plot(temp_vector, out)
plt.plot(temp_vector, in0)
plt.plot(temp_vector, in1)
plt.plot(temp_vector, in2)
plt.xlim([min(temp_vector), max(temp_vector)])
plt.grid()
plt.legend(["Emission", "Absorption (Fall 1)", "Absorption (Fall 2)", "Absorption (Fall 3)"])
plt.title("Temperatur-Eis-Albedo-Rückkopplung")
plt.xlabel("T / K")
plt.ylabel("Strahlungsflussdichte / W / m^2")
fig.savefig("figs/temp_ice_albedo.png", dpi = 500)





