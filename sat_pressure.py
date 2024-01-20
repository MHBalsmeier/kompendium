import numpy as np;
import matplotlib.pyplot as plt;
import math;

def saturation_pressure_ice_huang(temp_c):
	
	result = math.exp(43.494 - 6545.8/(temp_c + 278.0))/(temp_c + 868.0)**2
	
	return result

def saturation_pressure_ice_murphy(temp_k):
	
	result = math.exp(9.550426 - 5723.265/temp_k + 3.53068*math.log(temp_k) - 0.00728332*temp_k)
	
	return result

def saturation_pressure_ice(temp_c):
	
	if temp_c >= -80.0:
		result = saturation_pressure_ice_huang(temp_c)
	elif temp_c >= -100.0:
		huang_weight = (temp_c + 100.0)/20.0
		result = huang_weight*saturation_pressure_ice_huang(temp_c) + (1.0 - huang_weight)*saturation_pressure_ice_murphy(temp_c + 273.15)
	else:
		result = saturation_pressure_ice_murphy(temp_c + 273.15)
	
	return result

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

temp_c_water_vector = np.linspace(-50, 100, 10000);
sat_pressure_water_vector = np.zeros([len(temp_c_water_vector)]);

for ji in range(len(temp_c_water_vector)):
	sat_pressure_water_vector[ji] = math.log10(sat_pressure_water(temp_c_water_vector[ji]))

temp_c_ice_vector = np.linspace(-120, 0, 10000);
sat_pressure_ice_vector = np.zeros([len(temp_c_ice_vector)]);

for ji in range(len(temp_c_ice_vector)):
	sat_pressure_ice_vector[ji] = math.log10(saturation_pressure_ice(temp_c_ice_vector[ji]))

fig = plt.figure()
plt.title("Sättigungsdampfdruck")
plt.plot(temp_c_water_vector, sat_pressure_water_vector)
plt.plot(temp_c_ice_vector, sat_pressure_ice_vector)
plt.xlim([min(temp_c_ice_vector), max(temp_c_water_vector)])
plt.ylim([min(sat_pressure_ice_vector), max(sat_pressure_water_vector)])
plt.legend(["über Wasser", "über Eis"])
plt.xlabel(r"Temperatur / $^\circ$C")
plt.ylabel("log10(psat / Pa)")
plt.grid()
fig.savefig("figs/sat_pressure.png", dpi = 500)








