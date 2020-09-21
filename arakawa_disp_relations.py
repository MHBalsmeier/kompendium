import numpy as np;
import matplotlib.pyplot as plt;
import math;

fig = plt.figure();

epsilon = 1e-3;

kappa_vector = np.linspace(0 + epsilon, 2*math.pi + epsilon, 10000);
velocitys_array = np.zeros([len(kappa_vector), 4]);

for i in range(len(kappa_vector)):
	kappa = kappa_vector[i];
	velocitys_array[i, 0] = math.sin(kappa)/kappa;
	velocitys_array[i, 1] = math.cos(kappa);
	velocitys_array[i, 2] = math.sqrt((2 - 2*math.cos(kappa))/(kappa**2));
	velocitys_array[i, 3] = math.sin(kappa)/math.sqrt(2 - 2*math.cos(kappa));

plt.title("Dispersionsrelationen Arakawa-Gitter");
plt.plot(kappa_vector, velocitys_array[:, 0]);
plt.plot(kappa_vector, velocitys_array[:, 1]);
plt.plot(kappa_vector, velocitys_array[:, 2]);
plt.plot(kappa_vector, velocitys_array[:, 3]);
plt.xlim([min(kappa_vector), max(kappa_vector)]);
plt.ylim([np.min(velocitys_array), np.max(velocitys_array)]);
plt.legend([r"$c_{ph}$ A-Gitter", r"$c_{gr}$ A-Gitter", r"$c_{ph}$ C-Gitter", r"$c_{gr}$ C-Gitter"]);
plt.xlabel(r"$\kappa$");
plt.ylabel(r"$\tilde{c}$");
fig.savefig("figs/arakawa_disp_relations.png");
