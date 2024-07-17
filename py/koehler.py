import numpy as np
import matplotlib.pyplot as plt
import math

rho_w = 1024.0
t = 280.0
gamma = 0.072
k_b = 1.380649e-23
n_a = 6.02214076e23
r = k_b*n_a
m_w = 0.018
r_w = r/m_w

def calc_oversat_ratio(d, n_s):

    # This function evaluates the Koehler equation.
    
    # calculation of the result
    result = 4.0*gamma/(r_w*t*d*rho_w) - 6.0*m_w*n_s/(math.pi*d**3*rho_w)
    result = np.exp(result)
    
    return result

d_vector = np.linspace(1e-8, 1e-5, 10000)
oversat_vector_1 = np.zeros([len(d_vector)])
oversat_vector_2 = np.zeros([len(d_vector)])
oversat_vector_3 = np.zeros([len(d_vector)])

n_s_1 = 0.5e-18
n_s_2 = 0.5e-17
n_s_3 = 0.5e-16
for ji in range(len(d_vector)):
    oversat_vector_1[ji] = calc_oversat_ratio(d_vector[ji], n_s_1)
    oversat_vector_2[ji] = calc_oversat_ratio(d_vector[ji], n_s_2)
    oversat_vector_3[ji] = calc_oversat_ratio(d_vector[ji], n_s_3)

fig = plt.figure()
x_vector = 1.0e6*d_vector
plt.title("Dampfdruck über einer gekrümmten Lösung")
plt.plot(x_vector, 100.0*(oversat_vector_1 - 1))
plt.plot(x_vector, 100.0*(oversat_vector_2 - 1))
plt.plot(x_vector, 100.0*(oversat_vector_3 - 1))
plt.legend([r"n$_s$ = " + str(n_s_1) + " mol", r"n$_s$ = " + str(n_s_2) + " mol", r"n$_s$ = " + str(n_s_3) + " mol"])
plt.xlim([min(x_vector), max(x_vector)])
plt.xscale("log")
plt.ylim([-1.0, 1.0])
plt.xlabel(r"D / $\mu$m")
plt.ylabel("p / p$_S^{(0)}$ / %")
plt.grid()
fig.savefig("figs/koehler.png", dpi = 200)








