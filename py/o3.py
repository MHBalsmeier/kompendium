import numpy as np
import matplotlib.pyplot as plt
import math

def calc_o3_vmr(pressure):

	# This function calculates the ozone VMR as a function of air pressure.
	# It follows https://doi.org/10.5194/gmd-11-793-2018.

	g1 = 3.6478
	g2 = 0.83209
	g3 = 11.3515

	# calculation of the result
	calc_o3_vmr = g1*(pressure/100.0)**g2*math.exp(-pressure/(100.0*g3))*1.0e-6

	return calc_o3_vmr

pressure_vector = np.linspace(102400, 1, 10000)
o3_vector = np.zeros([len(pressure_vector)])

for ji in range(len(pressure_vector)):
	o3_vector[ji] = calc_o3_vmr(pressure_vector[ji])

z_km = -8.0*np.log(pressure_vector/102400.0)

fig = plt.figure()
plt.title("Ozonprofil")
plt.plot(z_km, o3_vector)
plt.xlim([min(z_km), max(z_km)])
plt.ylim([min(o3_vector), 1.05*max(o3_vector)])
plt.xlabel("z / km")
plt.ylabel("VMR Ozon")
plt.grid()
fig.savefig("figs/o3_profile.png", dpi = 500)








