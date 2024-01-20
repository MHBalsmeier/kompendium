import numpy as np
import matplotlib.pyplot as plt
import math

t_0 = 273.15
n_a = 6.02214076e23
m_v = n_a*0.002991e-23

def enthalpy_evaporation(temperature):

	# This function returns the enthalpy of evaporation depending on the temperature.
	temperature = temperature

	if (temperature<t_0):
		# This follows Eq. (9) in Murphy DM, Koop T. Review of the vapour pressures of ice and supercooled water for atmospheric applications.
		# QUARTERLY JOURNAL OF THE ROYAL METEOROLOGICAL SOCIETY. 2005;131(608):1539-1565.
		# clipping values that are too extreme for these approximations
		if (temperature<236.0):
			temperature = 236.0
		enthalpy_evaporation = 56579.0 - 42.212*temperature + math.exp(0.1149*(281.6 - temperature))
		# unit conversion from J/mol to J/kg
		enthalpy_evaporation = enthalpy_evaporation/m_v
	else:
		# This follows the formula (Eq. (8)) cited by Huang:
		# A Simple Accurate Formula for Calculating Saturation Vapor Pressure of Water and Ice, 2018, DOI: 10.1175/JAMC-D-17-0334.1.
		# clipping values that are too extreme for these approximations
		if (temperature>t_0+100.0):
			temperature = t_0 + 100.0
		enthalpy_evaporation = 3151378.0 - 2386.0*temperature
	
	return enthalpy_evaporation
  
def enthalpy_sublimation(temperature):

	# This function returns the enthalpy of sublimation depending on the temperature.
	# It follows Eq. (5) in Murphy DM, Koop T. Review of the vapour pressures of ice and supercooled water for atmospheric applications.
	# QUARTERLY JOURNAL OF THE ROYAL METEOROLOGICAL SOCIETY. 2005;131(608):1539-1565.

	# clipping values that are too extreme for this approximation
	if (temperature<30.0):
		temperature = 30.0
	# sublimation is not happening in thermodynamic equilibrium at temperatures > t_0
	if (temperature>t_0):
		temperature = t_0
	
	enthalpy_sublimation = 46782.5 + 35.8925*temperature - 0.07414*temperature**2 + 541.5*math.exp(-(temperature/123.75)**2)

	# unit conversion from J/mol to J/kg
	enthalpy_sublimation = enthalpy_sublimation/m_v
	
	return enthalpy_sublimation

temp_c_evap_vector = np.linspace(-35, 100, 10000)
enthap_evap_vector = np.zeros([len(temp_c_evap_vector)])

for ji in range(len(temp_c_evap_vector)):
	enthap_evap_vector[ji] = enthalpy_evaporation(temp_c_evap_vector[ji] + t_0)

temp_c_sub_vector = np.linspace(-100, 25, 10000)
enthap_sub_vector = np.zeros([len(temp_c_evap_vector)])

for ji in range(len(temp_c_evap_vector)):
	enthap_sub_vector[ji] = enthalpy_sublimation(temp_c_sub_vector[ji] + t_0)

fig = plt.figure()
plt.title("Enthalpie von Wasser")
plt.plot(temp_c_evap_vector, enthap_evap_vector)
plt.plot(temp_c_sub_vector, enthap_sub_vector)
plt.xlim([min(temp_c_sub_vector), max(temp_c_evap_vector)])
plt.ylim([0.5*min(enthap_evap_vector), 1.05*max(enthap_sub_vector)])
plt.legend(["Kondensation", "Resublimation"])
plt.xlabel(r"Temperatur / $^\circ$C")
plt.ylabel(r"Enthalpie / J/kg")
plt.grid()
fig.savefig("figs/enthalpy.png", dpi = 500)








