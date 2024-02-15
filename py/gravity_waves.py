import numpy as np;
import matplotlib.pyplot as plt;
import math as mat;

n_points_x = 100;
n_points_y = 100;
wavelength_max_x = 20e3;
wavelength_max_y = 20e3;
wind_speed = 8;
wavelength_z = 2e3;
wind_speed_max = 20;
brunt_vaislala_max = 0.04;

# end of input section

def return_period(U, N, l_x, l_y, l_z):
	H = 8e3;
	f = 1e-4;
	k = 2*mat.pi/l_x;
	l = 2*mat.pi/l_y;
	m = 2*mat.pi/l_z;
	omega_i = mat.sqrt((f**2*(m**2 + 1/(4*H**2)) + N**2*(k**2 + l**2))/(m**2 + 1/(4*H**2) + k**2 + l**2));
	omega = omega_i + U*k;
	period = 2*mat.pi/omega;
	return period;

periods = np.zeros([n_points_y, n_points_x]);
wavelength_vector_x = np.linspace(100, wavelength_max_x, n_points_x);
wavelength_vector_y = np.linspace(100, wavelength_max_y, n_points_y);

for i in range(len(periods[:, 0])):
	for j in range(len(periods[0, :])):
		periods[i, j] = return_period(wind_speed, 0.02, wavelength_vector_x[j], wavelength_vector_y[i], wavelength_z);

fig = plt.figure();
plt.title("Gravity wave period (wind speed: " + str(wind_speed) + " m/s in x-direction)");
plt.xlabel("x-wavelength / km");
plt.ylabel("y-wavelength / km");
plt.contourf(1e-3*wavelength_vector_x, 1e-3*wavelength_vector_y, (1/60)*periods, cmap = "jet", levels = 1000);
cb = plt.colorbar();
cb.set_label("min");
fig.savefig("figs/gravity_wave_dispersion.png", dpi = 500);
plt.close();

wind_speed_vector_x = np.linspace(4, wind_speed_max, n_points_x);
n_vector = np.linspace(0, brunt_vaislala_max, n_points_y);

for i in range(len(periods[:, 0])):
	for j in range(len(periods[0, :])):
		periods[i, j] = return_period(wind_speed_vector_x[j], n_vector[i], 10e3, 10e10, wavelength_z);

fig = plt.figure();
plt.title("Gravity wave period (x-wavelength: 10 km)");
plt.xlabel("wind speed / m / s");
plt.ylabel("Brunt-Väisälä frequency / Hz");
plt.contourf(wind_speed_vector_x, n_vector, (1/60)*periods, cmap = "jet", levels = 1000);
cb = plt.colorbar();
cb.set_label("min");
fig.savefig("figs/gravity_wave_period.png", dpi = 500);
plt.close();






