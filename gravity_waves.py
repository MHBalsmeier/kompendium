import numpy as np;
import matplotlib.pyplot as plt;
import math as mat;

n_points_x = 100;
n_points_y = 100;
wavelength_max_x = 20e3;
wavelength_max_y = 20e3;
wind_speed = 8;

# end of input section

def return_period(U, l_x, l_y, l_z):
	H = 8e3;
	f = 1e-4;
	N = 0.02;
	k = 2*mat.pi/l_x;
	l = 2*mat.pi/l_y;
	m = 2*mat.pi/l_z;
	omega_i = mat.sqrt((f**2 + N**2*(k**2 + l**2)/(m**2 + 1/(4*H**2)))*(m**2 + 1/(4*H**2))/(k**2 + l**2 + m**2 + 1/(4*H**2)));
	omega = omega_i + U*k;
	period = 2*mat.pi/omega;
	return period;

periods = np.zeros([n_points_y, n_points_x]);
wavelength_vector_x = np.linspace(100, wavelength_max_x, n_points_x);
wavelength_vector_y = np.linspace(100, wavelength_max_y, n_points_y);

for i in range(len(periods[:, 0])):
	for j in range(len(periods[0, :])):
		periods[i, j] = return_period(wind_speed, wavelength_vector_x[j], wavelength_vector_y[i], 1e10);

fig = plt.figure();
plt.title("Gravity wave period (wind speed: " + str(wind_speed) + " m/s in x-direction)");
plt.xlabel("x-wavelength / km");
plt.ylabel("y-wavelength / km");
plt.contourf(1e-3*wavelength_vector_x, 1e-3*wavelength_vector_y, (1/60)*periods, cmap = "jet");
cb = plt.colorbar();
cb.set_label("min");
fig.savefig("figs/gravity_wave_dispersion.png", dpi = 500);
