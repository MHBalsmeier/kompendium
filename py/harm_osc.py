import numpy as np;
import matplotlib.pyplot as plt;
import math as mat;

vector_length = 1000;

time_vector = np.linspace(0, 10, 1000);
undamped = np.zeros([vector_length]);
swing = np.zeros([vector_length]);
creep = np.zeros([vector_length]);
aperiod = np.zeros([vector_length]);

omega = 2*mat.pi;
k = omega**2;
d_swing = 0.05*mat.sqrt(k);
d_creep = 1.01*mat.sqrt(k);
d_aperiod = mat.sqrt(k);
eigenf = mat.sqrt(k - d_swing**2);

for i in range(vector_length):
	t = time_vector[i];
	undamped[i] = mat.cos(omega*t);
	swing[i] = mat.exp(-d_swing*t)*mat.cos(eigenf*t);
	creep[i] = mat.exp(-(d_creep + mat.sqrt(d_creep**2 - k))*t);
	aperiod[i] = (1 + 3*t)*mat.exp(-d_aperiod*t);

fig = plt.figure(figsize = (8, 8));
plt.plot(time_vector, undamped);
plt.plot(time_vector, swing);
plt.plot(time_vector, creep);
plt.plot(time_vector, aperiod);
plt.xlim([min(time_vector), max(time_vector)]);
plt.ylim([-1.1, 1.4]);
plt.grid();
plt.legend(["ungedämpft", "Schwingfall", "Kriechfall", "aperiod. Grenzfall"], loc = 0);
plt.xlabel("t / Periode");
plt.ylabel("x / Anfangsauslenkung");
plt.title("Die vier Fälle des harm. Oszillators");
fig.savefig("figs/harm_osc_cases.png", dpi = 500);
plt.show();
plt.close();

rel_frequency_vector = np.linspace(0, 3, 1000);
amplitude_spec = np.zeros([vector_length]);
phase_spec = np.zeros([vector_length]);

for i in range(vector_length):
	omega_rel = rel_frequency_vector[i];
	omega = omega_rel*eigenf;
	amplitude_spec[i] = mat.pow((k - omega**2)**2 + 4*d_swing**2*omega**2, -0.5);
	phase_spec[i] = mat.atan(2*d_swing*omega/(k - omega**2));

fig = plt.figure(figsize = (6, 6));
ax = plt.axes();
ax.plot(rel_frequency_vector, amplitude_spec, color = "red");
ax.legend(["Amplitudenspektrum"], loc = 0);
ax.set_ylim([-0.05, 0.4]);
ax_right = ax.twinx();
ax_right.plot(rel_frequency_vector, phase_spec, color = "green");
ax_right.set_ylim([-2.5, 2.5]);
ax_right.legend(["Phasenspektrum"], loc = 2);
plt.xlim([min(rel_frequency_vector), max(rel_frequency_vector)]);
ax.grid();
ax.set_xlabel(r"$\omega/\omega_e$");
ax.set_ylabel("Amplitde / Anregungsamplitude");
ax_right.set_ylabel("Phase");
plt.title("Resonanzverhalten des harm. Oszillators");
fig.savefig("figs/harm_osc_resonance.png", dpi = 500);
plt.show();
plt.close();









