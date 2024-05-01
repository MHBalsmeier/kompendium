import numpy as np
import matplotlib.pyplot as plt
import math

t_0 = 273.15

def saturation_pressure_ice_huang(temp_c):
    
    result = math.exp(43.494 - 6545.8/(temp_c + 278.0))/(temp_c + 868.0)**2
    
    return result

def saturation_pressure_ice_murphy(temp_k):
    
    result = math.exp(9.550426 - 5723.265/temp_k + 3.53068*math.log(temp_k) - 0.00728332*temp_k)
    
    return result

def dsaturation_pressure_ice_huang_dT(temp_c):

    # This function computes the derivative of the function saturation_pressure_ice_huang.

    dsaturation_pressure_ice_huang_dT = saturation_pressure_ice_huang(temp_c)*(6545.80/(temp_c + 278.0)**2 - 2.0/(temp_c + 868.0))

    return dsaturation_pressure_ice_huang_dT

def dsaturation_pressure_ice_murphy_dT(temp_k):

    # This function computes the derivative of the function saturation_pressure_ice_murphy.
    
    dsaturation_pressure_ice_murphy_dT = saturation_pressure_ice_murphy(temp_k)*(5723.265/temp_k**2 + 3.53068/temp_k - 0.00728332)

    return dsaturation_pressure_ice_murphy_dT

def saturation_pressure_ice(temp_c):
    
    if temp_c >= -80.0:
        result = saturation_pressure_ice_huang(temp_c)
    elif temp_c >= -100.0:
        huang_weight = (temp_c + 100.0)/20.0
        result = huang_weight*saturation_pressure_ice_huang(temp_c) + (1.0 - huang_weight)*saturation_pressure_ice_murphy(temp_c + 273.15)
    else:
        result = saturation_pressure_ice_murphy(temp_c + 273.15)
    
    return result

def dsaturation_pressure_ice_dT(temp_k):

    # This function computes the derivative of the function saturation_pressure_over_ice.

    # calculating the temperature in degrees Celsius
    temp_c = temp_k - t_0

    # at temperatures > 0 degrees Celsius ice cannot exist in equilibrium which is why this is clipped
    if (temp_c>0.0):
        dsaturation_pressure_ice_dT = 0.0
    elif (temp_c>=-80.0):
        dsaturation_pressure_ice_dT = dsaturation_pressure_ice_huang_dT(temp_c)
    elif (temp_c>=-100.0):
        huang_weight = (temp_c + 100.0)/20.0
        dsaturation_pressure_ice_dT = huang_weight*dsaturation_pressure_ice_huang_dT(temp_c) + (1.0 - huang_weight)*dsaturation_pressure_ice_murphy_dT(temp_k)
    elif (temp_k>=110.0):
        dsaturation_pressure_ice_dT = dsaturation_pressure_ice_murphy_dT(temp_k)
    # clipping too extreme values for this approximation
    else:
        dsaturation_pressure_ice_dT = 0.0

    return dsaturation_pressure_ice_dT

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

def dsat_pressure_water_dT(temperature):

    # This function computes the derivative of the function saturation_pressure_over_water.
    
    # calculating the temperature in degrees Celsius
    temp_c = temperature - t_0

    # these are the limits of this approximation
    if (temp_c>100.0):
        dsat_pressure_water_dT = 0.0
    elif (temp_c<0.0):
        dsat_pressure_water_dT = 0.0
    else:
        dsat_pressure_water_dT = sat_pressure_water(temperature-t_0)*(4924.99/(temp_c + 237.1)**2 - 1.57/(temp_c + 105.0))

    return dsat_pressure_water_dT

temp_c_water_vector = np.linspace(-50, 100, 10000)
sat_pressure_water_vector = np.zeros([len(temp_c_water_vector)])

for ji in range(len(temp_c_water_vector)):
    sat_pressure_water_vector[ji] = math.log10(sat_pressure_water(temp_c_water_vector[ji]))

temp_c_ice_vector = np.linspace(-120, 0, 10000)
sat_pressure_ice_vector = np.zeros([len(temp_c_ice_vector)])

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

dsat_pressure_water_vector_dT_ana = np.zeros([len(temp_c_water_vector)])
dsat_pressure_water_vector_dT_num = np.zeros([len(temp_c_water_vector)])

for ji in range(len(dsat_pressure_water_vector_dT_ana)):
    temp_c = temp_c_water_vector[ji]
    dsat_pressure_water_vector_dT_ana[ji] = dsat_pressure_water_dT(temp_c + t_0)
    dsat_pressure_water_vector_dT_num[ji] = sat_pressure_water(temp_c+0.5) - sat_pressure_water(temp_c-0.5)

fig = plt.figure()
plt.title("Ableitung Sättigungsdampfdruck")
plt.plot(temp_c_water_vector, dsat_pressure_water_vector_dT_ana)
plt.plot(temp_c_water_vector, dsat_pressure_water_vector_dT_num)
plt.xlim([0*min(temp_c_water_vector), max(temp_c_water_vector)])
plt.ylim([min(dsat_pressure_water_vector_dT_ana), max(dsat_pressure_water_vector_dT_ana)])
plt.legend(["über Wasser, analytisch", "über Wasser, numerisch"])
plt.xlabel(r"Temperatur / $^\circ$C")
plt.ylabel("dp/dT / Pa")
plt.grid()
fig.savefig("figs/dsat_pressure_dT_water.png", dpi = 500)

dsat_pressure_ice_vector_dT_ana = np.zeros([len(temp_c_ice_vector)])
dsat_pressure_ice_vector_dT_num = np.zeros([len(temp_c_ice_vector)])

for ji in range(len(dsat_pressure_ice_vector_dT_ana)):
    temp_c = temp_c_ice_vector[ji]
    dsat_pressure_ice_vector_dT_ana[ji] = dsaturation_pressure_ice_dT(temp_c + t_0)
    dsat_pressure_ice_vector_dT_num[ji] = saturation_pressure_ice(temp_c+0.5) - saturation_pressure_ice(temp_c-0.5)

fig = plt.figure()
plt.title("Ableitung Sättigungsdampfdruck")
plt.plot(temp_c_ice_vector, dsat_pressure_ice_vector_dT_ana)
plt.plot(temp_c_ice_vector, dsat_pressure_ice_vector_dT_num)
plt.xlim([min(temp_c_ice_vector), max(temp_c_ice_vector)])
plt.ylim([min(dsat_pressure_ice_vector_dT_ana), max(dsat_pressure_ice_vector_dT_ana)])
plt.legend(["über Eis, analytisch", "über Eis, numerisch"])
plt.xlabel(r"Temperatur / $^\circ$C")
plt.ylabel("dp/dT / Pa")
plt.grid()
fig.savefig("figs/dsat_pressure_dT_ice.png", dpi = 500)






