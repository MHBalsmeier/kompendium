import math as mat;

a = 6371000.785;
m_l = 7.346e22;
m_t = 5.9722e24;
x_l = -384400e3;
omega_l = 2*mat.pi/(28*24*3600);
G = 6.674e-11;

x_S = 1/(1+ m_t/m_l)*x_l;

print("x- coordinate of barycenter / Earth radius: " + str(x_S/a));

f_tx = omega_l**2*(a - x_S) - G*m_l/((a - x_l)**2);

print("Force at point x = a / N/kg: " + str(f_tx));

centrifugal_difference = omega_l**2*(a - x_S) - omega_l**2*(-a - x_S);
gravity_difference = G*m_l/((a - x_l)**2) - G*m_l/((-a - x_l)**2);

print("ratio of centrifugal difference / gravity difference: " + str(abs(centrifugal_difference/gravity_difference)));
