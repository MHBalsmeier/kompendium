import numpy as np
import matplotlib.pyplot as plt
import math

t_0 = 273.15
n_a = 6.02214076e23
m_v = n_a*0.002991e-23

def c_p_water(temp_c):

	# This function returns c_p of water.

	# For "positive" temperatures we use the formula cited in Pruppacher and Klett (2010), p. 93, Eq. (3-15).

	if (temp_c>=0.0):
		# clipping values that are too extreme for this approximation
		if (temp_c>35.0):
			temp_c = 35.0
		c_p_water = 0.9979 + 3.1e-6*(temp_c-35.)**2 + 3.8e-9*(temp_c-35.)**4
	# This is the case of supercooled water. We use the formula cited in Pruppacher and Klett (2010), p. 93, Eq. (3-16).
	else:
		# clipping values that are too extreme for this approximation
		if (temp_c<-37.0):
			temp_c = -37.0
		c_p_water = 1.000938 - 2.7052e-3*temp_c - 2.3235e-5*temp_c**2 + 4.3778e-6*temp_c**3 + 2.7136e-7*temp_c**4
	
	# unit conversion from IT cal/(g*K) to J/(kg*K)
	c_p_water = 4186.8*c_p_water
	
	return c_p_water

def c_p_ice(temperature):

	# This function returns c_p of ice.
	# It follows Eq. (4) in Murphy DM, Koop T. Review of the vapour pressures of ice and supercooled water for atmospheric applications.
	# QUARTERLY JOURNAL OF THE ROYAL METEOROLOGICAL SOCIETY. 2005;131(608):1539-1565.

	# ice cannot exist in equilibrium at temperatures > T_0
	if (temperature>t_0):
		temperature = t_0
	# clipping values that are too extreme for this approximation
	if (temperature<20.0):
		temperature = 20.0
	c_p_ice = -2.0572 + 0.14644*temperature + 0.06163*temperature*math.exp(-(temperature/125.1)**2)
	# unit conversion from J/(mol*K) to J/(kg*K)
	c_p_ice = c_p_ice/m_v
	
	return c_p_ice

temp_c_water_vector = np.linspace(-50, 100, 10000)
c_p_water_vector = np.zeros([len(temp_c_water_vector)])

for ji in range(len(temp_c_water_vector)):
	c_p_water_vector[ji] = c_p_water(temp_c_water_vector[ji])
  
temp_c_ice_vector = np.linspace(-150, 0, 10000)
c_p_ice_vector = np.zeros([len(temp_c_ice_vector)])

for ji in range(len(temp_c_water_vector)):
	c_p_ice_vector[ji] = c_p_ice(temp_c_ice_vector[ji] + t_0)

fig = plt.figure()
plt.title(r"$c_p$ von $H_2O$")
plt.plot(temp_c_water_vector, c_p_water_vector)
plt.plot(temp_c_ice_vector, c_p_ice_vector)
plt.xlim([min(temp_c_ice_vector), max(temp_c_water_vector)])
plt.ylim([min(c_p_ice_vector) - 50.0, max(c_p_water_vector) + 50.0])
plt.legend(["Wasser", "Eis"])
plt.xlabel(r"Temperatur / $^\circ$C")
plt.ylabel(r"$c_p$ / J/(kg*K)")
plt.grid()
fig.savefig("figs/c_p_h2o.png", dpi = 500)








