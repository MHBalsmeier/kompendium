import numpy as np;
import matplotlib.pyplot as plt;
import math;

fig = plt.figure();

epsilon = 1e-3;

def sat_pressure_water(temp_c):
	
	# This function returns the saturation pressure in Pa over liquid water as a function of the temperature in °C.
	
	if (temp_c>0.0):
		result = math.exp(34.494 - 4924.99/(temp_c + 237.1))/(temp_c + 105.0)**1.57
	else:
		# Clipping values that are too extreme for this approximation.
		if (temp_c<-50.0):
			temp_c = -50.0
		result = 100.0*(6.107799961 + 4.436518521e-1*temp_c + 1.428945805e-2*temp_c**2 \
		+ 2.650648471e-4*temp_c**3 + 3.031240396e-6*temp_c**4 + 2.034080948e-8*temp_c**5 \
		+ 6.136820929e-11*temp_c**6)
	
	return result

temp_c_vector = np.linspace(-50, 100, 10000);
sat_pressure_vector = np.zeros([len(temp_c_vector)]);

for ji in range(len(temp_c_vector)):
	sat_pressure_vector[ji] = math.log10(sat_pressure_water(temp_c_vector[ji]))

plt.title("Sättigungsdampfdruck");
plt.plot(temp_c_vector, sat_pressure_vector);
plt.xlim([min(temp_c_vector), max(temp_c_vector)]);
plt.ylim([min(sat_pressure_vector), max(sat_pressure_vector)]);
plt.xlabel(r"Temperatur / $^\circ$C");
plt.ylabel("log10(psat / Pa)");
fig.savefig("figs/sat_pressure.png", dpi = 500);
